"""Small CLI; no database server or agent framework."""
import argparse
import hashlib
import json
from pathlib import Path
import sys

from .model import Conversation, Graph, Candidates
from .io import load, write_json, import_export, ingest, merge, quarantine
from .validate import validate, require_valid
from .extract import prepare
from .bridge import parse_bridge_markdown
from .exporter_json import parse_exporter_json
from .views import stats, open_questions, trace, relations_of_kind
from .render import mermaid, dot, report, html_view


def parser():
    p = argparse.ArgumentParser(prog="inquiry-graph")
    sub = p.add_subparsers(dest="cmd", required=True)
    for name in ("prepare", "validate", "query", "render"):
        s = sub.add_parser(name)
        s.add_argument("input")
        if name in ("prepare", "render"):
            s.add_argument("output")
            s.add_argument("--force", action="store_true")
        if name == "query":
            s.add_argument("kind", choices=["stats", "open", "trace", "conflicts", "dependencies"])
            s.add_argument("--id")
        if name == "render":
            s.add_argument("--format", choices=["mermaid", "dot", "report", "html"], default="mermaid")
            s.add_argument("--view", choices=["all", "inquiry"], default="inquiry")
    s = sub.add_parser("import")
    s.add_argument("input")
    s.add_argument("output_dir")
    s.add_argument("--conversation-id")
    s.add_argument("--force", action="store_true")
    s = sub.add_parser("extract")
    s.add_argument("input")
    s.add_argument("output")
    source = s.add_mutually_exclusive_group(required=True)
    source.add_argument("--response-file")
    source.add_argument("--llm", action="store_true", help="live chunked extraction through llm_client")
    s.add_argument("--model", help="llm_client model id; default: llm_client get_model('extraction')")
    s.add_argument("--cache-dir", default="private/llm-cache")
    s.add_argument("--report", help="write the grounding/drop report here")
    s.add_argument("--quarantine-dir", default="private/quarantine")
    s.add_argument("--force", action="store_true")
    s = sub.add_parser("import-bridge", help="normalize a chatgpt-bridge read_chatgpt_chat transcript")
    s.add_argument("input")
    s.add_argument("output")
    s.add_argument("--user-label", default="Brian")
    s.add_argument("--force", action="store_true")
    s = sub.add_parser("import-exporter", help="normalize a Conversation Manager per-thread JSON")
    s.add_argument("input")
    s.add_argument("output")
    s.add_argument("--user-label", default="Brian")
    s.add_argument("--force", action="store_true")
    s = sub.add_parser("merge")
    s.add_argument("inputs", nargs="+")
    s.add_argument("--output", required=True)
    s.add_argument("--force", action="store_true")
    s = sub.add_parser("schema")
    s.add_argument("kind", choices=["graph", "candidates", "conversation"])
    s.add_argument("output")
    s.add_argument("--force", action="store_true")
    return p


def run(args):
    if hasattr(args, "output"):
        output = Path(args.output)
        inputs = ([args.input] if hasattr(args, "input") else getattr(args, "inputs", []))
        if getattr(args, "response_file", None):
            inputs = inputs + [args.response_file]
        for original in inputs:
            source_path = Path(original)
            if output.resolve() == source_path.resolve() or (output.exists() and source_path.exists() and output.samefile(source_path)):
                raise ValueError("output must not overwrite an input or source snapshot, even with --force")
    if args.cmd == "schema":
        cls = {"graph":Graph,"candidates":Candidates,"conversation":Conversation}[args.kind]
        write_json(args.output, cls.model_json_schema(), args.force)
    elif args.cmd == "import":
        data = json.loads(Path(args.input).read_text(encoding="utf-8"))
        convs = import_export(data, args.conversation_id)
        for c in convs:
            require_valid(Graph(id="import-check", conversations=[c]))
            # Export IDs are untrusted; hashed filename prevents directory traversal.
            name = hashlib.sha256(c.id.encode()).hexdigest()[:24] + ".json"
            write_json(Path(args.output_dir)/name, c, args.force)
        return {"imported": len(convs)}
    elif args.cmd == "prepare":
        source = load(args.input, Conversation)
        require_valid(Graph(id="prepare-check", conversations=[source]))
        write_json(args.output, prepare(source), args.force)
    elif args.cmd == "extract":
        raw = None
        try:
            source = load(args.input, Conversation)
            require_valid(Graph(id="extract-check", conversations=[source]))
            if args.response_file:
                raw = Path(args.response_file).read_text(encoding="utf-8")
                candidates = Candidates.model_validate_json(raw)
                graph = ingest(source,candidates,method="response-file",model=args.model)
            else:
                graph, report = llm_extract(source, args.model, Path(args.cache_dir))
                raw = report
                if args.report:
                    write_json(args.report, report, args.force)
            write_json(args.output,graph,args.force)
        except Exception as exc:
            location = quarantine(args.quarantine_dir,raw,exc)
            raise ValueError(f"Extraction rejected; diagnostics in {location}") from exc
        return stats(graph)
    elif args.cmd == "import-bridge":
        conv, skipped = parse_bridge_markdown(Path(args.input).read_text(encoding="utf-8"), user_label=args.user_label)
        require_valid(Graph(id="import-check", conversations=[conv]))
        write_json(args.output, conv, args.force)
        return {"conversation": conv.id, "messages": len(conv.messages), "skipped": skipped}
    elif args.cmd == "import-exporter":
        conv, skipped = parse_exporter_json(json.loads(Path(args.input).read_text(encoding="utf-8")), user_label=args.user_label)
        require_valid(Graph(id="import-check", conversations=[conv]))
        write_json(args.output, conv, args.force)
        return {"conversation": conv.id, "messages": len(conv.messages), "skipped": skipped}
    elif args.cmd == "merge":
        graph = merge([load(path,Graph) for path in args.inputs])
        write_json(args.output,graph,args.force)
        return stats(graph)
    else:
        graph = load(args.input,Graph)
        if args.cmd == "validate":
            return validate(graph)
        require_valid(graph)
        if args.cmd == "query":
            if args.kind == "stats":
                return stats(graph)
            if args.kind == "open":
                return open_questions(graph)
            if args.kind == "trace":
                return trace(graph,args.id)
            return relations_of_kind(graph,"challenges" if args.kind == "conflicts" else "depends_on")
        if args.cmd == "render":
            text = {"mermaid":lambda:mermaid(graph,args.view),"dot":lambda:dot(graph,args.view),
                    "report":lambda:report(graph),"html":lambda:html_view(graph)}[args.format]()
            path=Path(args.output)
            path.parent.mkdir(parents=True,exist_ok=True)
            # Exclusive by default; output text never executed by this application.
            with path.open("w" if args.force else "x",encoding="utf-8") as f:
                f.write(text)
    return {"ok":True}


def main(argv=None):
    args=parser().parse_args(argv)
    try:
        result=run(args)
        print(json.dumps(result,ensure_ascii=False,indent=2))
        return 1 if isinstance(result,dict) and result.get("valid") is False else 0
    except (ValueError,OSError,ImportError) as exc:
        print(json.dumps({"valid":False,"error":str(exc)},ensure_ascii=False),file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())


def llm_extract(source, model, cache_dir):
    """Run the live extractor; import lazily so the base install needs no LLM client."""
    import asyncio
    from .live_extract import extract_conversation
    if not model:
        from llm_client import get_model
        model = get_model("extraction")
    return asyncio.run(extract_conversation(source, model, cache_dir))

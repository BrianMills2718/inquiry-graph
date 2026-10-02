"""Local personal-information scan of chat text (nothing is sent anywhere).

Uses Presidio with spaCy's small English model. Hard identifiers (email, phone, card, SSN, IP, IBAN,
driver licence, passport) mark a chat HARD. Person or location names mark it REVIEW. Output lists chat ids
and entity types only, never the matched text.
"""
import argparse
import collections
import json
from pathlib import Path

from presidio_analyzer import AnalyzerEngine
from presidio_analyzer.nlp_engine import NlpEngineProvider

HARD = {"EMAIL_ADDRESS", "PHONE_NUMBER", "CREDIT_CARD", "US_SSN", "IP_ADDRESS", "IBAN_CODE", "US_DRIVER_LICENSE",
        "US_PASSPORT", "US_BANK_NUMBER", "CRYPTO", "MEDICAL_LICENSE"}
SOFT = {"PERSON", "LOCATION"}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("conv_dir", type=Path)
    ap.add_argument("decisions", type=Path)
    ap.add_argument("out", type=Path)
    ap.add_argument("--max-chars", type=int, default=40000)
    a = ap.parse_args()
    inc = {x["id"]: x["title"] for x in json.loads(a.decisions.read_text()) if x["include"]}
    nlp = NlpEngineProvider(nlp_configuration={"nlp_engine_name": "spacy", "models": [{"lang_code": "en", "model_name": "en_core_web_sm"}]}).create_engine()
    eng = AnalyzerEngine(nlp_engine=nlp, supported_languages=["en"])
    res = {}
    for f in sorted(a.conv_dir.glob("*.conv.json")):
        c = json.loads(f.read_text(encoding="utf-8"))
        if c["id"] not in inc:
            continue
        text = "\n".join(m["text"] for m in c["messages"])[: a.max_chars]
        found = collections.Counter()
        for r in eng.analyze(text=text, language="en", score_threshold=0.5):
            found[r.entity_type] += 1
        hard = {k: v for k, v in found.items() if k in HARD}
        soft = {k: v for k, v in found.items() if k in SOFT}
        res[c["id"]] = {"title": inc[c["id"]], "hard": hard, "soft": soft, "level": "HARD" if hard else ("REVIEW" if soft else "CLEAN")}
    a.out.write_text(json.dumps(res, indent=1), encoding="utf-8")
    print(json.dumps({"scanned": len(res), **collections.Counter(v["level"] for v in res.values())}))
    print("hard entity types:", dict(collections.Counter(k for v in res.values() for k in v["hard"])))


if __name__ == "__main__":
    main()

# Inquiry Graph user interfaces

The current candidate surface is the private cross-conversation topic map. Its use case,
representation decision, evidence semantics, and known limits are recorded in
[`docs/ui/topic-map/README.md`](../docs/ui/topic-map/README.md).

The builder is `tools/topic_map.py`; the HTML template is
`tools/topic_map_template.html`. The standalone HTML is generated under the gitignored
`private/xconv/` directory because it embeds exact source quotes. See `registry.yaml` for
the surface record and `learning-receipts/` for material-change evidence. Open the generated
HTML directly in a browser; it embeds its graph component bundle and needs no network access.

// Side panel and tooltips for the positions map (tools/position_topics.py).
// IG = {names: [topic name], layerSizes: [topics per level, broad to narrow], recs: [[title, date, app, kind, quote, conversation id, [topic name index, broad to narrow; negative = nearest topic, not placed by the clusterer]]]}.
(function () {
  const byChat = new Map();
  IG.recs.forEach((r, i) => { if (!byChat.has(r[5])) byChat.set(r[5], []); byChat.get(r[5]).push(i); });
  const esc = s => String(s).replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
  const panel = () => document.getElementById("ig-panel");

  window.igShow = function (i) {
    const r = IG.recs[i];
    if (!r) return;
    const path = r[6].map(n => IG.names[Math.abs(n)] + (n < 0 ? " (nearest topic)" : "")).filter((n, k, a) => n !== a[k - 1]).map(n => `<li>${esc(n)}</li>`).join("") || "<li>No topic (not clustered)</li>";
    const others = (byChat.get(r[5]) || []).filter(j => j !== i).sort((a, b) => IG.recs[a][1].localeCompare(IG.recs[b][1]));
    const list = others.slice(0, 40).map(j => `<li><button class="ig-link" data-i="${j}" data-tip="Open this statement in the panel">` +
      `${esc(IG.recs[j][1])} · ${esc(IG.recs[j][3])}: ${esc(IG.recs[j][4].slice(0, 140))}</button></li>`).join("");
    document.getElementById("ig-body").innerHTML =
      `<h2>${esc(r[0])}</h2><p class="ig-meta">${esc(r[2])} · ${esc(r[1])} · ${esc(r[3])}</p><blockquote>${esc(r[4])}</blockquote>` +
      `<h3>Topic, broad to narrow</h3><ol class="ig-path">${path}</ol>` +
      `<h3>Rest of this conversation (${others.length})</h3>` +
      (others.length ? `<ul class="ig-others">${list}</ul>` : "<p>Nothing else from this conversation.</p>") +
      (others.length > 40 ? "<p>Showing the first 40, oldest first.</p>" : "");
    panel().hidden = false;
    panel().scrollTop = 0;
  };

  document.addEventListener("click", e => {
    const link = e.target.closest(".ig-link");
    if (link) igShow(+link.dataset.i);
    else if (e.target.closest("#ig-close")) panel().hidden = true;
  });
  document.addEventListener("keydown", e => { if (e.key === "Escape") panel().hidden = true; });

  // Tooltips: a styled bubble on hover or keyboard focus, and on tap for touch screens.
  // [data-tip] wins; datamapplot's own controls get their text from TIPS by selector.
  const TIPS = [
    ["#search-container", "Search the quotes: points without your words fade out"],
    ["#colormap-selector-container, .color-map-dropdown, #colorMapOptions", "Colour the points by topic level, by coding session or chat, by app, or by kind of statement"],
    [".legend-item", "Click a coloured square to show only that group; click more squares to add groups, click again to remove"],
    ["#d3histogram-container, .d3histogram-container", "Points over time. Drag across the bars to show only that date range; click outside the selection to clear it"],
    [".expand-all-btn", "Open every topic to show its subtopics"],
    [".topic-tree-close-btn", "Fold the topic list away (click again to reopen)"],
    ["#topic-tree, .topic-tree", "Topics, broad to narrow. Click a topic to zoom the map to it"],
  ];
  const tip = () => document.getElementById("ig-tip");
  const textFor = el => {
    const own = el.closest("[data-tip]");
    if (own) return own.dataset.tip;
    for (const [sel, text] of TIPS) if (el.closest(sel)) return text;
    return null;
  };
  let shownFor = null, timer = null;
  const show = (el, text) => {
    const t = tip(), box = el.getBoundingClientRect();
    t.textContent = text; t.style.display = "block";
    const w = t.offsetWidth, h = t.offsetHeight;
    let x = Math.min(Math.max(8, box.left), window.innerWidth - w - 8), y = box.bottom + 6;
    if (y + h > window.innerHeight - 8) y = box.top - h - 6;
    t.style.left = x + "px"; t.style.top = y + "px";
  };
  const hide = () => { tip().style.display = "none"; shownFor = null; };
  const onEnter = e => {
    const text = e.target instanceof Element ? textFor(e.target) : null;
    if (!text) { if (shownFor) hide(); return; }
    const anchor = e.target.closest("[data-tip]") || TIPS.map(([s]) => e.target.closest(s)).find(Boolean);
    if (anchor === shownFor) return;
    clearTimeout(timer);
    timer = setTimeout(() => { shownFor = anchor; show(anchor, text); }, 150);
  };
  document.addEventListener("mouseover", onEnter);
  document.addEventListener("focusin", onEnter);
  document.addEventListener("focusout", hide);
  document.addEventListener("mouseout", e => { if (!e.relatedTarget || !(e.relatedTarget instanceof Element) || !textFor(e.relatedTarget)) { clearTimeout(timer); hide(); } });
  document.addEventListener("touchstart", e => {
    const text = e.target instanceof Element ? textFor(e.target) : null;
    if (!text) return;
    const anchor = e.target.closest("[data-tip]") || TIPS.map(([s]) => e.target.closest(s)).find(Boolean);
    show(anchor, text); clearTimeout(timer); timer = setTimeout(hide, 2500);
  }, { passive: true });

  // datamapplot names its topic-level colourings "<descriptor> Clusters", broadest first; the table mirrors
  // CLUSTER_LAYER_DESCRIPTORS in datamapplot/interactive_helpers.py. Say what each level is instead.
  const n = IG.layerSizes.length;
  const LEVELS = { 9: ["Top", "Upper", "Upper-mid", "Upper-central", "Mid", "Lower-central", "Lower-mid", "Lower", "Bottom"],
    8: ["Top", "Upper", "Upper-mid", "Upper-central", "Lower-central", "Lower-mid", "Lower", "Bottom"],
    7: ["Top", "Upper", "Upper-mid", "Mid", "Lower-mid", "Lower", "Bottom"], 6: ["Top", "Upper", "Upper-mid", "Lower-mid", "Lower", "Bottom"],
    5: ["Top", "Upper", "Mid", "Lower", "Bottom"], 4: ["Top", "Upper-mid", "Lower-mid", "Bottom"], 3: ["Upper", "Mid", "Lower"],
    2: ["Upper", "Lower"], 1: ["Primary"] }[n] || IG.layerSizes.map((_, i) => `Layer-${i}`);
  const level = i => i === 0 ? "broadest" : i === n - 1 ? "narrowest" : `level ${i + 1} of ${n}`;
  const RENAME = { "Clusters": "Topics (default colours)" };
  LEVELS.forEach((d, i) => { RENAME[d + " Clusters"] = `Topics: ${IG.layerSizes[i]}, ${level(i)}`; });
  const relabel = () => document.querySelectorAll(".color-map-text").forEach(el => { const t = RENAME[el.textContent.trim()]; if (t) el.textContent = t; });
  new MutationObserver(relabel).observe(document.body, { childList: true, subtree: true, characterData: true });
  relabel();
})();

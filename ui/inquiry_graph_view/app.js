import cytoscape from 'cytoscape'
import ELK from 'elkjs/lib/elk.bundled.js'
import data from './data.json'
document.getElementById('title').textContent = data.title
const legend = document.getElementById('legend')
for (const [k, c] of Object.entries(data.kinds)) legend.insertAdjacentHTML('beforeend', `<span class="chip" style="background:${c}"></span>${k} `)
const cy = cytoscape({
  container: document.getElementById('cy'), elements: data.elements, wheelSensitivity: 0.25,
  style: [
    { selector: 'node[!group]', style: { 'background-color': 'data(color)', label: 'data(label)', 'font-size': 11, 'text-wrap': 'wrap', 'text-max-width': 175, shape: 'round-rectangle', width: 190, height: 44, padding: 6, 'text-valign': 'center', 'text-halign': 'center', color: '#111', 'border-width': 1, 'border-color': '#555' } },
    { selector: 'node[?group]', style: { label: 'data(label)', 'background-color': '#f3f3f3', 'background-opacity': 0.7, 'border-width': 1, 'border-color': '#bbb', 'text-valign': 'top', 'text-halign': 'center', 'font-weight': 700, color: '#333', padding: 14, shape: 'round-rectangle' } },
    { selector: 'edge', style: { width: 1.5, 'line-color': '#777', 'target-arrow-color': '#777', 'target-arrow-shape': 'triangle', 'curve-style': 'bezier', label: 'data(label)', 'font-size': 9, 'text-background-color': '#fff', 'text-background-opacity': 0.9 } },
    { selector: ':selected', style: { 'border-width': 3, 'border-color': '#0b57d0', 'line-color': '#0b57d0', 'target-arrow-color': '#0b57d0' } },
  ],
})
// Pack the group boxes into a grid (rectpacking), and lay out the ideas inside each box (layered).
const elk = new ELK()
const leafs = data.elements.filter((e) => e.data.parent), groups = data.elements.filter((e) => e.data.group), rels = data.elements.filter((e) => e.data.source)
const byGroup = Object.fromEntries(groups.map((g) => [g.data.id, { id: g.data.id, layoutOptions: { 'elk.algorithm': 'layered', 'elk.direction': 'DOWN', 'elk.padding': '[top=30,left=12,bottom=12,right=12]', 'elk.spacing.nodeNode': 12, 'elk.layered.spacing.nodeNodeBetweenLayers': 26, 'elk.separateConnectedComponents': true, 'elk.aspectRatio': 1.2 }, children: [], edges: [] }]))
const groupOf = {}
for (const n of leafs) { byGroup[n.data.parent].children.push({ id: n.data.id, width: 190, height: 44 }); groupOf[n.data.id] = n.data.parent }
for (const r of rels) { const s = groupOf[r.data.source], t = groupOf[r.data.target]; if (s && s === t) byGroup[s].edges.push({ id: r.data.id, sources: [r.data.source], targets: [r.data.target] }) }
const root = { id: 'root', layoutOptions: { 'elk.algorithm': 'rectpacking', 'elk.aspectRatio': 1.6, 'elk.spacing.nodeNode': 24, 'elk.padding': '[top=20,left=20,bottom=20,right=20]' }, children: Object.values(byGroup) }
elk.layout(root).then((res) => {
  const pos = {}
  for (const g of res.children) for (const c of g.children || []) pos[c.id] = { x: g.x + c.x + c.width / 2, y: g.y + c.y + c.height / 2 }
  cy.nodes('[!group]').forEach((n) => n.position(pos[n.id()]))
  cy.layout({ name: 'preset', fit: true, padding: 30 }).run()
  window.__laidOut = true
})
const side = document.getElementById('side')
cy.on('tap', 'node[!group], edge', (e) => { const d = e.target.data(); side.innerHTML = `<b>${d.kind || d.label}</b><p>${(d.text || '').replace(/</g,'&lt;')}</p><blockquote>${(d.quote||'').replace(/</g,'&lt;')}</blockquote>` })

import { useRef, useState } from "react";
import { SAMPLE_WRITING } from "../api/mockData";
import "./paper.css";

/*
 * Freehand pen marking, like correcting a paper by hand.
 * strokes: [{ id, points:[{x,y}...], color, comment, cx, cy }]  (x/y are % of page)
 * Draw with mouse or finger; Undo removes the last stroke; Eraser removes a
 * clicked stroke; any stroke can carry an optional typed comment.
 */
export default function PaperViewer({ submission, onClose }) {
  const paperRef = useRef(null);
  const [strokes, setStrokes] = useState(submission?.strokes || []);
  const [tool, setTool] = useState("pen");          // 'pen' | 'erase' | 'off'
  const [color, setColor] = useState("#e12d39");
  const [cur, setCur] = useState(null);             // current stroke points
  const [commentFor, setCommentFor] = useState(null);
  const drawing = useRef(false);

  const pt = (e) => {
    const r = paperRef.current.getBoundingClientRect();
    const touch = e.touches?.[0];
    const cx = touch ? touch.clientX : e.clientX;
    const cy = touch ? touch.clientY : e.clientY;
    return { x: ((cx - r.left) / r.width) * 100, y: ((cy - r.top) / r.height) * 100 };
  };

  const start = (e) => {
    if (tool !== "pen") return;
    e.preventDefault();
    drawing.current = true;
    setCur([pt(e)]);
  };
  const moveP = (e) => {
    if (!drawing.current || tool !== "pen") return;
    e.preventDefault();
    setCur((c) => [...c, pt(e)]);
  };
  const end = () => {
    if (!drawing.current) return;
    drawing.current = false;
    setCur((c) => {
      if (c && c.length > 1) {
        const xs = c.map((p) => p.x), ys = c.map((p) => p.y);
        const cx = (Math.min(...xs) + Math.max(...xs)) / 2;
        const cy = Math.min(...ys);
        setStrokes((s) => [...s, { id: Date.now(), points: c, color, comment: "", cx, cy }]);
      }
      return null;
    });
  };

  const path = (points) => points.map((p, i) => `${i ? "L" : "M"}${p.x},${p.y}`).join(" ");

  // pen-shaped cursor tinted to the current pen colour (hotspot at the nib)
  const penCursor = () => {
    const svg =
      `<svg xmlns='http://www.w3.org/2000/svg' width='28' height='28' viewBox='0 0 28 28'>` +
      `<path d='M4 24 L7 21 L20 8 L23 11 L10 24 L4 24 Z' fill='${color}' stroke='white' stroke-width='1'/>` +
      `<path d='M4 24 L6.5 21.5 L5.5 22.5 Z' fill='#222222'/>` +
      `<path d='M19 7 L21 5 A1.4 1.4 0 0 1 23 7 L21 9 Z' fill='#f6a800' stroke='white' stroke-width='1'/>` +
      `</svg>`;
    return `url("data:image/svg+xml,${encodeURIComponent(svg)}") 4 24, crosshair`;
  };
  const undo = () => setStrokes((s) => s.slice(0, -1));
  const eraseStroke = (id) => setStrokes((s) => s.filter((k) => k.id !== id));
  const setComment = (id, v) => setStrokes((s) => s.map((k) => (k.id === id ? { ...k, comment: v } : k)));
  const withComments = strokes.filter((s) => s.comment);

  return (
    <div className="pv-back">
      <div className="pv">
        <header className="pv-top">
          <div><strong>{submission?.student || "Submission"}</strong><span className="muted"> · {submission?.file || "answer-script.pdf"}</span></div>
          <div className="spacer" />
          {/* pen toolbar */}
          <div className="pen-tools">
            <button className={tool === "pen" ? "on" : ""} title="Pen" onClick={() => setTool("pen")}>✒️</button>
            <button className={tool === "erase" ? "on" : ""} title="Eraser (click a stroke)" onClick={() => setTool(tool === "erase" ? "off" : "erase")}>🧽</button>
            <button title="Undo" onClick={undo}>↩️</button>
            <span className="pen-sep" />
            {["#e12d39", "#1769e0", "#1a9d5a"].map((c) => (
              <button key={c} className={`pen-color ${color === c ? "on" : ""}`} style={{ background: c }} onClick={() => { setColor(c); setTool("pen"); }} />
            ))}
          </div>
          <button className="btn sm outline" onClick={() => onClose(strokes)}>Close</button>
        </header>

        <div className="pv-body">
          <div className="pv-scroll">
            <div ref={paperRef}
              className={`paper ${tool === "pen" ? "pen" : ""} ${tool === "erase" ? "erase" : ""}`}
              style={tool === "pen" ? { cursor: penCursor() } : undefined}
              onMouseDown={start} onMouseMove={moveP} onMouseUp={end} onMouseLeave={end}
              onTouchStart={start} onTouchMove={moveP} onTouchEnd={end}>
              <h2 className="paper-title">{SAMPLE_WRITING.title}</h2>
              {SAMPLE_WRITING.paragraphs.map((p, i) => <p key={i} className="paper-line">{p}</p>)}

              {/* ink layer */}
              <svg className="ink" viewBox="0 0 100 100" preserveAspectRatio="none">
                {strokes.map((s) => (
                  <path key={s.id} d={path(s.points)} stroke={s.color} className={tool === "erase" ? "erasable" : ""}
                    onClick={() => tool === "erase" && eraseStroke(s.id)} />
                ))}
                {cur && cur.length > 1 && <path d={path(cur)} stroke={color} />}
              </svg>

              {/* comment tags anchored to strokes */}
              {strokes.map((s, i) => s.comment && (
                <div key={s.id} className="ink-note" style={{ left: `${s.cx}%`, top: `${s.cy}%` }}>
                  <b>{i + 1}.</b> {s.comment}
                </div>
              ))}
            </div>
          </div>

          {/* sidebar: list strokes, attach optional comments */}
          <aside className="pv-side">
            <h4>Marks ({strokes.length})</h4>
            <p className="muted" style={{ fontSize: 13 }}>
              {tool === "erase" ? "Click any ink stroke on the paper to erase it."
                : "Hold and draw on the paper to mark — circle, cross out, underline, tick. Add a comment below if you want."}
            </p>
            <div className="pv-marklist">
              {strokes.map((s, i) => (
                <div key={s.id} className="pv-markitem">
                  <div className="pv-markitem-top">
                    <span className="ink-num" style={{ background: s.color }}>{i + 1}</span>
                    <button className="pv-del" onClick={() => eraseStroke(s.id)}>🗑</button>
                  </div>
                  <textarea rows={2} placeholder="Optional comment…" value={s.comment} onChange={(e) => setComment(s.id, e.target.value)} />
                </div>
              ))}
              {strokes.length === 0 && <p className="muted">No marks yet.</p>}
            </div>
            <button className="btn navy block" style={{ marginTop: 14 }} onClick={() => onClose(strokes)}>Save Review</button>
            {withComments.length > 0 && <p className="muted" style={{ fontSize: 12, marginTop: 8 }}>{withComments.length} comment(s) attached</p>}
          </aside>
        </div>
      </div>
    </div>
  );
}

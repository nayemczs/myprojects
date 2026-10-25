import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";
import { useLang } from "../i18n/LanguageContext";
import { SCHOOL } from "../api/mockData";
import "./dashboard.css";

/* Shell: collapsible sidebar + topbar. `nav` = [{key,label,icon}] */
export function DashShell({ title, nav, active, onNav, children }) {
  const { user, logout } = useAuth();
  const { t } = useLang();
  const navigate = useNavigate();
  const [open, setOpen] = useState(false);

  return (
    <div className="dash">
      <aside className={`dash-side ${open ? "open" : ""}`}>
        <div className="dash-brand">
          <div className="brand-logo">{SCHOOL.short}</div>
          <strong>{SCHOOL.short} Portal</strong>
        </div>
        <nav className="dash-nav">
          {nav.map((n) => (
            <button key={n.key} className={active === n.key ? "on" : ""}
              onClick={() => { onNav(n.key); setOpen(false); }}>
              <span className="ic">{n.icon}</span>{n.label}
            </button>
          ))}
        </nav>
        <div className="dash-side-foot">
          <button onClick={() => navigate("/")}><span className="ic">🏠</span>{t("dash.mainSite")}</button>
          <button onClick={() => { logout(); navigate("/"); }}><span className="ic">🚪</span>{t("nav.logout")}</button>
        </div>
      </aside>

      <div className="dash-body">
        <header className="dash-top">
          <button className="menu-btn" onClick={() => setOpen(!open)}>☰</button>
          <h2>{title}</h2>
          <div className="spacer" />
          <div className="dash-user">
            <div className="avatar">{(user?.username || "U")[0].toUpperCase()}</div>
            <div><strong>{user?.username}</strong><span>{user?.role}</span></div>
          </div>
        </header>
        <main className="dash-main">{children}</main>
      </div>
      {open && <div className="dash-overlay" onClick={() => setOpen(false)} />}
    </div>
  );
}

export function StatCards({ items }) {
  return (
    <div className="stat-cards">
      {items.map((s) => (
        <div key={s.label} className="stat-card">
          <div className="stat-card-ic">{s.icon}</div>
          <div className="stat-card-body">
            <strong>{s.value}</strong>
            <span>{s.label}</span>
          </div>
          {s.delta && <span className="stat-delta">{s.delta}</span>}
        </div>
      ))}
    </div>
  );
}

/* Minimal dependency-free SVG line chart */
export function LineChart({ data, labels, height = 180, color = "#0a4a88" }) {
  const w = 520, h = height, pad = 28;
  const max = Math.max(...data) * 1.1, min = Math.min(...data) * 0.9;
  const x = (i) => pad + (i * (w - pad * 2)) / (data.length - 1);
  const y = (v) => h - pad - ((v - min) / (max - min || 1)) * (h - pad * 2);
  const line = data.map((v, i) => `${i ? "L" : "M"}${x(i)},${y(v)}`).join(" ");
  const area = `${line} L${x(data.length - 1)},${h - pad} L${x(0)},${h - pad} Z`;
  return (
    <svg viewBox={`0 0 ${w} ${h}`} className="chart" preserveAspectRatio="none">
      <defs>
        <linearGradient id="g1" x1="0" y1="0" x2="0" y2="1">
          <stop offset="0%" stopColor={color} stopOpacity=".28" />
          <stop offset="100%" stopColor={color} stopOpacity="0" />
        </linearGradient>
      </defs>
      <path d={area} fill="url(#g1)" />
      <path d={line} fill="none" stroke={color} strokeWidth="3" strokeLinejoin="round" strokeLinecap="round" />
      {data.map((v, i) => <circle key={i} cx={x(i)} cy={y(v)} r="3.5" fill="#fff" stroke={color} strokeWidth="2" />)}
      {labels && labels.map((l, i) => (
        <text key={i} x={x(i)} y={h - 8} fontSize="10" fill="#94a0b4" textAnchor="middle">{l}</text>
      ))}
    </svg>
  );
}

export function BarChart({ data, labels, height = 180, color = "#f6a800" }) {
  const w = 520, h = height, pad = 28;
  const max = Math.max(...data) * 1.15;
  const bw = (w - pad * 2) / data.length * 0.55;
  const gap = (w - pad * 2) / data.length;
  return (
    <svg viewBox={`0 0 ${w} ${h}`} className="chart" preserveAspectRatio="none">
      {data.map((v, i) => {
        const bh = (v / max) * (h - pad * 2);
        const bx = pad + i * gap + (gap - bw) / 2;
        return (
          <g key={i}>
            <rect x={bx} y={h - pad - bh} width={bw} height={bh} rx="5" fill={color} />
            <text x={bx + bw / 2} y={h - pad - bh - 6} fontSize="10" fill="#667085" textAnchor="middle">{v}</text>
            {labels && <text x={bx + bw / 2} y={h - 8} fontSize="10" fill="#94a0b4" textAnchor="middle">{labels[i]}</text>}
          </g>
        );
      })}
    </svg>
  );
}

export function DonutChart({ data, size = 170 }) {
  const total = data.reduce((s, d) => s + d.value, 0);
  const r = size / 2 - 14, cx = size / 2, cy = size / 2, C = 2 * Math.PI * r;
  let offset = 0;
  return (
    <div className="donut-wrap">
      <svg width={size} height={size} viewBox={`0 0 ${size} ${size}`}>
        <circle cx={cx} cy={cy} r={r} fill="none" stroke="#eef2f8" strokeWidth="18" />
        {data.map((d, i) => {
          const len = (d.value / total) * C;
          const el = (
            <circle key={i} cx={cx} cy={cy} r={r} fill="none" stroke={d.color} strokeWidth="18"
              strokeDasharray={`${len} ${C - len}`} strokeDashoffset={-offset}
              transform={`rotate(-90 ${cx} ${cy})`} strokeLinecap="round" />
          );
          offset += len;
          return el;
        })}
        <text x={cx} y={cy - 2} fontSize="22" fontWeight="800" fill="#002b5c" textAnchor="middle">{total}%</text>
        <text x={cx} y={cy + 16} fontSize="10" fill="#667085" textAnchor="middle">distribution</text>
      </svg>
      <div className="donut-legend">
        {data.map((d) => (
          <div key={d.label}><span style={{ background: d.color }} />{d.label} · {d.value}%</div>
        ))}
      </div>
    </div>
  );
}

export function Panel({ title, action, children }) {
  return (
    <div className="panel">
      <div className="panel-top">
        <h3>{title}</h3>
        {action}
      </div>
      {children}
    </div>
  );
}

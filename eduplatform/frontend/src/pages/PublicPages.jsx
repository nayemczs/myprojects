import { useEffect, useState } from "react";
import { useParams, Link } from "react-router-dom";
import api from "../api/client";
import {
  SCHOOL, HERO_SLIDES, STATS, NOTICES, LEADERS, ALUMNI, EVENTS, FACULTIES, FACILITIES, withFallback,
} from "../api/mockData";
import Avatar from "../components/Avatar";
import { useLang } from "../i18n/LanguageContext";
import "./public.css";

/* ---------------- Home ---------------- */
export function Home() {
  const { t } = useLang();
  const [slide, setSlide] = useState(0);
  const [notices, setNotices] = useState(NOTICES);
  const [events, setEvents] = useState(EVENTS);
  const [faculties, setFaculties] = useState(FACULTIES);

  useEffect(() => {
    withFallback(api.get("/posts/?kind=NOTICE"), NOTICES).then(setNotices);
    withFallback(api.get("/posts/?kind=EVENT"), EVENTS).then(setEvents);
    withFallback(api.get("/faculties/"), FACULTIES).then(setFaculties);
  }, []);

  useEffect(() => {
    const t = setInterval(() => setSlide((s) => (s + 1) % HERO_SLIDES.length), 5000);
    return () => clearInterval(t);
  }, []);

  return (
    <div>
      {/* Hero slider */}
      <section className="hero">
        {HERO_SLIDES.map((s, i) => (
          <div key={i} className={`hero-slide ${i === slide ? "on" : ""}`}
            style={{ backgroundImage: `linear-gradient(rgba(0,22,50,.72),rgba(0,22,50,.72)), url(${s.img})` }}>
            <div className="container hero-content">
              <span className="chip gold">{t("home.admissionsOpen")}</span>
              <h1>{s.title}</h1>
              <p>{s.subtitle}</p>
              <div className="row wrap">
                <Link to="/admission"><button className="btn">{t("common.applyNow")}</button></Link>
                <Link to="/about"><button className="btn ghost">{t("common.learnMore")}</button></Link>
              </div>
            </div>
          </div>
        ))}
        <div className="hero-dots">
          {HERO_SLIDES.map((_, i) => (
            <button key={i} className={i === slide ? "on" : ""} onClick={() => setSlide(i)} />
          ))}
        </div>
      </section>

      {/* Stats bar */}
      <section className="stats-band">
        <div className="container stats-grid">
          {STATS.map((s) => (
            <div key={s.label} className="stat-item">
              <div className="stat-ic">{s.icon}</div>
              <div><strong>{s.value}</strong><span>{s.label}</span></div>
            </div>
          ))}
        </div>
      </section>

      {/* Notices + Welcome */}
      <section className="section">
        <div className="container two-col">
          <div>
            <div className="panel-head"><span className="chip">{t("home.noticeBoard")}</span><Link to="/events" className="see-all">{t("common.viewAll")} →</Link></div>
            <div className="notice-list">
              {notices.slice(0, 5).map((n) => (
                <div key={n.id} className="notice-row">
                  <div className="notice-date">
                    <strong>{new Date(n.created_at).getDate()}</strong>
                    <span>{new Date(n.created_at).toLocaleString("en", { month: "short" })}</span>
                  </div>
                  <div>
                    <h4>{n.title}</h4>
                    <p className="muted">{(n.body || "").slice(0, 110)}…</p>
                  </div>
                </div>
              ))}
            </div>
          </div>
          <div className="welcome-card card">
            <span className="chip soft">{t("home.welcomeChip")} {SCHOOL.short}</span>
            <h2>{t("home.legacy")} {SCHOOL.established}</h2>
            <p className="muted">
              {SCHOOL.name} {t("home.welcomeBody")}
            </p>
            <Link to="/about"><button className="btn navy">{t("home.readStory")}</button></Link>
          </div>
        </div>
      </section>

      {/* Faculties */}
      <section className="section section-alt">
        <div className="container">
          <div className="sec-head">
            <div className="kicker">{t("home.academics")}</div>
            <h2>{t("home.ourFaculties")}</h2>
            <div className="bar" />
          </div>
          <div className="fac-grid">
            {faculties.map((f) => (
              <Link to={`/faculties/${f.slug}`} key={f.id} className="fac-card card">
                <div className="fac-ic">{f.icon || "🎓"}</div>
                <h3>{f.name}</h3>
                <p className="muted">{f.short_desc}</p>
                <span className="fac-link">{t("common.explore")} →</span>
              </Link>
            ))}
          </div>
        </div>
      </section>

      {/* Leadership */}
      <section className="section">
        <div className="container">
          <div className="sec-head">
            <div className="kicker">{t("home.leadership")}</div>
            <h2>{t("home.leaderMessages")}</h2>
            <div className="bar" />
          </div>
          <div className="leader-grid">
            {LEADERS.map((l) => (
              <div key={l.role} className="leader-card card">
                <Avatar name={l.name} image={l.photo} size={96} style={{ margin: "0 auto 12px", border: "4px solid #eef2fb" }} />
                <span className="chip gold">{l.role}</span>
                <h3>{l.name}</h3>
                <p className="muted">“{l.msg}”</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Alumni */}
      <section className="section section-alt">
        <div className="container">
          <div className="sec-head">
            <div className="kicker">{t("home.ourPride")}</div>
            <h2>{t("home.starAlumni")}</h2>
            <div className="bar" />
          </div>
          <div className="alumni-grid">
            {ALUMNI.map((a) => (
              <div key={a.name} className="alumni-card card">
                <Avatar name={a.name} image={a.photo} size={80} style={{ margin: "0 auto 10px" }} />
                <h4>{a.name}</h4>
                <p className="chip soft">{a.admitted}</p>
                <span className="muted">{t("home.batch")} {a.year}</span>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Events */}
      <section className="section">
        <div className="container">
          <div className="sec-head">
            <div className="kicker">{t("home.campusLife")}</div>
            <h2>{t("home.latestNews")}</h2>
            <div className="bar" />
          </div>
          <div className="event-grid">
            {events.slice(0, 3).map((e) => (
              <div key={e.id} className="event-card card">
                {e.img && <div className="event-img" style={{ backgroundImage: `url(${e.img})` }}><span className="chip gold">{e.category || "Event"}</span></div>}
                <div className="event-body">
                  {e.event_date && <span className="muted event-date">📅 {new Date(e.event_date).toLocaleDateString()}</span>}
                  <h3>{e.title}</h3>
                  <p className="muted">{(e.body || "").slice(0, 90)}…</p>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* CTA */}
      <section className="cta-band">
        <div className="container cta-in">
          <div>
            <h2>{t("home.ctaTitle")}</h2>
            <p>{t("home.ctaBody")} {SCHOOL.name}.</p>
          </div>
          <Link to="/admission"><button className="btn">{t("home.applyAdmission")}</button></Link>
        </div>
      </section>
    </div>
  );
}

/* ---------------- Faculties ---------------- */
export function Faculties() {
  const { t } = useLang();
  const [faculties, setFaculties] = useState(FACULTIES);
  useEffect(() => { withFallback(api.get("/faculties/"), FACULTIES).then(setFaculties); }, []);
  return (
    <PageShell title={t("home.ourFaculties")} crumb={t("home.academics")}>
      <div className="container section">
        <div className="fac-grid">
          {faculties.map((f) => (
            <Link to={`/faculties/${f.slug}`} key={f.id} className="fac-card card">
              <div className="fac-ic">{f.icon || "🎓"}</div>
              <h3>{f.name}</h3>
              <p className="muted">{f.short_desc}</p>
              {f.head_name && <span className="muted">{t("fac.head")}: {f.head_name}</span>}
              <span className="fac-link">{t("common.explore")} →</span>
            </Link>
          ))}
        </div>
      </div>
    </PageShell>
  );
}

export function FacultyDetail() {
  const { t } = useLang();
  const { slug } = useParams();
  const [f, setF] = useState(null);
  useEffect(() => {
    const fallback = FACULTIES.find((x) => x.slug === slug) || FACULTIES[0];
    withFallback(api.get(`/faculties/${slug}/`), fallback).then(setF);
  }, [slug]);
  if (!f) return <PageShell title="…" crumb={t("home.academics")}><div className="container section" /></PageShell>;
  return (
    <PageShell title={f.name} crumb={t("nav.faculties")}>
      <div className="container section">
        <div className="two-col">
          <div className="card">
            <div className="fac-ic big">{f.icon || "🎓"}</div>
            <h2>{f.name}</h2>
            {f.head_name && <p className="chip soft">{t("fac.head")}: {f.head_name}</p>}
            <p className="muted">{f.description || f.short_desc}</p>
          </div>
          <div className="card">
            <h3>{t("fac.whatWeOffer")}</h3>
            <ul className="tick-list">
              <li>{t("fac.offer1")}</li>
              <li>{t("fac.offer2")}</li>
              <li>{t("fac.offer3")}</li>
              <li>{t("fac.offer4")}</li>
            </ul>
            <Link to="/admission"><button className="btn navy block">{t("fac.applyTo")}</button></Link>
          </div>
        </div>
      </div>
    </PageShell>
  );
}

/* ---------------- Events ---------------- */
export function Events() {
  const { t } = useLang();
  const [events, setEvents] = useState(EVENTS);
  const [notices, setNotices] = useState(NOTICES);
  useEffect(() => {
    withFallback(api.get("/posts/?kind=EVENT"), EVENTS).then(setEvents);
    withFallback(api.get("/posts/?kind=NOTICE"), NOTICES).then(setNotices);
  }, []);
  return (
    <PageShell title={t("home.latestNews")} crumb={t("home.campusLife")}>
      <div className="container section">
        <div className="event-grid">
          {events.map((e) => (
            <div key={e.id} className="event-card card">
              {e.img && <div className="event-img" style={{ backgroundImage: `url(${e.img})` }}><span className="chip gold">{e.category || "Event"}</span></div>}
              <div className="event-body">
                {e.event_date && <span className="muted event-date">📅 {new Date(e.event_date).toLocaleString()}</span>}
                <h3>{e.title}</h3>
                <p className="muted">{e.body}</p>
              </div>
            </div>
          ))}
        </div>
        <div className="sec-head" style={{ marginTop: 50 }}><h2>{t("home.noticeBoard")}</h2><div className="bar" /></div>
        <div className="notice-list">
          {notices.map((n) => (
            <div key={n.id} className="notice-row card" style={{ marginBottom: 10 }}>
              <div className="notice-date">
                <strong>{new Date(n.created_at).getDate()}</strong>
                <span>{new Date(n.created_at).toLocaleString("en", { month: "short" })}</span>
              </div>
              <div><h4>{n.title}</h4><p className="muted">{n.body}</p></div>
            </div>
          ))}
        </div>
      </div>
    </PageShell>
  );
}

/* ---------------- About ---------------- */
export function About() {
  const { t } = useLang();
  return (
    <PageShell title={t("about.title")} crumb={t("home.welcomeChip")}>
      <div className="container section">
        <div className="two-col">
          <div>
            <span className="chip soft">{t("about.ourStory")}</span>
            <h2>{t("about.heading")}</h2>
            <p className="muted">
              {SCHOOL.name} ({SCHOOL.established}) {t("about.body1")}
            </p>
            <p className="muted">
              “{SCHOOL.tagline}” ({SCHOOL.taglineEn}).
            </p>
          </div>
          <img className="about-img" src="https://images.unsplash.com/photo-1541339907198-e08756dedf3f?auto=format&fit=crop&w=900&q=70" alt="campus" />
        </div>
        <div className="value-grid">
          {[
            { ic: "🎯", t: t("about.mission"), d: t("about.missionBody") },
            { ic: "👁️", t: t("about.vision"), d: t("about.visionBody") },
            { ic: "💎", t: t("about.values"), d: t("about.valuesBody") },
          ].map((v) => (
            <div key={v.t} className="card value-card">
              <div className="fac-ic">{v.ic}</div>
              <h3>{v.t}</h3>
              <p className="muted">{v.d}</p>
            </div>
          ))}
        </div>
        <div className="sec-head" style={{ marginTop: 56 }}><div className="kicker">{t("home.leadership")}</div><h2>{t("about.ourLeaders")}</h2><div className="bar" /></div>
        <div className="leader-grid">
          {LEADERS.map((l) => (
            <div key={l.role} className="leader-card card">
              <Avatar name={l.name} image={l.photo} size={96} style={{ margin: "0 auto 12px", border: "4px solid #eef2fb" }} />
              <span className="chip gold">{l.role}</span>
              <h3>{l.name}</h3>
              <p className="muted">“{l.msg}”</p>
            </div>
          ))}
        </div>

        <div className="sec-head" style={{ marginTop: 56 }}><div className="kicker">{t("about.facilitiesKicker")}</div><h2>{t("about.ourFacilities")}</h2><div className="bar" /></div>
        <div className="fac-grid">
          {FACILITIES.map((f) => (
            <div key={f.name} className="fac-card card">
              <div className="fac-ic">{f.icon}</div>
              <h3>{f.name}</h3>
              <p className="muted">{f.desc}</p>
            </div>
          ))}
        </div>
      </div>
    </PageShell>
  );
}

/* ---------------- Admission ---------------- */
export function Admission() {
  const { t } = useLang();
  const steps = [
    { n: 1, t: t("adm.step1t"), d: t("adm.step1d") },
    { n: 2, t: t("adm.step2t"), d: t("adm.step2d") },
    { n: 3, t: t("adm.step3t"), d: t("adm.step3d") },
    { n: 4, t: t("adm.step4t"), d: t("adm.step4d") },
  ];
  return (
    <PageShell title={t("nav.admission")} crumb={t("home.welcomeChip")}>
      <div className="container section">
        <div className="sec-head"><div className="kicker">{t("adm.howToApply")}</div><h2>{t("adm.process")}</h2><div className="bar" /></div>
        <div className="steps-grid">
          {steps.map((s) => (
            <div key={s.n} className="step-card card">
              <div className="step-n">{s.n}</div>
              <h3>{s.t}</h3>
              <p className="muted">{s.d}</p>
            </div>
          ))}
        </div>
        <div className="card admission-cta">
          <div>
            <h2>{t("adm.openTitle")}</h2>
            <p className="muted">{t("adm.openBody")}</p>
          </div>
          <Link to="/register"><button className="btn navy">{t("adm.registerNow")}</button></Link>
        </div>
      </div>
    </PageShell>
  );
}

/* ---------------- Contact ---------------- */
export function Contact() {
  const { t } = useLang();
  const [sent, setSent] = useState(false);
  return (
    <PageShell title={t("contact.title")} crumb={t("contact.getInTouch")}>
      <div className="container section">
        <div className="two-col">
          <div className="card">
            <h3>{t("contact.sendMessage")}</h3>
            {sent ? (
              <p className="chip approved" style={{ display: "inline-block" }}>{t("contact.thanks")}</p>
            ) : (
              <>
                <label>{t("contact.name")}</label><input />
                <label>{t("contact.email")}</label><input />
                <label>{t("contact.message")}</label><textarea rows={4} />
                <br /><br />
                <button className="btn navy" onClick={() => setSent(true)}>{t("contact.sendMessage")}</button>
              </>
            )}
          </div>
          <div className="card contact-info">
            <h3>{t("contact.reachUs")}</h3>
            <p><strong>📍 {t("contact.address")}</strong><br /><span className="muted">{SCHOOL.address}</span></p>
            <p><strong>📞 {t("contact.phone")}</strong><br /><span className="muted">{SCHOOL.phone}</span></p>
            <p><strong>✉️ {t("contact.email")}</strong><br /><span className="muted">{SCHOOL.email}</span></p>
            <p><strong>🕐 {t("contact.hours")}</strong><br /><span className="muted">{t("contact.hoursVal")}</span></p>
          </div>
        </div>
      </div>
    </PageShell>
  );
}

/* ---------------- Shared page shell (banner + breadcrumb) ---------------- */
function PageShell({ title, crumb, children }) {
  const { t } = useLang();
  return (
    <div>
      <div className="page-banner">
        <div className="container">
          <h1>{title}</h1>
          <div className="crumb"><Link to="/">{t("nav.home")}</Link> <span>›</span> {crumb}</div>
        </div>
      </div>
      {children}
    </div>
  );
}

import { useEffect, useState } from "react";
import { useParams, Link } from "react-router-dom";
import api from "../api/client";
import {
  SCHOOL, HERO_SLIDES, STATS, NOTICES, LEADERS, ALUMNI, EVENTS, FACULTIES, FACILITIES, withFallback,
} from "../api/mockData";
import "./public.css";

/* ---------------- Home ---------------- */
export function Home() {
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
              <span className="chip gold">Admissions Open 2026</span>
              <h1>{s.title}</h1>
              <p>{s.subtitle}</p>
              <div className="row wrap">
                <Link to="/admission"><button className="btn">Apply Now</button></Link>
                <Link to="/about"><button className="btn ghost">Learn More</button></Link>
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
            <div className="panel-head"><span className="chip">Notice Board</span><Link to="/events" className="see-all">View all →</Link></div>
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
            <span className="chip soft">Welcome to {SCHOOL.short}</span>
            <h2>A Legacy of Excellence Since {SCHOOL.established}</h2>
            <p className="muted">
              {SCHOOL.name} is committed to nurturing well-rounded individuals through
              quality education, modern facilities and a values-driven environment. Our
              students consistently achieve outstanding results and go on to the nation's
              top universities.
            </p>
            <Link to="/about"><button className="btn navy">Read Our Story</button></Link>
          </div>
        </div>
      </section>

      {/* Faculties */}
      <section className="section section-alt">
        <div className="container">
          <div className="sec-head">
            <div className="kicker">Academics</div>
            <h2>Our Faculties</h2>
            <div className="bar" />
          </div>
          <div className="fac-grid">
            {faculties.map((f) => (
              <Link to={`/faculties/${f.slug}`} key={f.id} className="fac-card card">
                <div className="fac-ic">{f.icon || "🎓"}</div>
                <h3>{f.name}</h3>
                <p className="muted">{f.short_desc}</p>
                <span className="fac-link">Explore →</span>
              </Link>
            ))}
          </div>
        </div>
      </section>

      {/* Leadership */}
      <section className="section">
        <div className="container">
          <div className="sec-head">
            <div className="kicker">Leadership</div>
            <h2>Messages from Our Leaders</h2>
            <div className="bar" />
          </div>
          <div className="leader-grid">
            {LEADERS.map((l) => (
              <div key={l.role} className="leader-card card">
                <img src={l.photo} alt={l.name} className="leader-img" />
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
            <div className="kicker">Our Pride</div>
            <h2>Star Alumni</h2>
            <div className="bar" />
          </div>
          <div className="alumni-grid">
            {ALUMNI.map((a) => (
              <div key={a.name} className="alumni-card card">
                <img src={a.photo} alt={a.name} />
                <h4>{a.name}</h4>
                <p className="chip soft">{a.admitted}</p>
                <span className="muted">Batch {a.year}</span>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Events */}
      <section className="section">
        <div className="container">
          <div className="sec-head">
            <div className="kicker">Campus Life</div>
            <h2>Latest News & Events</h2>
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
            <h2>Ready to Begin Your Journey?</h2>
            <p>Admissions for 2026 are now open. Secure your place at {SCHOOL.name}.</p>
          </div>
          <Link to="/admission"><button className="btn">Apply for Admission</button></Link>
        </div>
      </section>
    </div>
  );
}

/* ---------------- Faculties ---------------- */
export function Faculties() {
  const [faculties, setFaculties] = useState(FACULTIES);
  useEffect(() => { withFallback(api.get("/faculties/"), FACULTIES).then(setFaculties); }, []);
  return (
    <PageShell title="Our Faculties" crumb="Academics">
      <div className="container section">
        <div className="fac-grid">
          {faculties.map((f) => (
            <Link to={`/faculties/${f.slug}`} key={f.id} className="fac-card card">
              <div className="fac-ic">{f.icon || "🎓"}</div>
              <h3>{f.name}</h3>
              <p className="muted">{f.short_desc}</p>
              {f.head_name && <span className="muted">Head: {f.head_name}</span>}
              <span className="fac-link">Explore →</span>
            </Link>
          ))}
        </div>
      </div>
    </PageShell>
  );
}

export function FacultyDetail() {
  const { slug } = useParams();
  const [f, setF] = useState(null);
  useEffect(() => {
    const fallback = FACULTIES.find((x) => x.slug === slug) || FACULTIES[0];
    withFallback(api.get(`/faculties/${slug}/`), fallback).then(setF);
  }, [slug]);
  if (!f) return <PageShell title="Loading…" crumb="Academics"><div className="container section" /></PageShell>;
  return (
    <PageShell title={f.name} crumb="Faculties">
      <div className="container section">
        <div className="two-col">
          <div className="card">
            <div className="fac-ic big">{f.icon || "🎓"}</div>
            <h2>{f.name}</h2>
            {f.head_name && <p className="chip soft">Head: {f.head_name}</p>}
            <p className="muted">{f.description || f.short_desc}</p>
          </div>
          <div className="card">
            <h3>What We Offer</h3>
            <ul className="tick-list">
              <li>Experienced, qualified faculty members</li>
              <li>Modern laboratories and learning resources</li>
              <li>Regular assessments and personalized feedback</li>
              <li>Co-curricular clubs and competitions</li>
            </ul>
            <Link to="/admission"><button className="btn navy block">Apply to this Faculty</button></Link>
          </div>
        </div>
      </div>
    </PageShell>
  );
}

/* ---------------- Events ---------------- */
export function Events() {
  const [events, setEvents] = useState(EVENTS);
  const [notices, setNotices] = useState(NOTICES);
  useEffect(() => {
    withFallback(api.get("/posts/?kind=EVENT"), EVENTS).then(setEvents);
    withFallback(api.get("/posts/?kind=NOTICE"), NOTICES).then(setNotices);
  }, []);
  return (
    <PageShell title="News & Events" crumb="Campus Life">
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
        <div className="sec-head" style={{ marginTop: 50 }}><h2>All Notices</h2><div className="bar" /></div>
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
  return (
    <PageShell title="About Us" crumb="Our Institution">
      <div className="container section">
        <div className="two-col">
          <div>
            <span className="chip soft">Our Story</span>
            <h2>Shaping Minds, Building Futures</h2>
            <p className="muted">
              Founded in {SCHOOL.established}, {SCHOOL.name} has grown into one of the
              region's most respected institutions. We combine a rigorous academic
              curriculum with strong moral values, producing graduates who excel
              nationally and internationally.
            </p>
            <p className="muted">
              Our guiding spirit is “{SCHOOL.tagline}” ({SCHOOL.taglineEn}). Every classroom,
              laboratory and playing field is designed to help students discover and
              reach their full potential.
            </p>
          </div>
          <img className="about-img" src="https://images.unsplash.com/photo-1541339907198-e08756dedf3f?auto=format&fit=crop&w=900&q=70" alt="campus" />
        </div>
        <div className="value-grid">
          {[
            { ic: "🎯", t: "Our Mission", d: "To deliver world-class education that empowers every student." },
            { ic: "👁️", t: "Our Vision", d: "To be the leading center of academic and moral excellence." },
            { ic: "💎", t: "Our Values", d: "Integrity, discipline, curiosity and compassion." },
          ].map((v) => (
            <div key={v.t} className="card value-card">
              <div className="fac-ic">{v.ic}</div>
              <h3>{v.t}</h3>
              <p className="muted">{v.d}</p>
            </div>
          ))}
        </div>
        <div className="sec-head" style={{ marginTop: 56 }}><div className="kicker">Leadership</div><h2>Our Leaders</h2><div className="bar" /></div>
        <div className="leader-grid">
          {LEADERS.map((l) => (
            <div key={l.role} className="leader-card card">
              <img src={l.photo} alt={l.name} className="leader-img" />
              <span className="chip gold">{l.role}</span>
              <h3>{l.name}</h3>
              <p className="muted">“{l.msg}”</p>
            </div>
          ))}
        </div>

        <div className="sec-head" style={{ marginTop: 56 }}><div className="kicker">Campus</div><h2>Our Facilities</h2><div className="bar" /></div>
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
  const steps = [
    { n: 1, t: "Register Online", d: "Create a student account on our portal." },
    { n: 2, t: "Submit Documents", d: "Upload academic records and required papers." },
    { n: 3, t: "Admission Test", d: "Appear for the entrance assessment / interview." },
    { n: 4, t: "Enroll", d: "Complete payment and join your class." },
  ];
  return (
    <PageShell title="Admission" crumb="Join Us">
      <div className="container section">
        <div className="sec-head"><div className="kicker">How to Apply</div><h2>Admission Process</h2><div className="bar" /></div>
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
            <h2>Admissions Open for 2026</h2>
            <p className="muted">Begin your application today and take the first step toward a brighter future.</p>
          </div>
          <Link to="/register"><button className="btn navy">Register Now</button></Link>
        </div>
      </div>
    </PageShell>
  );
}

/* ---------------- Contact ---------------- */
export function Contact() {
  const [sent, setSent] = useState(false);
  return (
    <PageShell title="Contact Us" crumb="Get in Touch">
      <div className="container section">
        <div className="two-col">
          <div className="card">
            <h3>Send Us a Message</h3>
            {sent ? (
              <p className="chip approved" style={{ display: "inline-block" }}>Thanks! We'll get back to you soon.</p>
            ) : (
              <>
                <label>Name</label><input placeholder="Your name" />
                <label>Email</label><input placeholder="you@example.com" />
                <label>Message</label><textarea rows={4} placeholder="How can we help?" />
                <br /><br />
                <button className="btn navy" onClick={() => setSent(true)}>Send Message</button>
              </>
            )}
          </div>
          <div className="card contact-info">
            <h3>Reach Us</h3>
            <p><strong>📍 Address</strong><br /><span className="muted">{SCHOOL.address}</span></p>
            <p><strong>📞 Phone</strong><br /><span className="muted">{SCHOOL.phone}</span></p>
            <p><strong>✉️ Email</strong><br /><span className="muted">{SCHOOL.email}</span></p>
            <p><strong>🕐 Office Hours</strong><br /><span className="muted">Sun–Thu, 8:00 AM – 4:00 PM</span></p>
          </div>
        </div>
      </div>
    </PageShell>
  );
}

/* ---------------- Shared page shell (banner + breadcrumb) ---------------- */
function PageShell({ title, crumb, children }) {
  return (
    <div>
      <div className="page-banner">
        <div className="container">
          <h1>{title}</h1>
          <div className="crumb"><Link to="/">Home</Link> <span>›</span> {crumb}</div>
        </div>
      </div>
      {children}
    </div>
  );
}

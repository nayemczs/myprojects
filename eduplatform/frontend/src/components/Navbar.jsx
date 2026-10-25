import { useState } from "react";
import { Link, useNavigate, useLocation } from "react-router-dom";
import { useAuth } from "../context/AuthContext";
import { useLang } from "../i18n/LanguageContext";
import { SCHOOL } from "../api/mockData";
import "./navbar.css";

const PORTAL_PATH = {
  PRINCIPAL: "/admin-portal", ADMIN: "/admin-portal",
  TEACHER: "/teacher-portal", STUDENT: "/student-portal",
};

const NAV = [
  { to: "/", key: "nav.home" },
  { to: "/about", key: "nav.about" },
  { to: "/faculties", key: "nav.faculties" },
  { to: "/events", key: "nav.events" },
  { to: "/admission", key: "nav.admission" },
  { to: "/contact", key: "nav.contact" },
];

export default function Navbar() {
  const { user, logout } = useAuth();
  const { t } = useLang();
  const navigate = useNavigate();
  const { pathname } = useLocation();
  const [open, setOpen] = useState(false);

  return (
    <header className="nsa-header">
      <div className="topbar">
        <div className="container topbar-in">
          <span>📞 {SCHOOL.phone}</span>
          <span>✉️ {SCHOOL.email}</span>
          <span className="spacer" />
          <span>Established {SCHOOL.established} · EIIN {SCHOOL.eiin}</span>
        </div>
      </div>

      <nav className="mainnav">
        <div className="container mainnav-in">
          <Link to="/" className="brand" onClick={() => setOpen(false)}>
            <div className="brand-logo">{SCHOOL.short}</div>
            <div className="brand-text">
              <strong>{SCHOOL.name}</strong>
              <small>{SCHOOL.tagline}</small>
            </div>
          </Link>

          <button className="hamburger" onClick={() => setOpen(!open)} aria-label="menu">
            <span /><span /><span />
          </button>

          <div className={`links ${open ? "show" : ""}`}>
            {NAV.map((n) => (
              <Link key={n.to} to={n.to}
                className={pathname === n.to ? "active" : ""}
                onClick={() => setOpen(false)}>
                {t(n.key)}
              </Link>
            ))}
            {user ? (
              <>
                <Link to={PORTAL_PATH[user.role]} className="cta" onClick={() => setOpen(false)}>
                  {t("nav.myPortal")}
                </Link>
                <button className="link-btn" onClick={() => { logout(); navigate("/"); setOpen(false); }}>
                  {t("nav.logout")}
                </button>
              </>
            ) : (
              <>
                <Link to="/register" onClick={() => setOpen(false)}>{t("nav.register")}</Link>
                <Link to="/login" className="cta" onClick={() => setOpen(false)}>{t("nav.login")}</Link>
              </>
            )}
          </div>
        </div>
      </nav>
    </header>
  );
}

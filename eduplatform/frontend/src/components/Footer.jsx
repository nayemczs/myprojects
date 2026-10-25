import { Link } from "react-router-dom";
import { useLang } from "../i18n/LanguageContext";
import { SCHOOL } from "../api/mockData";
import "./footer.css";

export default function Footer() {
  const { t } = useLang();
  return (
    <footer className="nsa-footer">
      <div className="container foot-grid">
        <div>
          <div className="foot-brand">
            <div className="brand-logo">{SCHOOL.short}</div>
            <strong>{SCHOOL.name}</strong>
          </div>
          <p className="muted-light">{SCHOOL.tagline}. A center of academic excellence since {SCHOOL.established}.</p>
          <div className="socials">
            <a href="#" aria-label="facebook">f</a>
            <a href="#" aria-label="youtube">▶</a>
            <a href="#" aria-label="linkedin">in</a>
          </div>
        </div>
        <div>
          <h4>{t("foot.quickLinks")}</h4>
          <Link to="/about">{t("nav.about")}</Link>
          <Link to="/faculties">{t("nav.faculties")}</Link>
          <Link to="/admission">{t("nav.admission")}</Link>
          <Link to="/events">{t("nav.events")}</Link>
        </div>
        <div>
          <h4>{t("foot.portals")}</h4>
          <Link to="/login">{t("foot.studentPortal")}</Link>
          <Link to="/login">{t("foot.teacherPortal")}</Link>
          <Link to="/login">{t("foot.adminPortal")}</Link>
          <Link to="/register">{t("nav.register")}</Link>
        </div>
        <div>
          <h4>{t("nav.contact")}</h4>
          <p className="muted-light">{SCHOOL.address}</p>
          <p className="muted-light">📞 {SCHOOL.phone}</p>
          <p className="muted-light">✉️ {SCHOOL.email}</p>
        </div>
      </div>
      <div className="foot-bottom">
        <div className="container">
          © {new Date().getFullYear()} {SCHOOL.name}. {t("foot.rights")}
        </div>
      </div>
    </footer>
  );
}

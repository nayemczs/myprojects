import { Link } from "react-router-dom";
import { SCHOOL } from "../api/mockData";
import "./footer.css";

export default function Footer() {
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
          <h4>Quick Links</h4>
          <Link to="/about">About Us</Link>
          <Link to="/faculties">Faculties</Link>
          <Link to="/admission">Admission</Link>
          <Link to="/events">Events</Link>
        </div>
        <div>
          <h4>Portals</h4>
          <Link to="/login">Student Portal</Link>
          <Link to="/login">Teacher Portal</Link>
          <Link to="/login">Admin Portal</Link>
          <Link to="/register">Register</Link>
        </div>
        <div>
          <h4>Contact</h4>
          <p className="muted-light">{SCHOOL.address}</p>
          <p className="muted-light">📞 {SCHOOL.phone}</p>
          <p className="muted-light">✉️ {SCHOOL.email}</p>
        </div>
      </div>
      <div className="foot-bottom">
        <div className="container">
          © {new Date().getFullYear()} {SCHOOL.name}. All rights reserved.
        </div>
      </div>
    </footer>
  );
}

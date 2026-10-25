import { useState, useEffect } from "react";
import { useNavigate, Link } from "react-router-dom";
import { useAuth } from "../context/AuthContext";
import { useLang } from "../i18n/LanguageContext";
import api from "../api/client";
import { SCHOOL } from "../api/mockData";
import "./auth.css";

const PORTAL_PATH = {
  PRINCIPAL: "/admin-portal", ADMIN: "/admin-portal",
  TEACHER: "/teacher-portal", STUDENT: "/student-portal",
};

function AuthShell({ children }) {
  return (
    <div className="auth-wrap">
      <div className="auth-side">
        <div className="brand-logo big">{SCHOOL.short}</div>
        <h2>{SCHOOL.name}</h2>
        <p>{SCHOOL.tagline}</p>
        <ul>
          <li>✓ Access marks, assignments & results</li>
          <li>✓ Join subject group chats</li>
          <li>✓ Stay updated with notices</li>
        </ul>
      </div>
      <div className="auth-main">{children}</div>
    </div>
  );
}

export function Login() {
  const { login } = useAuth();
  const { t } = useLang();
  const navigate = useNavigate();
  const [form, setForm] = useState({ username: "", password: "" });
  const [err, setErr] = useState("");
  const [busy, setBusy] = useState(false);

  const submit = async () => {
    setErr(""); setBusy(true);
    try {
      const user = await login(form.username, form.password);
      navigate(PORTAL_PATH[user.role]);
    } catch (e) {
      setErr(e.response?.data?.detail || t("auth.loginFailed"));
    } finally { setBusy(false); }
  };

  return (
    <AuthShell>
      <h1>{t("auth.welcomeBack")}</h1>
      <p className="muted">{t("auth.signIn")}</p>
      <label>{t("auth.username")}</label>
      <input value={form.username} onChange={(e) => setForm({ ...form, username: e.target.value })} />
      <label>{t("auth.password")}</label>
      <input type="password" value={form.password}
        onChange={(e) => setForm({ ...form, password: e.target.value })}
        onKeyDown={(e) => e.key === "Enter" && submit()} />
      {err && <p className="error-msg">{err}</p>}
      <button className="btn navy block" style={{ marginTop: 18 }} onClick={submit} disabled={busy}>
        {busy ? t("auth.signingIn") : t("nav.login")}
      </button>
      <p className="muted auth-foot">{t("auth.noAccount")} <Link to="/register">{t("auth.registerHere")}</Link></p>
      <div className="demo-box">
        <strong>Demo logins</strong> (password: <code>password123</code>)
        <span>principal · admin1 · teacher_physics · student1</span>
      </div>
    </AuthShell>
  );
}

export function Register() {
  const { t } = useLang();
  const navigate = useNavigate();
  const [form, setForm] = useState({ username: "", email: "", password: "", first_name: "", last_name: "", classroom: "" });
  const [classrooms, setClassrooms] = useState([]);
  const [done, setDone] = useState(false);
  const [err, setErr] = useState("");

  useEffect(() => { api.get("/classrooms/").then((r) => setClassrooms(r.data)).catch(() => {}); }, []);

  const submit = async () => {
    setErr("");
    try {
      const payload = { ...form };
      if (!payload.classroom) delete payload.classroom;
      await api.post("/auth/register/", payload);
      setDone(true);
    } catch (e) {
      setErr(typeof e.response?.data === "object" ? Object.values(e.response.data).join(" ") : "Registration failed");
    }
  };

  if (done)
    return (
      <AuthShell>
        <div className="center">
          <div className="success-ic">✓</div>
          <h1>{t("auth.regSubmitted")}</h1>
          <p className="muted">{t("auth.pending")}</p>
          <button className="btn navy" onClick={() => navigate("/login")}>{t("auth.goLogin")}</button>
        </div>
      </AuthShell>
    );

  return (
    <AuthShell>
      <h1>{t("auth.studentReg")}</h1>
      <p className="muted">{t("auth.createAccount")}</p>
      <div className="form-2col">
        <div><label>{t("auth.firstName")}</label><input value={form.first_name} onChange={(e) => setForm({ ...form, first_name: e.target.value })} /></div>
        <div><label>{t("auth.lastName")}</label><input value={form.last_name} onChange={(e) => setForm({ ...form, last_name: e.target.value })} /></div>
      </div>
      <label>{t("auth.username")}</label><input value={form.username} onChange={(e) => setForm({ ...form, username: e.target.value })} />
      <label>{t("contact.email")}</label><input value={form.email} onChange={(e) => setForm({ ...form, email: e.target.value })} />
      <label>{t("auth.password")}</label><input type="password" value={form.password} onChange={(e) => setForm({ ...form, password: e.target.value })} />
      <label>{t("auth.class")}</label>
      <select value={form.classroom} onChange={(e) => setForm({ ...form, classroom: e.target.value })}>
        <option value="">—</option>
        {classrooms.map((c) => <option key={c.id} value={c.id}>{c.name} {c.section}</option>)}
      </select>
      {err && <p className="error-msg">{err}</p>}
      <button className="btn navy block" style={{ marginTop: 18 }} onClick={submit}>{t("nav.register")}</button>
      <p className="muted auth-foot">{t("auth.noAccount")} <Link to="/login">{t("nav.login")}</Link></p>
    </AuthShell>
  );
}

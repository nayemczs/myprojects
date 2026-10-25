import { useState, useEffect } from "react";
import api from "../../api/client";
import { DashShell, StatCards, LineChart, DonutChart, Panel } from "../../components/Dashboard";
import {
  ADMIN_STATS, ENROLLMENT_TREND, ENROLLMENT_LABELS, GRADE_DIST, NOTICES, withFallback,
} from "../../api/mockData";
import { useAuth } from "../../context/AuthContext";
import { useLang } from "../../i18n/LanguageContext";

export default function AdminPortal() {
  const { user } = useAuth();
  const { t } = useLang();
  const [tab, setTab] = useState("overview");
  const nav = [
    { key: "overview", label: t("dash.overview"), icon: "📊" },
    { key: "content", label: t("dash.content"), icon: "📝" },
    { key: "approvals", label: t("dash.approvals"), icon: "✅" },
    { key: "marks", label: t("dash.marks"), icon: "🎯" },
  ];
  if (user.role === "PRINCIPAL") nav.push({ key: "admins", label: t("dash.admins"), icon: "👥" });

  const titles = { overview: t("dash.adminDash"), content: t("admin.published"), approvals: t("admin.pendingStudents"), marks: t("admin.marksAwaiting"), admins: t("admin.addAdmin") };

  return (
    <DashShell title={titles[tab]} nav={nav} active={tab} onNav={setTab}>
      {tab === "overview" && <Overview />}
      {tab === "content" && <ContentManager />}
      {tab === "approvals" && <StudentApprovals />}
      {tab === "marks" && <MarkApprovals />}
      {tab === "admins" && <AdminManager />}
    </DashShell>
  );
}

function Overview() {
  const [notices, setNotices] = useState(NOTICES);
  useEffect(() => { withFallback(api.get("/posts/?kind=NOTICE"), NOTICES).then(setNotices); }, []);
  return (
    <div>
      <StatCards items={ADMIN_STATS} />
      <div className="dash-grid c2">
        <Panel title="Enrollment Trend">
          <LineChart data={ENROLLMENT_TREND} labels={ENROLLMENT_LABELS} />
        </Panel>
        <Panel title="Grade Distribution">
          <DonutChart data={GRADE_DIST} />
        </Panel>
      </div>
      <div style={{ height: 20 }} />
      <Panel title="Recent Notices">
        <table>
          <thead><tr><th>Title</th><th>Date</th><th>Type</th></tr></thead>
          <tbody>
            {notices.slice(0, 5).map((n) => (
              <tr key={n.id}><td>{n.title}</td><td>{new Date(n.created_at).toLocaleDateString()}</td><td><span className="badge approved">{n.kind || "NOTICE"}</span></td></tr>
            ))}
          </tbody>
        </table>
      </Panel>
    </div>
  );
}

function ContentManager() {
  const [posts, setPosts] = useState([]);
  const [form, setForm] = useState({ kind: "POST", title: "", body: "", event_date: "" });
  const [editing, setEditing] = useState(null);
  const [msg, setMsg] = useState("");

  const load = () => withFallback(api.get("/posts/"), []).then(setPosts);
  useEffect(() => { load(); }, []);

  const save = async () => {
    const payload = { ...form };
    if (!payload.event_date) delete payload.event_date;
    try {
      if (editing) await api.patch(`/posts/${editing}/`, payload);
      else await api.post("/posts/", payload);
      setForm({ kind: "POST", title: "", body: "", event_date: "" }); setEditing(null); load();
    } catch { setMsg("Couldn't save — is the backend running and are you logged in as admin?"); }
  };
  const remove = async (id) => { try { await api.delete(`/posts/${id}/`); load(); } catch {} };
  const edit = (p) => { setEditing(p.id); setForm({ kind: p.kind, title: p.title, body: p.body, event_date: p.event_date || "" }); };

  return (
    <div className="dash-grid c2">
      <Panel title={editing ? "Edit Content" : "New Content"}>
        <label>Type</label>
        <select value={form.kind} onChange={(e) => setForm({ ...form, kind: e.target.value })}>
          <option value="POST">Post</option><option value="NOTICE">Notice</option><option value="EVENT">Event</option>
        </select>
        <label>Title</label>
        <input value={form.title} onChange={(e) => setForm({ ...form, title: e.target.value })} />
        <label>Body</label>
        <textarea rows={4} value={form.body} onChange={(e) => setForm({ ...form, body: e.target.value })} />
        {form.kind === "EVENT" && (<><label>Event date</label><input type="datetime-local" value={form.event_date} onChange={(e) => setForm({ ...form, event_date: e.target.value })} /></>)}
        {msg && <p className="error-msg">{msg}</p>}
        <br />
        <button className="btn navy" onClick={save}>{editing ? "Update" : "Publish"}</button>
        {editing && <button className="btn sm outline" style={{ marginLeft: 8 }} onClick={() => { setEditing(null); setForm({ kind: "POST", title: "", body: "", event_date: "" }); }}>Cancel</button>}
      </Panel>
      <Panel title="Published Content">
        <table>
          <thead><tr><th>Type</th><th>Title</th><th></th></tr></thead>
          <tbody>
            {posts.length === 0 && <tr><td colSpan="3" className="muted">No content yet. Create one on the left.</td></tr>}
            {posts.map((p) => (
              <tr key={p.id}>
                <td><span className="badge approved">{p.kind}</span></td><td>{p.title}</td>
                <td style={{ whiteSpace: "nowrap" }}>
                  <button className="btn sm outline" onClick={() => edit(p)}>Edit</button>{" "}
                  <button className="btn sm danger" onClick={() => remove(p.id)}>Delete</button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </Panel>
    </div>
  );
}

function StudentApprovals() {
  const [pending, setPending] = useState([]);
  const load = () => withFallback(api.get("/users/?role=STUDENT&approved=false"), []).then(setPending);
  useEffect(() => { load(); }, []);
  const approve = async (id) => { try { await api.post(`/users/${id}/approve/`); load(); } catch {} };
  return (
    <Panel title="Pending Student Registrations">
      {pending.length === 0 && <p className="muted">No pending students right now.</p>}
      {pending.length > 0 && (
        <table>
          <thead><tr><th>Name</th><th>Username</th><th>Email</th><th></th></tr></thead>
          <tbody>
            {pending.map((u) => (
              <tr key={u.id}><td>{u.first_name} {u.last_name}</td><td>{u.username}</td><td>{u.email}</td>
                <td><button className="btn sm success" onClick={() => approve(u.id)}>Approve</button></td></tr>
            ))}
          </tbody>
        </table>
      )}
    </Panel>
  );
}

function MarkApprovals() {
  const [marks, setMarks] = useState([]);
  const load = () => withFallback(api.get("/marks/"), []).then((d) => setMarks(d.filter((m) => m.status === "PENDING")));
  useEffect(() => { load(); }, []);
  const act = async (id, action) => { try { await api.post(`/marks/${id}/${action}/`); load(); } catch {} };
  return (
    <Panel title="Marks Awaiting Approval">
      {marks.length === 0 && <p className="muted">Nothing pending. When teachers submit marks, they appear here for approval.</p>}
      {marks.length > 0 && (
        <table>
          <thead><tr><th>Student</th><th>Subject</th><th>Exam</th><th>Score</th><th></th></tr></thead>
          <tbody>
            {marks.map((m) => (
              <tr key={m.id}><td>{m.student_name}</td><td>{m.subject_name}</td><td>{m.exam_name}</td><td><strong>{m.score}</strong></td>
                <td style={{ whiteSpace: "nowrap" }}>
                  <button className="btn sm success" onClick={() => act(m.id, "approve")}>Approve</button>{" "}
                  <button className="btn sm danger" onClick={() => act(m.id, "reject")}>Reject</button>
                </td></tr>
            ))}
          </tbody>
        </table>
      )}
    </Panel>
  );
}

function AdminManager() {
  const [admins, setAdmins] = useState([]);
  const [form, setForm] = useState({ username: "", email: "", first_name: "", password: "" });
  const [msg, setMsg] = useState("");
  const load = () => withFallback(api.get("/users/?role=ADMIN"), []).then(setAdmins);
  useEffect(() => { load(); }, []);
  const create = async () => {
    setMsg("");
    try { await api.post("/users/create_admin/", form); setMsg("✓ Administrator created."); setForm({ username: "", email: "", first_name: "", password: "" }); load(); }
    catch (e) { setMsg(e.response?.data?.error || "Failed to create."); }
  };
  return (
    <div className="dash-grid c2">
      <Panel title="Add Administrator">
        {["first_name", "username", "email"].map((f) => (
          <div key={f}><label>{f.replace("_", " ")}</label><input value={form[f]} onChange={(e) => setForm({ ...form, [f]: e.target.value })} /></div>
        ))}
        <label>Password</label>
        <input type="password" value={form.password} onChange={(e) => setForm({ ...form, password: e.target.value })} />
        {msg && <p className="muted" style={{ marginTop: 10 }}>{msg}</p>}
        <br />
        <button className="btn navy" onClick={create}>Create Administrator</button>
      </Panel>
      <Panel title="Current Administrators">
        <table><tbody>
          {admins.length === 0 && <tr><td className="muted">None yet.</td></tr>}
          {admins.map((a) => <tr key={a.id}><td><div className="dash-user"><div className="avatar">{a.username[0].toUpperCase()}</div><div><strong>{a.username}</strong><span>{a.email}</span></div></div></td></tr>)}
        </tbody></table>
      </Panel>
    </div>
  );
}

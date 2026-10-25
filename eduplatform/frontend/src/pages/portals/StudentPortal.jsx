import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import api from "../../api/client";
import { DashShell, StatCards, LineChart, Panel } from "../../components/Dashboard";
import { useLang } from "../../i18n/LanguageContext";
import {
  STUDENT_STATS, STUDENT_MARKS, STUDENT_PROGRESS, PROGRESS_LABELS, ASSIGNMENTS, withFallback,
} from "../../api/mockData";

export default function StudentPortal() {
  const { t } = useLang();
  const [tab, setTab] = useState("overview");
  const navigate = useNavigate();
  const nav = [
    { key: "overview", label: t("dash.overview"), icon: "📊" },
    { key: "marks", label: t("dash.myMarks"), icon: "🎯" },
    { key: "assignments", label: t("dash.assignments"), icon: "📝" },
    { key: "chat", label: t("dash.groupChat"), icon: "💬" },
  ];
  const titles = { overview: t("dash.studentDash"), marks: t("student.myResults"), assignments: t("dash.assignments") };

  const onNav = (k) => { if (k === "chat") navigate("/chat"); else setTab(k); };

  return (
    <DashShell title={titles[tab]} nav={nav} active={tab} onNav={onNav}>
      {tab === "overview" && <Overview />}
      {tab === "marks" && <MyMarks />}
      {tab === "assignments" && <MyAssignments />}
    </DashShell>
  );
}

function Overview() {
  const [marks, setMarks] = useState(STUDENT_MARKS);
  useEffect(() => {
    withFallback(api.get("/marks/"), null).then((d) => {
      if (Array.isArray(d) && d.length) setMarks(d.map((m) => ({ subject: m.subject_name, score: Number(m.score), grade: "" })));
    });
  }, []);
  return (
    <div>
      <StatCards items={STUDENT_STATS} />
      <div className="dash-grid c2">
        <Panel title="Progress Over Time">
          <LineChart data={STUDENT_PROGRESS} labels={PROGRESS_LABELS} color="#1a9d5a" />
        </Panel>
        <Panel title="Subject Scores">
          {marks.map((m) => (
            <div key={m.subject} style={{ marginBottom: 14 }}>
              <div className="row" style={{ justifyContent: "space-between", marginBottom: 5 }}>
                <span>{m.subject}</span><strong>{m.score}%</strong>
              </div>
              <div className="progress-bar"><span style={{ width: `${m.score}%` }} /></div>
            </div>
          ))}
        </Panel>
      </div>
    </div>
  );
}

function MyMarks() {
  const [marks, setMarks] = useState(STUDENT_MARKS.map((m) => ({ exam_name: "Half Yearly 2026", subject_name: m.subject, score: m.score })));
  useEffect(() => {
    withFallback(api.get("/marks/"), null).then((d) => { if (Array.isArray(d) && d.length) setMarks(d); });
  }, []);
  return (
    <Panel title="Approved Results">
      <table>
        <thead><tr><th>Exam</th><th>Subject</th><th>Score</th></tr></thead>
        <tbody>
          {marks.map((m, i) => (
            <tr key={i}><td>{m.exam_name}</td><td>{m.subject_name}</td><td><strong>{m.score}</strong></td></tr>
          ))}
        </tbody>
      </table>
      <p className="muted" style={{ marginTop: 12 }}>Only marks approved by the administration are shown here.</p>
    </Panel>
  );
}

function MyAssignments() {
  const [assignments, setAssignments] = useState(ASSIGNMENTS);
  useEffect(() => { withFallback(api.get("/assignments/"), ASSIGNMENTS).then(setAssignments); }, []);
  return (
    <div className="dash-grid">
      {assignments.map((a) => <AssignmentCard key={a.id} a={a} />)}
    </div>
  );
}

function AssignmentCard({ a }) {
  const [file, setFile] = useState(null);
  const [msg, setMsg] = useState("");
  const submit = async () => {
    setMsg("");
    const fd = new FormData(); fd.append("file", file);
    try { await api.post(`/assignments/${a.id}/submissions/`, fd, { headers: { "Content-Type": "multipart/form-data" } }); setMsg("✓ Submitted"); }
    catch { setMsg("Submission needs the backend running."); }
  };
  const overdue = a.status === "submitted";
  return (
    <Panel title={a.title} action={<span className={`badge ${overdue ? "approved" : "pending"}`}>{a.status || "due"}</span>}>
      <p className="muted">{a.subject_name} · due {new Date(a.due_date).toLocaleString()}</p>
      <p>{a.description}</p>
      <div className="row wrap" style={{ alignItems: "center" }}>
        <input type="file" style={{ maxWidth: 260 }} onChange={(e) => setFile(e.target.files[0])} />
        <button className="btn navy sm" onClick={submit} disabled={!file}>Submit</button>
        {msg && <span className="muted">{msg}</span>}
      </div>
    </Panel>
  );
}

import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import api from "../../api/client";
import { DashShell, StatCards, BarChart, Panel } from "../../components/Dashboard";
import PaperViewer from "../../components/PaperViewer";
import { useLang } from "../../i18n/LanguageContext";
import {
  TEACHER_STATS, CLASS_PERFORMANCE, CLASS_LABELS, withFallback,
  CLASSES, CLASS_ASSIGNMENTS,
} from "../../api/mockData";

export default function TeacherPortal() {
  const { t } = useLang();
  const [tab, setTab] = useState("overview");
  const navigate = useNavigate();
  const nav = [
    { key: "overview", label: t("dash.overview"), icon: "📊" },
    { key: "marks", label: t("dash.submitMarks"), icon: "🎯" },
    { key: "assignments", label: t("dash.assignments"), icon: "📝" },
    { key: "chat", label: t("dash.groupChat"), icon: "💬" },
  ];
  const titles = { overview: t("dash.teacherDash"), marks: t("dash.submitMarks"), assignments: t("dash.assignments") };
  const onNav = (k) => { if (k === "chat") navigate("/chat"); else setTab(k); };
  return (
    <DashShell title={titles[tab]} nav={nav} active={tab} onNav={onNav}>
      {tab === "overview" && <Overview />}
      {tab === "marks" && <MarkEntry />}
      {tab === "assignments" && <Assignments />}
    </DashShell>
  );
}

function Overview() {
  return (
    <div>
      <StatCards items={TEACHER_STATS} />
      <div className="dash-grid c2">
        <Panel title="Class Average Performance (%)">
          <BarChart data={CLASS_PERFORMANCE} labels={CLASS_LABELS} />
        </Panel>
        <Panel title="Upcoming">
          <ul className="tick-list">
            <li>Half-Yearly marks submission — due Mar 10</li>
            <li>Grade pending lab reports (7)</li>
            <li>Parent-teacher meeting — Mar 15</li>
            <li>Submit attendance for the week</li>
          </ul>
        </Panel>
      </div>
    </div>
  );
}

function MarkEntry() {
  const [subjects, setSubjects] = useState([]);
  const [exams, setExams] = useState([]);
  const [students, setStudents] = useState([]);
  const [subjectId, setSubjectId] = useState("");
  const [examId, setExamId] = useState("");
  const [scores, setScores] = useState({});
  const [msg, setMsg] = useState("");

  useEffect(() => { withFallback(api.get("/subjects/?mine=true"), []).then(setSubjects); }, []);
  useEffect(() => {
    if (!subjectId) return;
    const subj = subjects.find((s) => String(s.id) === String(subjectId));
    if (!subj) return;
    withFallback(api.get(`/students/?classroom=${subj.classroom}`), []).then(setStudents);
    withFallback(api.get(`/exams/`), []).then((d) => setExams(d.filter((e) => e.classroom === subj.classroom)));
  }, [subjectId, subjects]);

  const submit = async () => {
    setMsg("");
    const marks = students.map((s) => ({ student: s.id, score: scores[s.id] || 0 }));
    try {
      const { data } = await api.post("/marks/bulk_submit/", { exam: examId, subject: subjectId, marks });
      setMsg(`✓ Submitted ${data.submitted} marks. Sent to administration for approval.`); setScores({});
    } catch { setMsg("Couldn't submit — ensure the backend is running and you're logged in as the subject's teacher."); }
  };

  return (
    <Panel title="Enter Exam Marks">
      {subjects.length === 0 && <p className="muted">No subjects assigned to you yet (or backend offline). An admin assigns subjects in Django admin.</p>}
      <div className="form-2col">
        <div>
          <label>Subject</label>
          <select value={subjectId} onChange={(e) => setSubjectId(e.target.value)}>
            <option value="">— select —</option>
            {subjects.map((s) => <option key={s.id} value={s.id}>{s.name} ({s.classroom_name})</option>)}
          </select>
        </div>
        <div>
          <label>Exam</label>
          <select value={examId} onChange={(e) => setExamId(e.target.value)}>
            <option value="">— select —</option>
            {exams.map((e) => <option key={e.id} value={e.id}>{e.name}</option>)}
          </select>
        </div>
      </div>
      {subjectId && examId && students.length > 0 && (
        <>
          <table style={{ marginTop: 18 }}>
            <thead><tr><th>Student</th><th>Score</th></tr></thead>
            <tbody>
              {students.map((s) => (
                <tr key={s.id}>
                  <td>{s.name || s.username} <span className="muted">({s.roll})</span></td>
                  <td><input type="number" style={{ width: 110 }} value={scores[s.id] || ""} onChange={(e) => setScores({ ...scores, [s.id]: e.target.value })} /></td>
                </tr>
              ))}
            </tbody>
          </table>
          <br />
          <button className="btn navy" onClick={submit}>Submit to Administration</button>
        </>
      )}
      {msg && <p className="muted" style={{ marginTop: 14 }}>{msg}</p>}
    </Panel>
  );
}

/* ---- Assignments: pick class -> list assignments -> open one -> submissions ---- */
function Assignments() {
  const [classId, setClassId] = useState(CLASSES[0].id);
  const [openId, setOpenId] = useState(null);     // open assignment detail
  const [creating, setCreating] = useState(false);
  const [store, setStore] = useState(CLASS_ASSIGNMENTS); // local editable copy

  const list = store[classId] || [];
  const openAssignment = list.find((a) => a.id === openId);

  const addAssignment = (a) => {
    setStore((s) => ({ ...s, [classId]: [{ ...a, id: Date.now(), submissions: [] }, ...(s[classId] || [])] }));
    setCreating(false);
  };
  const saveGrade = (asgId, idx, grade, feedback) => {
    setStore((s) => ({
      ...s,
      [classId]: s[classId].map((a) => a.id !== asgId ? a : {
        ...a, submissions: a.submissions.map((sub, i) => i !== idx ? sub : { ...sub, grade: grade === "" ? null : Number(grade), feedback, status: "graded" }),
      }),
    }));
  };

  if (openAssignment) {
    return <AssignmentDetail a={openAssignment} onBack={() => setOpenId(null)} onGrade={saveGrade} />;
  }

  return (
    <div>
      {/* Class selector — different screen per class */}
      <div className="class-tabs">
        {CLASSES.map((c) => (
          <button key={c.id} className={classId === c.id ? "on" : ""} onClick={() => setClassId(c.id)}>
            {c.name} {c.section}
          </button>
        ))}
        <button className="btn navy sm class-new" onClick={() => setCreating(true)}>+ New Assignment</button>
      </div>

      {creating && <CreateAssignment onClose={() => setCreating(false)} onCreate={addAssignment} />}

      <div className="dash-grid">
        {list.length === 0 && <Panel title="No assignments"><p className="muted">No assignments for this class yet. Create one above.</p></Panel>}
        {list.map((a) => {
          const total = a.submissions.length;
          const done = a.submissions.filter((s) => s.status !== "missing").length;
          const graded = a.submissions.filter((s) => s.status === "graded").length;
          return (
            <div key={a.id} className="panel assign-card" onClick={() => setOpenId(a.id)}>
              <div className="assign-card-top">
                <div>
                  <h3>{a.title}</h3>
                  <p className="muted">{a.subject_name} · due {new Date(a.due_date).toLocaleDateString()} · posted {new Date(a.created_at).toLocaleDateString()}</p>
                </div>
                <span className="badge approved">{done}/{total} submitted</span>
              </div>
              <p className="muted">{a.description}</p>
              <div className="assign-progress">
                <div className="progress-bar"><span style={{ width: `${total ? (done / total) * 100 : 0}%` }} /></div>
                <span className="muted">{graded} graded</span>
                <span className="open-link">Open details →</span>
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}

function AssignmentDetail({ a, onBack, onGrade }) {
  const [filter, setFilter] = useState("all");
  const total = a.submissions.length;
  const submitted = a.submissions.filter((s) => s.status !== "missing").length;
  const graded = a.submissions.filter((s) => s.status === "graded").length;
  const missing = total - submitted;

  const shown = a.submissions.filter((s) =>
    filter === "all" ? true :
    filter === "submitted" ? s.status !== "missing" :
    filter === "graded" ? s.status === "graded" :
    s.status === "missing"
  );

  return (
    <div>
      <button className="btn outline sm" onClick={onBack}>← Back to assignments</button>
      <div className="panel" style={{ marginTop: 14 }}>
        <h2 style={{ margin: 0 }}>{a.title}</h2>
        <p className="muted">{a.subject_name} · due {new Date(a.due_date).toLocaleString()}</p>
        <p>{a.description}</p>
      </div>

      <div className="stat-cards" style={{ marginTop: 16 }}>
        <div className="stat-card"><div className="stat-card-ic">👥</div><div className="stat-card-body"><strong>{total}</strong><span>Total students</span></div></div>
        <div className="stat-card"><div className="stat-card-ic">📤</div><div className="stat-card-body"><strong>{submitted}</strong><span>Submitted</span></div></div>
        <div className="stat-card"><div className="stat-card-ic">✅</div><div className="stat-card-body"><strong>{graded}</strong><span>Graded</span></div></div>
        <div className="stat-card"><div className="stat-card-ic">⏳</div><div className="stat-card-body"><strong>{missing}</strong><span>Not submitted</span></div></div>
      </div>

      <div className="dash-tabs" style={{ marginTop: 16 }}>
        {[["all", "All"], ["submitted", "Submitted"], ["graded", "Graded"], ["missing", "Not submitted"]].map(([k, l]) => (
          <button key={k} className={filter === k ? "on" : ""} onClick={() => setFilter(k)}>{l}</button>
        ))}
      </div>

      <Panel title="Student Submissions">
        <table>
          <thead><tr><th>Student</th><th>Status</th><th>File</th><th>Submitted</th><th>Grade</th><th>Feedback</th></tr></thead>
          <tbody>
            {shown.map((s) => {
              const realIdx = a.submissions.indexOf(s);
              return <SubmissionRow key={s.student} s={s} onSave={(g, f) => onGrade(a.id, realIdx, g, f)} />;
            })}
            {shown.length === 0 && <tr><td colSpan="6" className="muted">No students in this filter.</td></tr>}
          </tbody>
        </table>
      </Panel>
    </div>
  );
}

function SubmissionRow({ s, onSave }) {
  const [grade, setGrade] = useState(s.grade ?? "");
  const [feedback, setFeedback] = useState(s.feedback || "");
  const [strokes, setStrokes] = useState(s.strokes || []);
  const [viewing, setViewing] = useState(false);
  const badge = s.status === "graded" ? "approved" : s.status === "missing" ? "rejected" : "pending";
  const closeViewer = (newStrokes) => { setStrokes(newStrokes); s.strokes = newStrokes; setViewing(false); };
  return (
    <tr>
      <td><strong>{s.student}</strong><div className="muted">Roll {s.roll}</div></td>
      <td><span className={`badge ${badge}`}>{s.status}</span></td>
      <td>
        {s.file ? (
          <button className="btn sm outline" onClick={() => setViewing(true)}>
            📄 View / Mark{strokes.length > 0 && <span className="mark-count">{strokes.length}</span>}
          </button>
        ) : <span className="muted">—</span>}
      </td>
      <td>{s.submitted_at ? new Date(s.submitted_at).toLocaleString() : <span className="muted">—</span>}</td>
      <td><input type="number" style={{ width: 70 }} value={grade} disabled={s.status === "missing"} onChange={(e) => setGrade(e.target.value)} /></td>
      <td>
        <div className="row" style={{ gap: 6 }}>
          <input value={feedback} disabled={s.status === "missing"} placeholder="note…" onChange={(e) => setFeedback(e.target.value)} />
          <button className="btn navy sm" disabled={s.status === "missing"} onClick={() => onSave(grade, feedback)}>Save</button>
        </div>
        {viewing && <PaperViewer submission={{ ...s, strokes }} onClose={closeViewer} />}
      </td>
    </tr>
  );
}

function CreateAssignment({ onClose, onCreate }) {
  const [f, setF] = useState({ title: "", subject_name: "", description: "", due_date: "" });
  return (
    <div className="wa-modal-back" onClick={onClose}>
      <div className="wa-modal" onClick={(e) => e.stopPropagation()}>
        <h3>New Assignment</h3>
        <label>Title</label><input value={f.title} onChange={(e) => setF({ ...f, title: e.target.value })} />
        <label>Subject</label><input value={f.subject_name} onChange={(e) => setF({ ...f, subject_name: e.target.value })} placeholder="e.g. Physics" />
        <label>Description</label><textarea rows={3} value={f.description} onChange={(e) => setF({ ...f, description: e.target.value })} />
        <label>Due date</label><input type="datetime-local" value={f.due_date} onChange={(e) => setF({ ...f, due_date: e.target.value })} />
        <div className="wa-modal-foot">
          <button className="btn outline sm" onClick={onClose}>Cancel</button>
          <button className="btn navy sm" disabled={!f.title || !f.due_date}
            onClick={() => onCreate({ ...f, created_at: new Date().toISOString() })}>Create & Send to Class</button>
        </div>
      </div>
    </div>
  );
}

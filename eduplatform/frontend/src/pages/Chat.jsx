import { useState, useEffect, useRef } from "react";
import { useNavigate } from "react-router-dom";
import api from "../api/client";
import { useAuth } from "../context/AuthContext";
import { useLang } from "../i18n/LanguageContext";
import {
  CHAT_GROUPS, CHAT_MESSAGES, CLASSES, CLASS_STUDENTS, withFallback,
} from "../api/mockData";
import "./chat.css";

const EMOJIS = ["😀", "😂", "😊", "👍", "🙏", "❤️", "🎉", "🔥", "😢", "😮", "👏", "✅", "📚", "✍️", "💯", "🤔"];

export default function Chat() {
  const { user } = useAuth();
  const { t } = useLang();
  const navigate = useNavigate();
  const canCreate = user && ["TEACHER", "PRINCIPAL", "ADMIN"].includes(user.role);

  const [groups, setGroups] = useState(() =>
    CHAT_GROUPS.map((g) => ({ ...g, unread: Math.floor(Math.random() * 3), online: Math.random() > 0.4 }))
  );
  const [active, setActive] = useState(groups[0]);
  const [threads, setThreads] = useState({ ...CHAT_MESSAGES });
  const [text, setText] = useState("");
  const [search, setSearch] = useState("");          // chat-list search
  const [msgSearch, setMsgSearch] = useState("");     // in-conversation search
  const [showMsgSearch, setShowMsgSearch] = useState(false);
  const [showList, setShowList] = useState(true);
  const [showEmoji, setShowEmoji] = useState(false);
  const [replyTo, setReplyTo] = useState(null);
  const [editing, setEditing] = useState(null);
  const [menuFor, setMenuFor] = useState(null);
  const [typing, setTyping] = useState(false);
  const [showCreate, setShowCreate] = useState(false);
  const endRef = useRef(null);
  const fileRef = useRef(null);

  const messages = threads[active?.id] || [];

  useEffect(() => {
    withFallback(api.get("/groups/"), CHAT_GROUPS).then((data) => {
      const mapped = data.map((g, i) => ({
        id: g.id,
        name: g.subject_name ? `${g.subject_name} — Group` : (CHAT_GROUPS[i]?.name || "Group"),
        subject_name: g.subject_name || CHAT_GROUPS[i]?.subject_name || "Subject",
        avatar: CHAT_GROUPS[i]?.avatar || "💬", color: CHAT_GROUPS[i]?.color || "#0a4a88",
        lastTime: CHAT_GROUPS[i]?.lastTime || "",
        unread: Math.floor(Math.random() * 3), online: Math.random() > 0.4,
      }));
      if (mapped.length) { setGroups(mapped); setActive((a) => mapped.find((m) => m.id === a?.id) || mapped[0]); }
    });
  }, []);

  useEffect(() => {
    if (!active) return;
    setGroups((gs) => gs.map((g) => (g.id === active.id ? { ...g, unread: 0 } : g)));
    if (threads[active.id]) return;
    withFallback(api.get(`/groups/${active.id}/messages/`), CHAT_MESSAGES[active.id] || []).then((data) => {
      const mapped = Array.isArray(data) ? data.map((m) => ({
        id: m.id, sender_name: m.sender_name, text: m.text, created_at: m.created_at,
        me: m.sender_name === user?.username, status: "read",
      })) : [];
      setThreads((t) => ({ ...t, [active.id]: mapped.length ? mapped : (CHAT_MESSAGES[active.id] || []) }));
    });
  }, [active, user]); // eslint-disable-line

  useEffect(() => { endRef.current?.scrollIntoView({ behavior: "smooth" }); }, [messages.length, active, typing]);

  // simulate someone typing + replying occasionally
  useEffect(() => {
    if (!active) return;
    const t = setTimeout(() => setTyping(true), 1500);
    const t2 = setTimeout(() => setTyping(false), 4200);
    return () => { clearTimeout(t); clearTimeout(t2); setTyping(false); };
  }, [active]);

  const fmt = (iso) => { try { return new Date(iso).toLocaleTimeString("en", { hour: "2-digit", minute: "2-digit" }); } catch { return ""; } };

  const pushMsg = (msg) => setThreads((t) => ({ ...t, [active.id]: [...(t[active.id] || []), msg] }));

  const send = async () => {
    if (!text.trim()) return;
    if (editing) {
      setThreads((t) => ({ ...t, [active.id]: t[active.id].map((m) => m.id === editing ? { ...m, text: text.trim(), edited: true } : m) }));
      setEditing(null); setText(""); return;
    }
    const msg = {
      id: Date.now(), sender_name: "You", text: text.trim(), created_at: new Date().toISOString(),
      me: true, status: "sent", replyTo: replyTo ? { name: replyTo.sender_name, text: replyTo.text } : null,
    };
    pushMsg(msg); setText(""); setReplyTo(null); setShowEmoji(false);
    // fake delivery -> read ticks
    setTimeout(() => setThreads((t) => ({ ...t, [active.id]: t[active.id].map((m) => m.id === msg.id ? { ...m, status: "delivered" } : m) })), 700);
    setTimeout(() => setThreads((t) => ({ ...t, [active.id]: t[active.id].map((m) => m.id === msg.id ? { ...m, status: "read" } : m) })), 1800);
    try { await api.post(`/groups/${active.id}/messages/`, { text: msg.text }); } catch { /* local */ }
  };

  const attach = (e) => {
    const file = e.target.files[0]; if (!file) return;
    const isImg = file.type.startsWith("image/");
    const msg = {
      id: Date.now(), sender_name: "You", me: true, status: "sent", created_at: new Date().toISOString(),
      text: isImg ? "" : `📎 ${file.name}`, image: isImg ? URL.createObjectURL(file) : null, fileName: isImg ? null : file.name,
    };
    pushMsg(msg); e.target.value = "";
  };

  const del = (id) => { setThreads((t) => ({ ...t, [active.id]: t[active.id].map((m) => m.id === id ? { ...m, text: "🚫 This message was deleted", deleted: true, image: null } : m) })); setMenuFor(null); };
  const startEdit = (m) => { setEditing(m.id); setText(m.text); setMenuFor(null); };

  const createGroup = (name, members) => {
    const g = { id: Date.now(), name, subject_name: name, avatar: "👥", color: "#0a4a88", lastTime: "now", unread: 0, online: true, members };
    setGroups((gs) => [g, ...gs]); setThreads((t) => ({ ...t, [g.id]: [] })); setActive(g); setShowCreate(false); setShowList(false);
  };

  const filteredGroups = groups.filter((g) => g.name.toLowerCase().includes(search.toLowerCase()));
  const visibleMsgs = msgSearch ? messages.filter((m) => (m.text || "").toLowerCase().includes(msgSearch.toLowerCase())) : messages;

  const tick = (s) => s === "read" ? "✓✓" : s === "delivered" ? "✓✓" : "✓";

  return (
    <div className="wa">
      {/* ---- Chat list ---- */}
      <aside className={`wa-list ${showList ? "" : "hide-mobile"}`}>
        <div className="wa-list-top">
          <div className="dash-user">
            <div className="avatar">{(user?.username || "U")[0].toUpperCase()}</div>
            <strong>{user?.username || "Me"}</strong>
          </div>
          <div className="wa-list-actions">
            {canCreate && <button className="wa-icon" title="New group" onClick={() => setShowCreate(true)}>＋</button>}
            <button className="wa-icon" title="Back" onClick={() => navigate(-1)}>✕</button>
          </div>
        </div>
        <div className="wa-search"><input placeholder={t("chat.searchChats")} value={search} onChange={(e) => setSearch(e.target.value)} /></div>
        <div className="wa-chats">
          {filteredGroups.map((g) => (
            <button key={g.id} className={`wa-chat ${active?.id === g.id ? "on" : ""}`} onClick={() => { setActive(g); setShowList(false); setMsgSearch(""); setShowMsgSearch(false); }}>
              <div className="wa-avatar" style={{ background: g.color }}>{g.avatar}{g.online && <i className="dot" />}</div>
              <div className="wa-chat-mid">
                <strong>{g.name}</strong>
                <span className="muted">{g.online ? t("chat.online") : t("chat.typeMessage")}</span>
              </div>
              <div className="wa-chat-end">
                <span className="wa-time">{g.lastTime}</span>
                {g.unread > 0 && <span className="wa-unread">{g.unread}</span>}
              </div>
            </button>
          ))}
        </div>
      </aside>

      {/* ---- Conversation ---- */}
      <section className={`wa-conv ${showList ? "hide-mobile" : ""}`}>
        {active ? (
          <>
            <header className="wa-conv-top">
              <button className="wa-back" onClick={() => setShowList(true)}>←</button>
              <div className="wa-avatar sm" style={{ background: active.color }}>{active.avatar}</div>
              <div className="wa-conv-title">
                <strong>{active.name}</strong>
                <span className="muted">{typing ? t("chat.typing") : active.online ? t("chat.online") : t("chat.lastSeen")}</span>
              </div>
              <div className="spacer" />
              <button className="wa-icon dark" title="Search" onClick={() => setShowMsgSearch((s) => !s)}>🔍</button>
            </header>

            {showMsgSearch && (
              <div className="wa-msgsearch"><input autoFocus placeholder="Search in conversation…" value={msgSearch} onChange={(e) => setMsgSearch(e.target.value)} /></div>
            )}

            <div className="wa-thread" onClick={() => setMenuFor(null)}>
              {visibleMsgs.map((m) => (
                <div key={m.id} className={`bubble ${m.me ? "me" : ""} ${m.deleted ? "deleted" : ""}`}>
                  {!m.me && !m.deleted && <span className="bubble-name">{m.sender_name}</span>}
                  {m.replyTo && <div className="bubble-reply"><strong>{m.replyTo.name}</strong><span>{m.replyTo.text}</span></div>}
                  {m.image && <img className="bubble-img" src={m.image} alt="attachment" />}
                  {m.text && <p>{m.text}{m.edited && <em className="edited"> (edited)</em>}</p>}
                  <span className="bubble-time">{fmt(m.created_at)}{m.me && !m.deleted && <span className={`ticks ${m.status === "read" ? "read" : ""}`}> {tick(m.status)}</span>}</span>
                  {!m.deleted && (
                    <button className="bubble-menu" onClick={(e) => { e.stopPropagation(); setMenuFor(menuFor === m.id ? null : m.id); }}>⌄</button>
                  )}
                  {menuFor === m.id && (
                    <div className="bubble-actions" onClick={(e) => e.stopPropagation()}>
                      <button onClick={() => { setReplyTo(m); setMenuFor(null); }}>↩ Reply</button>
                      {m.me && <button onClick={() => startEdit(m)}>✏ Edit</button>}
                      {m.me && <button onClick={() => del(m.id)}>🗑 Delete</button>}
                    </div>
                  )}
                </div>
              ))}
              {typing && <div className="bubble typing-bubble"><span /><span /><span /></div>}
              <div ref={endRef} />
            </div>

            {replyTo && (
              <div className="wa-replybar">
                <div><strong>Replying to {replyTo.sender_name}</strong><span>{replyTo.text}</span></div>
                <button onClick={() => setReplyTo(null)}>✕</button>
              </div>
            )}
            {editing && (
              <div className="wa-replybar edit">
                <div><strong>Editing message</strong></div>
                <button onClick={() => { setEditing(null); setText(""); }}>✕</button>
              </div>
            )}

            {showEmoji && (
              <div className="wa-emoji">
                {EMOJIS.map((e) => <button key={e} onClick={() => setText((t) => t + e)}>{e}</button>)}
              </div>
            )}

            <div className="wa-input">
              <button className="wa-icon" title="Emoji" onClick={() => setShowEmoji((s) => !s)}>😊</button>
              <button className="wa-icon" title="Attach" onClick={() => fileRef.current?.click()}>📎</button>
              <input type="file" ref={fileRef} hidden onChange={attach} />
              <input placeholder={t("chat.typeMessage")} value={text}
                onChange={(e) => setText(e.target.value)}
                onKeyDown={(e) => e.key === "Enter" && send()} />
              <button className="wa-send" onClick={send}>{editing ? "✓" : "➤"}</button>
            </div>
          </>
        ) : <div className="wa-empty"><p>Select a chat to start messaging</p></div>}
      </section>

      {showCreate && <CreateGroup onClose={() => setShowCreate(false)} onCreate={createGroup} />}
    </div>
  );
}

function CreateGroup({ onClose, onCreate }) {
  const [name, setName] = useState("");
  const [classId, setClassId] = useState("");
  const [picked, setPicked] = useState([]);
  const students = classId ? (CLASS_STUDENTS[classId] || []) : [];
  const toggle = (id) => setPicked((p) => p.includes(id) ? p.filter((x) => x !== id) : [...p, id]);

  return (
    <div className="wa-modal-back" onClick={onClose}>
      <div className="wa-modal" onClick={(e) => e.stopPropagation()}>
        <h3>Create New Group</h3>
        <label>Group name</label>
        <input value={name} onChange={(e) => setName(e.target.value)} placeholder="e.g. Physics — Class 10-A" />
        <label>Class</label>
        <select value={classId} onChange={(e) => { setClassId(e.target.value); setPicked([]); }}>
          <option value="">— select class —</option>
          {CLASSES.map((c) => <option key={c.id} value={c.id}>{c.name} {c.section}</option>)}
        </select>
        {students.length > 0 && (
          <>
            <label>Add students ({picked.length} selected)</label>
            <div className="wa-member-list">
              {students.map((s) => (
                <label key={s.id} className="wa-member">
                  <input type="checkbox" checked={picked.includes(s.id)} onChange={() => toggle(s.id)} />
                  <span>{s.name} <em className="muted">· Roll {s.roll}</em></span>
                </label>
              ))}
            </div>
          </>
        )}
        <div className="wa-modal-foot">
          <button className="btn outline sm" onClick={onClose}>Cancel</button>
          <button className="btn navy sm" disabled={!name || picked.length === 0}
            onClick={() => onCreate(name, picked)}>Create Group</button>
        </div>
      </div>
    </div>
  );
}

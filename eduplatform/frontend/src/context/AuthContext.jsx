import { createContext, useContext, useState, useEffect } from "react";
import api from "../api/client";

const AuthContext = createContext(null);

// Offline demo accounts — used when there's no backend (e.g. on Vercel).
// All four share the same password.
const DEMO_PASSWORD = "phypass123";
const DEMO_USERS = {
  physics_teacher: { id: 1, username: "physics_teacher", role: "TEACHER", first_name: "Physics", last_name: "Teacher", is_approved: true },
  student1: { id: 2, username: "student1", role: "STUDENT", first_name: "Sample", last_name: "Student", is_approved: true },
  admin1: { id: 3, username: "admin1", role: "ADMIN", first_name: "Admin", last_name: "", is_approved: true },
  principal: { id: 4, username: "principal", role: "PRINCIPAL", first_name: "The", last_name: "Principal", is_approved: true },
};

export function AuthProvider({ children }) {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Restore a demo session (works with no backend)
    const demo = localStorage.getItem("demo_user");
    if (demo) {
      try { setUser(JSON.parse(demo)); } catch { localStorage.removeItem("demo_user"); }
      setLoading(false);
      return;
    }
    const token = localStorage.getItem("access");
    if (token) {
      api.get("/auth/me/")
        .then((r) => setUser(r.data))
        .catch(() => localStorage.clear())
        .finally(() => setLoading(false));
    } else {
      setLoading(false);
    }
  }, []);

  const login = async (username, password) => {
    // 1) try the real backend first
    try {
      const { data } = await api.post("/auth/login/", { username, password });
      localStorage.setItem("access", data.access);
      localStorage.setItem("refresh", data.refresh);
      setUser(data.user);
      return data.user;
    } catch (err) {
      // 2) backend unreachable (no server) → fall back to demo accounts
      const noServer = !err.response; // network error, not a 4xx from the server
      const key = (username || "").trim().toLowerCase();
      if (noServer && DEMO_USERS[key] && password === DEMO_PASSWORD) {
        const u = DEMO_USERS[key];
        localStorage.setItem("demo_user", JSON.stringify(u));
        setUser(u);
        return u;
      }
      // wrong credentials, or server returned a real error
      throw err.response ? err : { response: { data: { detail: "invalid" } } };
    }
  };

  const logout = () => {
    localStorage.clear();
    setUser(null);
  };

  return (
    <AuthContext.Provider value={{ user, loading, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
}

export const useAuth = () => useContext(AuthContext);

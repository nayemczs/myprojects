import { Routes, Route, useLocation } from "react-router-dom";
import Navbar from "./components/Navbar";
import Footer from "./components/Footer";
import ProtectedRoute from "./routes/ProtectedRoute";
import { Home, Faculties, FacultyDetail, Events, About, Admission, Contact } from "./pages/PublicPages";
import { Login, Register } from "./pages/AuthPages";
import AdminPortal from "./pages/portals/AdminPortal";
import TeacherPortal from "./pages/portals/TeacherPortal";
import StudentPortal from "./pages/portals/StudentPortal";
import Chat from "./pages/Chat";
import LanguagePopup from "./components/LanguagePopup";
import LangToggle from "./components/LangToggle";
import "./responsive.css"; // loaded last so it refines the other stylesheets

export default function App() {
  const { pathname } = useLocation();
  // Full-height screens: no footer so the layout fills the viewport.
  const noFooter = ["/admin-portal", "/teacher-portal", "/student-portal", "/chat"].some((p) => pathname.startsWith(p));

  return (
    <>
      <LanguagePopup />
      <LangToggle />
      <Navbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/faculties" element={<Faculties />} />
        <Route path="/faculties/:slug" element={<FacultyDetail />} />
        <Route path="/events" element={<Events />} />
        <Route path="/about" element={<About />} />
        <Route path="/admission" element={<Admission />} />
        <Route path="/contact" element={<Contact />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />

        <Route path="/admin-portal" element={
          <ProtectedRoute roles={["ADMIN", "PRINCIPAL"]}><AdminPortal /></ProtectedRoute>} />
        <Route path="/teacher-portal" element={
          <ProtectedRoute roles={["TEACHER"]}><TeacherPortal /></ProtectedRoute>} />
        <Route path="/student-portal" element={
          <ProtectedRoute roles={["STUDENT"]}><StudentPortal /></ProtectedRoute>} />
        <Route path="/chat" element={
          <ProtectedRoute><Chat /></ProtectedRoute>} />
      </Routes>
      {!noFooter && <Footer />}
    </>
  );
}

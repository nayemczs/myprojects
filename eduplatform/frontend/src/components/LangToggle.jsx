import { useLang } from "../i18n/LanguageContext";
import "./langtoggle.css";

// Always-visible language switch, fixed to the top-right corner.
export default function LangToggle() {
  const { lang, choose } = useLang();
  return (
    <div className="lang-toggle" role="group" aria-label="Language">
      <button className={lang === "en" ? "on" : ""} onClick={() => choose("en")}>EN</button>
      <button className={lang === "bn" ? "on" : ""} onClick={() => choose("bn")}>বাং</button>
    </div>
  );
}

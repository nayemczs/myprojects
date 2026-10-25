import { useLang } from "../i18n/LanguageContext";
import { SCHOOL } from "../api/mockData";
import "./langpopup.css";

export default function LanguagePopup() {
  const { chosen, choose } = useLang();
  if (chosen) return null; // already picked — don't show again

  return (
    <div className="lang-back">
      <div className="lang-box">
        <div className="brand-logo big">{SCHOOL.short}</div>
        <h2 className="lang-q">আপনি কোন ভাষায় ওয়েবসাইটটি দেখতে চান?</h2>
        <p className="lang-q-en">Which language do you prefer?</p>
        <div className="lang-btns">
          <button className="lang-btn" onClick={() => choose("en")}>English</button>
          <button className="lang-btn bn" onClick={() => choose("bn")}>বাংলা</button>
        </div>
      </div>
    </div>
  );
}

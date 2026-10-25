import { createContext, useContext, useState, useCallback } from "react";
import { STRINGS } from "./strings";

const LanguageContext = createContext(null);
const KEY = "nsa_lang";

export function LanguageProvider({ children }) {
  const [lang, setLang] = useState(() => {
    try { return localStorage.getItem(KEY) || null; } catch { return null; }
  });

  const choose = useCallback((l) => {
    setLang(l);
    try { localStorage.setItem(KEY, l); } catch { /* ignore */ }
  }, []);

  // t("key") -> string in active language (defaults to English if a key/translation is missing)
  const t = useCallback((key) => {
    const entry = STRINGS[key];
    if (!entry) return key;
    const active = lang || "en";
    return entry[active] || entry.en || key;
  }, [lang]);

  return (
    <LanguageContext.Provider value={{ lang: lang || "en", chosen: !!lang, choose, t }}>
      {children}
    </LanguageContext.Provider>
  );
}

export const useLang = () => useContext(LanguageContext);

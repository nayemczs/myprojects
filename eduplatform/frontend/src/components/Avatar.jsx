import { useMemo, useState } from "react";

/**
 * Avatar — shows a profile image, or a coloured circle with the person's
 * initials when there's no image or the image fails to load. The background
 * colour is derived from the name, so each person gets a consistent colour.
 *
 * props: name (full name) OR firstName+lastName, image (url), size (px), style, fontStyle
 */
const PALETTE = [
  "#002b5c", "#0a4a88", "#1769e0", "#1a9d5a", "#128c7e",
  "#8e44ad", "#c0392b", "#d99400", "#e67e22", "#16a085",
  "#2c3e50", "#d64550", "#6c3483", "#117a65", "#b9770e",
];

function colourFor(seed) {
  let h = 0;
  for (let i = 0; i < seed.length; i++) h = (h * 31 + seed.charCodeAt(i)) >>> 0;
  return PALETTE[h % PALETTE.length];
}

// Titles/honorifics to ignore when building initials.
const TITLES = new Set([
  "mr", "mrs", "ms", "miss", "dr", "prof", "professor", "eng", "engr", "er",
  "md", "mohd", "sir", "late", "air", "cdre", "capt", "maj", "col", "lt",
  "retd", "hon", "rev", "mx",
]);

function initialsOf(name) {
  // strip trailing dots and parentheticals like "(Retd)", then drop title words
  const cleaned = name.replace(/\([^)]*\)/g, " ");
  const parts = cleaned
    .trim()
    .split(/\s+/)
    .map((w) => w.replace(/\./g, ""))
    .filter((w) => w && !TITLES.has(w.toLowerCase()));
  if (parts.length === 0) return "?";
  if (parts.length === 1) return parts[0].slice(0, 2).toUpperCase();
  return (parts[0][0] + parts[parts.length - 1][0]).toUpperCase();
}

export default function Avatar({ name, firstName, lastName, image, size = 50, style, fontStyle }) {
  const [broken, setBroken] = useState(false);
  const full = name || [firstName, lastName].filter(Boolean).join(" ") || "?";
  const initials = useMemo(() => initialsOf(full), [full]);
  const bg = useMemo(() => colourFor(full), [full]);

  if (image && !broken) {
    return (
      <img src={image} alt={full} onError={() => setBroken(true)}
        style={{ width: size, height: size, borderRadius: "50%", objectFit: "cover", ...style }} />
    );
  }
  return (
    <div style={{
      width: size, height: size, borderRadius: "50%", background: bg, color: "#fff",
      display: "flex", alignItems: "center", justifyContent: "center",
      fontWeight: 700, fontSize: size / 2.6, flexShrink: 0, lineHeight: 1,
      textTransform: "uppercase", ...style,
    }}>
      <span style={fontStyle}>{initials}</span>
    </div>
  );
}

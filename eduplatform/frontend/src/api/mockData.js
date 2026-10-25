// Rich default/fallback content so every page looks complete even with no backend data.
// Pages try the real API first (see withFallback) and use these if it returns nothing.

export const SCHOOL = {
  name: "South Point School & College",
  short: "SPSC",
  tagline: "শিক্ষা নিয়ে গড়ব দেশ, লাল সবুজের বাংলাদেশ",
  taglineEn: "Education to Build the Nation",
  established: "2003",
  eiin: "108040",
  phone: "02-41081531, 01754-412344",
  email: "spsc2002@gmail.com",
  address: "Road #11, House #251, Block J, Baridhara, Dhaka 1212, Bangladesh",
};

export const HERO_SLIDES = [
  {
    title: "Welcome to South Point School & College",
    subtitle: "A trusted name in secondary and higher secondary education since 2003.",
    img: "https://images.unsplash.com/photo-1562774053-701939374585?auto=format&fit=crop&w=1600&q=70",
  },
  {
    title: "শিক্ষা নিয়ে গড়ব দেশ, লাল সবুজের বাংলাদেশ",
    subtitle: "Nurturing excellence, discipline and values in every student.",
    img: "https://images.unsplash.com/photo-1523050854058-8df90110c9f1?auto=format&fit=crop&w=1600&q=70",
  },
  {
    title: "Admissions Open 2026",
    subtitle: "Join a community committed to academic and moral excellence.",
    img: "https://images.unsplash.com/photo-1498243691581-b145c3f54a5a?auto=format&fit=crop&w=1600&q=70",
  },
];

export const STATS = [
  { label: "Board Exam Success", label_bn: "বোর্ড পরীক্ষায় সাফল্য", value: "100%", icon: "🎓" },
  { label: "Qualified Faculty", label_bn: "যোগ্য শিক্ষক", value: "67+", icon: "👩‍🏫" },
  { label: "Awards Won", label_bn: "অর্জিত পুরস্কার", value: "30", icon: "🏆" },
  { label: "Graduates", label_bn: "গ্র্যাজুয়েট", value: "95+", icon: "🌟" },
];

// Pick the Bangla field (field + "_bn") when the language is bn and it exists.
export function L(item, field, lang) {
  if (!item) return "";
  if (lang === "bn" && item[field + "_bn"]) return item[field + "_bn"];
  return item[field];
}

export const NOTICES = [
  { id: 1, title: "New Admission Form Distribution", title_bn: "নতুন ভর্তি ফরম বিতরণ", body: "Admission forms for the upcoming session are now being distributed from the school office.", body_bn: "আসন্ন সেশনের ভর্তি ফরম স্কুল অফিস থেকে বিতরণ করা হচ্ছে।", created_at: "2026-10-04", kind: "NOTICE" },
  { id: 2, title: "Holiday for Durga Puja and Laxmi Puja", title_bn: "দুর্গাপূজা ও লক্ষ্মীপূজার ছুটি", body: "The institution will remain closed for Durga Puja and Laxmi Puja holidays.", body_bn: "দুর্গাপূজা ও লক্ষ্মীপূজা উপলক্ষে প্রতিষ্ঠান বন্ধ থাকবে।", created_at: "2026-10-17", kind: "NOTICE" },
  { id: 3, title: "বার্ষিক সাংস্কৃতিক প্রতিযোগিতা – ২০২৬", title_bn: "বার্ষিক সাংস্কৃতিক প্রতিযোগিতা – ২০২৬", body: "Annual cultural competition 2026 — students are invited to register for the events.", body_bn: "বার্ষিক সাংস্কৃতিক প্রতিযোগিতা ২০২৬ — শিক্ষার্থীদের অংশগ্রহণের জন্য নিবন্ধন করতে অনুরোধ করা হলো।", created_at: "2026-09-21", kind: "NOTICE" },
  { id: 4, title: "Notice for Tuition Fee Payment for September", title_bn: "সেপ্টেম্বর মাসের বেতন পরিশোধের নোটিশ", body: "Guardians are requested to pay the September tuition fees within the stipulated time.", body_bn: "অভিভাবকদের নির্ধারিত সময়ের মধ্যে সেপ্টেম্বর মাসের বেতন পরিশোধ করতে অনুরোধ করা হলো।", created_at: "2026-09-05", kind: "NOTICE" },
  { id: 5, title: "SSC Result-2026", title_bn: "এসএসসি ফলাফল-২০২৬", body: "Congratulations to all our students for their outstanding results in the SSC examination 2026.", body_bn: "এসএসসি পরীক্ষা ২০২৬-এ অসাধারণ ফলাফলের জন্য আমাদের সকল শিক্ষার্থীকে অভিনন্দন।", created_at: "2026-08-10", kind: "NOTICE" },
];

export const LEADERS = [
  { role: "Chairman", role_bn: "চেয়ারম্যান", name: "Eng. M. A. Rashid", name_bn: "ইঞ্জি. এম. এ. রশিদ", photo: "", msg: "When I used to close my eyes before establishing South Point School & College, I dreamed of an institution where students grow far beyond formal education.", msg_bn: "সাউথ পয়েন্ট স্কুল অ্যান্ড কলেজ প্রতিষ্ঠার আগে আমি এমন একটি প্রতিষ্ঠানের স্বপ্ন দেখতাম, যেখানে শিক্ষার্থীরা প্রথাগত শিক্ষার বাইরেও গড়ে উঠবে।" },
  { role: "Founder Principal", role_bn: "প্রতিষ্ঠাতা অধ্যক্ষ", name: "Mrs. Hamida Ali", name_bn: "মিসেস হামিদা আলী", photo: "", msg: "Education is the key to carry a nation forward. Our aim has always been to build character alongside knowledge.", msg_bn: "শিক্ষা একটি জাতিকে এগিয়ে নেওয়ার চাবিকাঠি। জ্ঞানের পাশাপাশি চরিত্র গঠনই সর্বদা আমাদের লক্ষ্য।" },
  { role: "Principal", role_bn: "অধ্যক্ষ", name: "Air Cdre (Retd) Kazi Abdul Moyen", name_bn: "এয়ার কমোডর (অব.) কাজী আব্দুল মঈন", photo: "", msg: "It is a matter of great pride to lead this institution — a strong and trusted name in secondary and higher secondary education.", msg_bn: "মাধ্যমিক ও উচ্চ মাধ্যমিক শিক্ষায় একটি শক্তিশালী ও নির্ভরযোগ্য নাম এই প্রতিষ্ঠানের নেতৃত্ব দেওয়া অত্যন্ত গর্বের বিষয়।" },
  { role: "Headmistress", role_bn: "প্রধান শিক্ষিকা", name: "Debosree Sarker", name_bn: "দেবশ্রী সরকার", photo: "", msg: "South Point stands as a benchmark for excellence in secondary and higher secondary education in our country.", msg_bn: "সাউথ পয়েন্ট আমাদের দেশে মাধ্যমিক ও উচ্চ মাধ্যমিক শিক্ষায় শ্রেষ্ঠত্বের এক মানদণ্ড।" },
];

export const ALUMNI = [
  { name: "Ashfia Khan Tuski", name_bn: "আশফিয়া খান তুস্কি", admitted: "Sahabuddin Medical College", admitted_bn: "সাহাবুদ্দিন মেডিকেল কলেজ", year: "2024", photo: "" },
  { name: "Mumtazah Nawar", name_bn: "মুমতাজাহ নওয়ার", admitted: "University of Dhaka", admitted_bn: "ঢাকা বিশ্ববিদ্যালয়", year: "2024", photo: "" },
  { name: "Arufa Rifaat", name_bn: "আরুফা রিফাত", admitted: "KUET — Engineering", admitted_bn: "কুয়েট — প্রকৌশল", year: "2024", photo: "" },
  { name: "Nabila Hossen Naba", name_bn: "নাবিলা হোসেন নাবা", admitted: "Sir Salimullah Medical College", admitted_bn: "স্যার সলিমুল্লাহ মেডিকেল কলেজ", year: "2024", photo: "" },
  { name: "Afrah Tasnim", name_bn: "আফরাহ তাসনিম", admitted: "Mugda Medical College", admitted_bn: "মুগদা মেডিকেল কলেজ", year: "2024", photo: "" },
  { name: "Nur-E-Sabah", name_bn: "নূর-ই-সাবাহ", admitted: "Shaheed Tajuddin Ahmed Medical College", admitted_bn: "শহীদ তাজউদ্দিন আহমদ মেডিকেল কলেজ", year: "2024", photo: "" },
];

export const EVENTS = [
  { id: 1, title: "A Proud Achievement of Our Young Debaters!", title_bn: "আমাদের তরুণ বিতার্কিকদের গর্বের অর্জন!", body: "Our debate team brought home honours from a recent inter-school competition.", body_bn: "সাম্প্রতিক আন্তঃস্কুল প্রতিযোগিতায় আমাদের বিতর্ক দল সম্মান বয়ে এনেছে।", event_date: "2026-08-28T10:00:00", category: "General", category_bn: "সাধারণ", img: "https://images.unsplash.com/photo-1475721027785-f74eccf877e2?auto=format&fit=crop&w=800&q=70" },
  { id: 2, title: "বাংলা নববর্ষ ১৪৩৩ উপলক্ষে বর্ষবরণ অনুষ্ঠান", title_bn: "বাংলা নববর্ষ ১৪৩৩ উপলক্ষে বর্ষবরণ অনুষ্ঠান", body: "A vibrant celebration of the Bengali New Year 1433 with music, colour and tradition.", body_bn: "সংগীত, রং ও ঐতিহ্যে বাংলা নববর্ষ ১৪৩৩-এর প্রাণবন্ত উদযাপন।", event_date: "2026-04-14T09:00:00", category: "Cultural", category_bn: "সাংস্কৃতিক", img: "https://images.unsplash.com/photo-1511578314322-379afb476865?auto=format&fit=crop&w=800&q=70" },
  { id: 3, title: "আন্তর্জাতিক মাতৃভাষা ও শহীদ দিবস উদযাপন", title_bn: "আন্তর্জাতিক মাতৃভাষা ও শহীদ দিবস উদযাপন", body: "Observance of International Mother Language Day and Martyrs' Day with due solemnity.", body_bn: "যথাযোগ্য মর্যাদায় আন্তর্জাতিক মাতৃভাষা ও শহীদ দিবস পালন।", event_date: "2026-02-21T08:00:00", category: "Cultural", category_bn: "সাংস্কৃতিক", img: "https://images.unsplash.com/photo-1524178232363-1fb2b075b655?auto=format&fit=crop&w=800&q=70" },
  { id: 4, title: "Inter Class Football Tournament 2025", title_bn: "আন্তঃশ্রেণি ফুটবল টুর্নামেন্ট ২০২৫", body: "Students competed in an energetic inter-class football tournament.", body_bn: "শিক্ষার্থীরা প্রাণবন্ত আন্তঃশ্রেণি ফুটবল টুর্নামেন্টে প্রতিযোগিতা করে।", event_date: "2025-07-10T09:00:00", category: "Sports", category_bn: "ক্রীড়া", img: "https://images.unsplash.com/photo-1461896836934-ffe607ba8211?auto=format&fit=crop&w=800&q=70" },
];

// At South Point these are the academic streams offered at secondary & higher secondary level.
export const FACULTIES = [
  { id: 1, slug: "science", name: "Science Group", name_bn: "বিজ্ঞান বিভাগ", short_desc: "Physics, Chemistry, Biology & Higher Mathematics", short_desc_bn: "পদার্থ, রসায়ন, জীববিজ্ঞান ও উচ্চতর গণিত", head_name: "Head of Science", head_name_bn: "বিজ্ঞান বিভাগের প্রধান", icon: "🔬", description: "The Science group prepares students for medical, engineering and university admission with fully-equipped physics, chemistry and biology laboratories.", description_bn: "বিজ্ঞান বিভাগ সুসজ্জিত পদার্থ, রসায়ন ও জীববিজ্ঞান গবেষণাগারের মাধ্যমে শিক্ষার্থীদের মেডিকেল, প্রকৌশল ও বিশ্ববিদ্যালয় ভর্তির জন্য প্রস্তুত করে।" },
  { id: 2, slug: "business-studies", name: "Business Studies Group", name_bn: "ব্যবসায় শিক্ষা বিভাগ", short_desc: "Accounting, Finance, Business Entrepreneurship & Economics", short_desc_bn: "হিসাববিজ্ঞান, ফিন্যান্স, উদ্যোক্তা ও অর্থনীতি", head_name: "Head of Business Studies", head_name_bn: "ব্যবসায় শিক্ষা বিভাগের প্রধান", icon: "📊", description: "The Business Studies group builds strong foundations in accounting, management and economics for future business leaders.", description_bn: "ব্যবসায় শিক্ষা বিভাগ ভবিষ্যৎ ব্যবসায়ী নেতাদের জন্য হিসাববিজ্ঞান, ব্যবস্থাপনা ও অর্থনীতিতে দৃঢ় ভিত্তি গড়ে তোলে।" },
  { id: 3, slug: "humanities", name: "Humanities Group", name_bn: "মানবিক বিভাগ", short_desc: "Bengali, English, Civics, Geography & History", short_desc_bn: "বাংলা, ইংরেজি, পৌরনীতি, ভূগোল ও ইতিহাস", head_name: "Head of Humanities", head_name_bn: "মানবিক বিভাগের প্রধান", icon: "📚", description: "The Humanities group develops critical thinking, language skills and social awareness.", description_bn: "মানবিক বিভাগ সমালোচনামূলক চিন্তা, ভাষাদক্ষতা ও সামাজিক সচেতনতা গড়ে তোলে।" },
  { id: 4, slug: "primary", name: "Primary & Junior Section", name_bn: "প্রাথমিক ও জুনিয়র শাখা", short_desc: "Nursery to Class VIII — foundation years", short_desc_bn: "নার্সারি থেকে অষ্টম শ্রেণি — ভিত্তির বছরগুলো", head_name: "Headmistress", head_name_bn: "প্রধান শিক্ষিকা", icon: "🧒", description: "Our primary and junior section nurtures young learners with care, discipline and a strong academic foundation.", description_bn: "আমাদের প্রাথমিক ও জুনিয়র শাখা যত্ন, শৃঙ্খলা ও দৃঢ় শিক্ষাগত ভিত্তির মাধ্যমে ছোট শিক্ষার্থীদের গড়ে তোলে।" },
];

// Real facilities listed by South Point School & College.
export const FACILITIES = [
  { icon: "📖", name: "Library", desc: "A well-stocked library supporting academic and recreational reading." },
  { icon: "🧪", name: "Laboratories", desc: "Modern physics, chemistry, biology and computer laboratories." },
  { icon: "⚽", name: "Sports & Games", desc: "Facilities and coaching for football, cricket and indoor games." },
  { icon: "🎭", name: "Clubs", desc: "Active clubs including the debate club and cultural activities." },
  { icon: "📷", name: "Photo & Video Gallery", desc: "A rich archive of events, programs and achievements." },
  { icon: "💳", name: "Online Payment", desc: "Convenient online admission and fee payment for guardians." },
];

// ---- Dashboard mock data ----
export const ADMIN_STATS = [
  { label: "Total Students", value: "1,284", delta: "+6%", icon: "👩‍🎓" },
  { label: "Teachers", value: "67", delta: "+2", icon: "👨‍🏫" },
  { label: "Pending Approvals", value: "9", delta: "today", icon: "⏳" },
  { label: "Active Notices", value: "14", delta: "this month", icon: "📢" },
];
export const ENROLLMENT_TREND = [620, 680, 740, 810, 900, 1010, 1120, 1284];
export const ENROLLMENT_LABELS = ["2019", "2020", "2021", "2022", "2023", "2024", "2025", "2026"];
export const GRADE_DIST = [
  { label: "A+", value: 38, color: "#1a9d5a" },
  { label: "A", value: 29, color: "#4caf50" },
  { label: "A-", value: 16, color: "#f6a800" },
  { label: "B", value: 11, color: "#ff8a3d" },
  { label: "C", value: 6, color: "#d64550" },
];

export const TEACHER_STATS = [
  { label: "My Classes", value: "5", icon: "🏫" },
  { label: "Students", value: "182", icon: "👨‍🎓" },
  { label: "Assignments", value: "12", icon: "📝" },
  { label: "Pending Grading", value: "7", icon: "✅" },
];
export const CLASS_PERFORMANCE = [72, 78, 69, 85, 80];
export const CLASS_LABELS = ["10-A", "10-B", "9-A", "9-B", "8-A"];

export const STUDENT_STATS = [
  { label: "Attendance", value: "96%", icon: "📅" },
  { label: "Avg. Grade", value: "A", icon: "🎯" },
  { label: "Assignments Due", value: "3", icon: "📌" },
  { label: "Class Rank", value: "#4", icon: "🏅" },
];
export const STUDENT_MARKS = [
  { subject: "Physics", score: 88, grade: "A+" },
  { subject: "Chemistry", score: 81, grade: "A" },
  { subject: "Mathematics", score: 92, grade: "A+" },
  { subject: "English", score: 76, grade: "A-" },
  { subject: "ICT", score: 85, grade: "A" },
];
export const STUDENT_PROGRESS = [70, 74, 72, 80, 83, 85, 88];
export const PROGRESS_LABELS = ["W1", "W2", "W3", "W4", "W5", "W6", "W7"];

export const ASSIGNMENTS = [
  { id: 1, title: "Newton's Laws Problem Set", subject_name: "Physics", due_date: "2026-03-02T23:59:00", description: "Solve problems 1–15 from chapter 4.", status: "due" },
  { id: 2, title: "Organic Chemistry Lab Report", subject_name: "Chemistry", due_date: "2026-03-05T23:59:00", description: "Write up the esterification experiment.", status: "due" },
  { id: 3, title: "Essay: Climate Change", subject_name: "English", due_date: "2026-02-20T23:59:00", description: "800-word argumentative essay.", status: "submitted" },
];

// ---- WhatsApp-style chat mock data ----
export const CHAT_GROUPS = [
  { id: 1, name: "Physics — Class 10-A", subject_name: "Physics", avatar: "🔬", color: "#0a4a88", lastTime: "10:42" },
  { id: 2, name: "Mathematics — Class 10-A", subject_name: "Mathematics", avatar: "📐", color: "#1a9d5a", lastTime: "09:15" },
  { id: 3, name: "English — Class 10-A", subject_name: "English", avatar: "📖", color: "#d99400", lastTime: "Yesterday" },
  { id: 4, name: "Chemistry — Class 10-A", subject_name: "Chemistry", avatar: "⚗️", color: "#8e44ad", lastTime: "Yesterday" },
];
export const CHAT_MESSAGES = {
  1: [
    { id: 1, sender_name: "Mr. Kamrul (Teacher)", text: "Assalamu Alaikum everyone. Reminder: problem set due this Sunday.", created_at: "2026-02-26T10:30:00", me: false },
    { id: 2, sender_name: "You", text: "Walaikum Assalam sir. Noted!", created_at: "2026-02-26T10:33:00", me: true },
    { id: 3, sender_name: "Sadia", text: "Sir, is question 12 part of it?", created_at: "2026-02-26T10:38:00", me: false },
    { id: 4, sender_name: "Mr. Kamrul (Teacher)", text: "Yes Sadia, include 1 through 15.", created_at: "2026-02-26T10:42:00", me: false },
  ],
  2: [
    { id: 1, sender_name: "Ms. Farzana (Teacher)", text: "Great work on the last quiz, class!", created_at: "2026-02-26T09:10:00", me: false },
    { id: 2, sender_name: "You", text: "Thank you ma'am 😊", created_at: "2026-02-26T09:15:00", me: true },
  ],
  3: [
    { id: 1, sender_name: "Mr. Imran (Teacher)", text: "Essay submissions look strong this term.", created_at: "2026-02-25T14:00:00", me: false },
  ],
  4: [
    { id: 1, sender_name: "Dr. Sabbir (Teacher)", text: "Lab safety briefing tomorrow before class.", created_at: "2026-02-25T16:20:00", me: false },
  ],
};

// Try the API call; if it throws or returns empty, use fallback.
export async function withFallback(promise, fallback) {
  try {
    const res = await promise;
    const data = res?.data;
    if (Array.isArray(data)) return data.length ? data : fallback;
    if (data && typeof data === "object") return data;
    return fallback;
  } catch {
    return fallback;
  }
}

// ---- Classes & students (for group creation + assignment screens) ----
export const CLASSES = [
  { id: 1, name: "Class 10", section: "A" },
  { id: 2, name: "Class 10", section: "B" },
  { id: 3, name: "Class 9", section: "A" },
];
export const CLASS_STUDENTS = {
  1: [
    { id: 11, name: "Sadia Rahman", roll: "01" },
    { id: 12, name: "Tahmid Hasan", roll: "02" },
    { id: 13, name: "Nabila Hossen", roll: "03" },
    { id: 14, name: "Rakib Chowdhury", roll: "04" },
    { id: 15, name: "Mumtazah Nawar", roll: "05" },
  ],
  2: [
    { id: 21, name: "Arufa Rifaat", roll: "01" },
    { id: 22, name: "Afrah Tasnim", roll: "02" },
    { id: 23, name: "Nur-E-Sabah", roll: "03" },
  ],
  3: [
    { id: 31, name: "Adiat Jahan", roll: "01" },
    { id: 32, name: "Monia Nigar", roll: "02" },
  ],
};

// Assignments grouped per class, with full submission detail per student.
export const CLASS_ASSIGNMENTS = {
  1: [
    {
      id: 101, title: "Newton's Laws Problem Set", subject_name: "Physics",
      due_date: "2026-03-02T23:59:00", created_at: "2026-02-20",
      description: "Solve problems 1–15 from chapter 4.",
      submissions: [
        { student: "Sadia Rahman", roll: "01", status: "graded", submitted_at: "2026-02-28T20:12:00", file: "sadia_physics.pdf", grade: 18, feedback: "Excellent work." },
        { student: "Tahmid Hasan", roll: "02", status: "submitted", submitted_at: "2026-03-01T22:40:00", file: "tahmid_physics.pdf", grade: null, feedback: "" },
        { student: "Nabila Hossen", roll: "03", status: "submitted", submitted_at: "2026-03-02T19:05:00", file: "nabila_physics.pdf", grade: null, feedback: "" },
        { student: "Rakib Chowdhury", roll: "04", status: "missing", submitted_at: null, file: null, grade: null, feedback: "" },
        { student: "Mumtazah Nawar", roll: "05", status: "graded", submitted_at: "2026-02-27T18:00:00", file: "mumtazah_physics.pdf", grade: 20, feedback: "Perfect." },
      ],
    },
    {
      id: 102, title: "Projectile Motion Lab Report", subject_name: "Physics",
      due_date: "2026-02-15T23:59:00", created_at: "2026-02-05",
      description: "Write up the projectile experiment with graphs.",
      submissions: [
        { student: "Sadia Rahman", roll: "01", status: "graded", submitted_at: "2026-02-14T21:00:00", file: "sadia_lab.pdf", grade: 17, feedback: "Good graphs." },
        { student: "Tahmid Hasan", roll: "02", status: "graded", submitted_at: "2026-02-13T20:00:00", file: "tahmid_lab.pdf", grade: 15, feedback: "Add error analysis." },
        { student: "Nabila Hossen", roll: "03", status: "missing", submitted_at: null, file: null, grade: null, feedback: "" },
      ],
    },
  ],
  2: [
    {
      id: 201, title: "Chemical Bonding Worksheet", subject_name: "Chemistry",
      due_date: "2026-03-08T23:59:00", created_at: "2026-02-25",
      description: "Complete the ionic and covalent bonding exercises.",
      submissions: [
        { student: "Arufa Rifaat", roll: "01", status: "submitted", submitted_at: "2026-03-05T19:00:00", file: "arufa_chem.pdf", grade: null, feedback: "" },
        { student: "Afrah Tasnim", roll: "02", status: "missing", submitted_at: null, file: null, grade: null, feedback: "" },
      ],
    },
  ],
  3: [
    {
      id: 301, title: "Algebra Assignment 3", subject_name: "Mathematics",
      due_date: "2026-03-10T23:59:00", created_at: "2026-02-28",
      description: "Quadratic equations, exercises 5.1–5.3.",
      submissions: [
        { student: "Adiat Jahan", roll: "01", status: "graded", submitted_at: "2026-03-07T17:00:00", file: "adiat_math.pdf", grade: 19, feedback: "Well done." },
      ],
    },
  ],
};

// Sample student writing shown in the paper viewer (stands in for the PDF content).
export const SAMPLE_WRITING = {
  title: "Answer Script",
  paragraphs: [
    "Q1. Explain Newton's three laws of motion with examples.",
    "Newton's first law states that a object remains at rest or in uniform motion unless acted upon by a external force. This is also called the law of inertia. For example, a book lying on a table stays there until someone push it.",
    "The second law says that the force applied on a body is equal to the mass multiplied by its acceleration, F = ma. When we apply more force the acceleration become greater if the mass is constant.",
    "Newton's third law tells us that for every action there is a equal and opposite reaction. When we jump, our legs push the ground downward and the ground push us upward with same force.",
    "In conclusion, these three laws form the foundation of classical mechanics and they help us understand how objects move in our daily life.",
  ],
};

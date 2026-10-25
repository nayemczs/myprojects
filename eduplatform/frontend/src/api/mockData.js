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
  { label: "Board Exam Success", value: "100%", icon: "🎓" },
  { label: "Qualified Faculty", value: "67+", icon: "👩‍🏫" },
  { label: "Awards Won", value: "30", icon: "🏆" },
  { label: "Graduates", value: "95+", icon: "🌟" },
];

export const NOTICES = [
  { id: 1, title: "New Admission Form Distribution", body: "Admission forms for the upcoming session are now being distributed from the school office.", created_at: "2026-10-04", kind: "NOTICE" },
  { id: 2, title: "Holiday for Durga Puja and Laxmi Puja", body: "The institution will remain closed for Durga Puja and Laxmi Puja holidays.", created_at: "2026-10-17", kind: "NOTICE" },
  { id: 3, title: "বার্ষিক সাংস্কৃতিক প্রতিযোগিতা – ২০২৬", body: "Annual cultural competition 2026 — students are invited to register for the events.", created_at: "2026-09-21", kind: "NOTICE" },
  { id: 4, title: "Notice for Tuition Fee Payment for September", body: "Guardians are requested to pay the September tuition fees within the stipulated time.", created_at: "2026-09-05", kind: "NOTICE" },
  { id: 5, title: "SSC Result-2026", body: "Congratulations to all our students for their outstanding results in the SSC examination 2026.", created_at: "2026-08-10", kind: "NOTICE" },
];

export const LEADERS = [
  { role: "Chairman", name: "Eng. M. A. Rashid", photo: "https://i.pravatar.cc/200?img=12", msg: "When I used to close my eyes before establishing South Point School & College, I dreamed of an institution where students grow far beyond formal education." },
  { role: "Founder Principal", name: "Mrs. Hamida Ali", photo: "https://i.pravatar.cc/200?img=45", msg: "Education is the key to carry a nation forward. Our aim has always been to build character alongside knowledge." },
  { role: "Principal", name: "Air Cdre (Retd) Kazi Abdul Moyen", photo: "https://i.pravatar.cc/200?img=52", msg: "It is a matter of great pride to lead this institution — a strong and trusted name in secondary and higher secondary education." },
  { role: "Headmistress", name: "Debosree Sarker", photo: "https://i.pravatar.cc/200?img=47", msg: "South Point stands as a benchmark for excellence in secondary and higher secondary education in our country." },
];

export const ALUMNI = [
  { name: "Ashfia Khan Tuski", admitted: "Sahabuddin Medical College", year: "2024", photo: "https://i.pravatar.cc/150?img=20" },
  { name: "Mumtazah Nawar", admitted: "University of Dhaka", year: "2024", photo: "https://i.pravatar.cc/150?img=24" },
  { name: "Arufa Rifaat", admitted: "KUET — Engineering", year: "2024", photo: "https://i.pravatar.cc/150?img=16" },
  { name: "Nabila Hossen Naba", admitted: "Sir Salimullah Medical College", year: "2024", photo: "https://i.pravatar.cc/150?img=29" },
  { name: "Afrah Tasnim", admitted: "Mugda Medical College", year: "2024", photo: "https://i.pravatar.cc/150?img=5" },
  { name: "Nur-E-Sabah", admitted: "Shaheed Tajuddin Ahmed Medical College", year: "2024", photo: "https://i.pravatar.cc/150?img=32" },
];

export const EVENTS = [
  { id: 1, title: "A Proud Achievement of Our Young Debaters!", body: "Our debate team brought home honours from a recent inter-school competition.", event_date: "2026-08-28T10:00:00", category: "General", img: "https://images.unsplash.com/photo-1475721027785-f74eccf877e2?auto=format&fit=crop&w=800&q=70" },
  { id: 2, title: "বাংলা নববর্ষ ১৪৩৩ উপলক্ষে বর্ষবরণ অনুষ্ঠান", body: "A vibrant celebration of the Bengali New Year 1433 with music, colour and tradition.", event_date: "2026-04-14T09:00:00", category: "Cultural", img: "https://images.unsplash.com/photo-1511578314322-379afb476865?auto=format&fit=crop&w=800&q=70" },
  { id: 3, title: "আন্তর্জাতিক মাতৃভাষা ও শহীদ দিবস উদযাপন", body: "Observance of International Mother Language Day and Martyrs' Day with due solemnity.", event_date: "2026-02-21T08:00:00", category: "Cultural", img: "https://images.unsplash.com/photo-1524178232363-1fb2b075b655?auto=format&fit=crop&w=800&q=70" },
  { id: 4, title: "Inter Class Football Tournament 2025", body: "Students competed in an energetic inter-class football tournament.", event_date: "2025-07-10T09:00:00", category: "Sports", img: "https://images.unsplash.com/photo-1461896836934-ffe607ba8211?auto=format&fit=crop&w=800&q=70" },
];

// At South Point these are the academic streams offered at secondary & higher secondary level.
export const FACULTIES = [
  { id: 1, slug: "science", name: "Science Group", short_desc: "Physics, Chemistry, Biology & Higher Mathematics", head_name: "Head of Science", icon: "🔬", description: "The Science group prepares students for medical, engineering and university admission with fully-equipped physics, chemistry and biology laboratories." },
  { id: 2, slug: "business-studies", name: "Business Studies Group", short_desc: "Accounting, Finance, Business Entrepreneurship & Economics", head_name: "Head of Business Studies", icon: "📊", description: "The Business Studies group builds strong foundations in accounting, management and economics for future business leaders." },
  { id: 3, slug: "humanities", name: "Humanities Group", short_desc: "Bengali, English, Civics, Geography & History", head_name: "Head of Humanities", icon: "📚", description: "The Humanities group develops critical thinking, language skills and social awareness." },
  { id: 4, slug: "primary", name: "Primary & Junior Section", short_desc: "Nursery to Class VIII — foundation years", head_name: "Headmistress", icon: "🧒", description: "Our primary and junior section nurtures young learners with care, discipline and a strong academic foundation." },
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

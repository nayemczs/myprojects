from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Role(models.TextChoices):
        PRINCIPAL = "PRINCIPAL", "Principal"
        ADMIN = "ADMIN", "Administrator"
        TEACHER = "TEACHER", "Teacher"
        STUDENT = "STUDENT", "Student"

    role = models.CharField(max_length=20, choices=Role.choices, default=Role.STUDENT)
    # Students self-register and must be approved by an admin/principal.
    is_approved = models.BooleanField(default=False)
    phone = models.CharField(max_length=20, blank=True)

    def save(self, *args, **kwargs):
        # Staff roles are auto-approved; students require approval.
        if self.role in {self.Role.PRINCIPAL, self.Role.ADMIN, self.Role.TEACHER}:
            self.is_approved = True
        super().save(*args, **kwargs)


# ---------- Public website content ----------

class Faculty(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    short_desc = models.CharField(max_length=300, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="faculties/", blank=True, null=True)
    head_name = models.CharField(max_length=120, blank=True)

    class Meta:
        verbose_name_plural = "Faculties"

    def __str__(self):
        return self.name


class Post(models.Model):
    class Kind(models.TextChoices):
        POST = "POST", "Post"
        NOTICE = "NOTICE", "Notice"
        EVENT = "EVENT", "Event"

    kind = models.CharField(max_length=10, choices=Kind.choices, default=Kind.POST)
    title = models.CharField(max_length=200)
    body = models.TextField()
    image = models.ImageField(upload_to="posts/", blank=True, null=True)
    event_date = models.DateTimeField(blank=True, null=True)  # for events
    published = models.BooleanField(default=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="posts")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"[{self.kind}] {self.title}"


class AboutPage(models.Model):
    """Singleton-ish content for the About page."""
    heading = models.CharField(max_length=200, default="About Us")
    body = models.TextField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)


# ---------- Academic structure ----------

class ClassRoom(models.Model):
    name = models.CharField(max_length=80)        # e.g. "Class 10"
    section = models.CharField(max_length=10, blank=True)  # e.g. "A"

    class Meta:
        unique_together = ("name", "section")

    def __str__(self):
        return f"{self.name} {self.section}".strip()


class Subject(models.Model):
    name = models.CharField(max_length=80)
    classroom = models.ForeignKey(ClassRoom, on_delete=models.CASCADE, related_name="subjects")
    teacher = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True,
        related_name="subjects", limit_choices_to={"role": "TEACHER"},
    )

    class Meta:
        unique_together = ("name", "classroom")

    def __str__(self):
        return f"{self.name} - {self.classroom}"


class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="student_profile")
    classroom = models.ForeignKey(ClassRoom, on_delete=models.SET_NULL, null=True, related_name="students")
    roll = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return f"{self.user.get_full_name() or self.user.username} ({self.classroom})"


# ---------- Subject groups (per subject, with teacher + students) ----------

class SubjectGroup(models.Model):
    subject = models.OneToOneField(Subject, on_delete=models.CASCADE, related_name="group")
    members = models.ManyToManyField(StudentProfile, related_name="groups", blank=True)

    def __str__(self):
        return f"Group: {self.subject}"


class GroupMessage(models.Model):
    group = models.ForeignKey(SubjectGroup, on_delete=models.CASCADE, related_name="messages")
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_at"]


# ---------- Exams & marks (teacher submits -> admin approves) ----------

class Exam(models.Model):
    name = models.CharField(max_length=80)  # e.g. "Half Yearly 2026"
    classroom = models.ForeignKey(ClassRoom, on_delete=models.CASCADE, related_name="exams")
    total_marks = models.PositiveIntegerField(default=100)

    def __str__(self):
        return f"{self.name} - {self.classroom}"


class Mark(models.Model):
    class Status(models.TextChoices):
        PENDING = "PENDING", "Pending approval"
        APPROVED = "APPROVED", "Approved"
        REJECTED = "REJECTED", "Rejected"

    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name="marks")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="marks")
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, related_name="marks")
    score = models.DecimalField(max_digits=6, decimal_places=2)
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.PENDING)
    submitted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="submitted_marks")
    approved_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="approved_marks")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("exam", "subject", "student")

    def __str__(self):
        return f"{self.student} / {self.subject} = {self.score} [{self.status}]"


# ---------- Assignments ----------

class Assignment(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="assignments")
    classroom = models.ForeignKey(ClassRoom, on_delete=models.CASCADE, related_name="assignments")
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    attachment = models.FileField(upload_to="assignments/", blank=True, null=True)
    due_date = models.DateTimeField()
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="created_assignments")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class Submission(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name="submissions")
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, related_name="submissions")
    file = models.FileField(upload_to="submissions/")
    note = models.TextField(blank=True)
    grade = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("assignment", "student")

    def __str__(self):
        return f"{self.student} -> {self.assignment}"

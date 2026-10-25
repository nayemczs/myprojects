from django.core.management.base import BaseCommand
from core.models import (
    User, ClassRoom, Subject, StudentProfile, Exam, Faculty, SubjectGroup,
)


class Command(BaseCommand):
    help = "Seed demo data (principal, admin, teacher, student, classes)"

    def handle(self, *args, **kwargs):
        def mkuser(username, role, **extra):
            u, created = User.objects.get_or_create(username=username, defaults={"role": role, **extra})
            if created:
                u.set_password("password123")
                u.role = role
                u.save()
                self.stdout.write(f"created {role}: {username} / password123")
            return u

        principal = mkuser("principal", User.Role.PRINCIPAL, first_name="The", last_name="Principal")
        admin = mkuser("admin1", User.Role.ADMIN)
        teacher = mkuser("teacher_physics", User.Role.TEACHER, first_name="Physics", last_name="Teacher")

        c10, _ = ClassRoom.objects.get_or_create(name="Class 10", section="A")
        physics, _ = Subject.objects.get_or_create(name="Physics", classroom=c10, defaults={"teacher": teacher})
        if physics.teacher is None:
            physics.teacher = teacher
            physics.save()

        Exam.objects.get_or_create(name="Half Yearly 2026", classroom=c10, total_marks=100)

        student = mkuser("student1", User.Role.STUDENT, first_name="Sample", last_name="Student")
        student.is_approved = True
        student.save()
        profile, _ = StudentProfile.objects.get_or_create(user=student, defaults={"classroom": c10, "roll": "01"})

        # put the demo student into the physics subject group
        group, _ = SubjectGroup.objects.get_or_create(subject=physics)
        group.members.add(profile)

        Faculty.objects.get_or_create(slug="science", defaults={
            "name": "Faculty of Science", "short_desc": "Physics, Chemistry, Biology, Math"})

        self.stdout.write(self.style.SUCCESS("Seed complete."))

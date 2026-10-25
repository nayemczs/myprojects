from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import (
    User, Faculty, Post, AboutPage, ClassRoom, Subject, StudentProfile,
    SubjectGroup, Exam, Mark, Assignment, Submission,
)


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ("username", "email", "role", "is_approved", "is_staff")
    list_filter = ("role", "is_approved")
    fieldsets = UserAdmin.fieldsets + (
        ("Role & approval", {"fields": ("role", "is_approved", "phone")}),
    )


admin.site.register([Faculty, Post, AboutPage, ClassRoom, Subject,
                     StudentProfile, SubjectGroup, Exam, Mark,
                     Assignment, Submission])

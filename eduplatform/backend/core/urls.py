from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView
from . import views

router = DefaultRouter()
router.register("users", views.UserAdminViewSet, basename="users")
router.register("faculties", views.FacultyViewSet, basename="faculties")
router.register("posts", views.PostViewSet, basename="posts")
router.register("about", views.AboutPageViewSet, basename="about")
router.register("classrooms", views.ClassRoomViewSet, basename="classrooms")
router.register("subjects", views.SubjectViewSet, basename="subjects")
router.register("students", views.StudentProfileViewSet, basename="students")
router.register("groups", views.SubjectGroupViewSet, basename="groups")
router.register("exams", views.ExamViewSet, basename="exams")
router.register("marks", views.MarkViewSet, basename="marks")
router.register("assignments", views.AssignmentViewSet, basename="assignments")
router.register("submissions", views.SubmissionViewSet, basename="submissions")

urlpatterns = [
    path("auth/login/", views.MyTokenObtainPairView.as_view()),
    path("auth/refresh/", TokenRefreshView.as_view()),
    path("auth/register/", views.RegisterView.as_view()),
    path("auth/me/", views.MeView.as_view()),
    path("", include(router.urls)),
]

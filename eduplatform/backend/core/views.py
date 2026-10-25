from rest_framework import viewsets, generics
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import (
    User, Faculty, Post, AboutPage, ClassRoom, Subject, StudentProfile,
    SubjectGroup, Exam, Mark, Assignment, Submission,
)
from .serializers import (
    UserSerializer, RegisterSerializer, MyTokenObtainPairSerializer,
    FacultySerializer, PostSerializer, AboutPageSerializer, ClassRoomSerializer,
    SubjectSerializer, StudentProfileSerializer, SubjectGroupSerializer,
    GroupMessageSerializer, ExamSerializer, MarkSerializer,
    AssignmentSerializer, SubmissionSerializer,
)
from .permissions import (
    IsPrincipal, IsAdminOrPrincipal, IsTeacher, ReadOnlyOrStaff,
)


# ---------- Auth ----------

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


class MeView(generics.RetrieveAPIView):
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


# ---------- User management (principal adds admins; staff approve students) ----------

class UserAdminViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("-id")
    serializer_class = UserSerializer
    permission_classes = [IsAdminOrPrincipal]

    def get_queryset(self):
        qs = super().get_queryset()
        role = self.request.query_params.get("role")
        approved = self.request.query_params.get("approved")
        if role:
            qs = qs.filter(role=role.upper())
        if approved is not None:
            qs = qs.filter(is_approved=approved == "true")
        return qs

    @action(detail=True, methods=["post"])
    def approve(self, request, pk=None):
        user = self.get_object()
        user.is_approved = True
        user.save()
        return Response({"status": "approved"})

    @action(detail=False, methods=["post"], permission_classes=[IsPrincipal])
    def create_admin(self, request):
        """Only the principal can mint new administrators."""
        data = request.data
        if User.objects.filter(username=data.get("username")).exists():
            return Response({"error": "username taken"}, status=400)
        u = User(
            username=data["username"], email=data.get("email", ""),
            first_name=data.get("first_name", ""), role=User.Role.ADMIN,
        )
        u.set_password(data["password"])
        u.save()
        return Response(UserSerializer(u).data, status=201)


# ---------- Public content ----------

class FacultyViewSet(viewsets.ModelViewSet):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer
    permission_classes = [ReadOnlyOrStaff]
    lookup_field = "slug"


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    permission_classes = [ReadOnlyOrStaff]

    def get_queryset(self):
        qs = Post.objects.all()
        kind = self.request.query_params.get("kind")
        if kind:
            qs = qs.filter(kind=kind.upper())
        return qs

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class AboutPageViewSet(viewsets.ModelViewSet):
    queryset = AboutPage.objects.all()
    serializer_class = AboutPageSerializer
    permission_classes = [ReadOnlyOrStaff]


# ---------- Academic structure ----------

class ClassRoomViewSet(viewsets.ModelViewSet):
    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomSerializer

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [AllowAny()]
        return [IsAdminOrPrincipal()]


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        classroom = self.request.query_params.get("classroom")
        if classroom:
            qs = qs.filter(classroom_id=classroom)
        # Teachers only see their own subjects in their portal
        if self.request.user.is_authenticated and self.request.user.role == "TEACHER":
            mine = self.request.query_params.get("mine")
            if mine == "true":
                qs = qs.filter(teacher=self.request.user)
        return qs

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [AllowAny()]
        return [IsAdminOrPrincipal()]


class StudentProfileViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = StudentProfile.objects.select_related("user", "classroom")
    serializer_class = StudentProfileSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        classroom = self.request.query_params.get("classroom")
        if classroom:
            qs = qs.filter(classroom_id=classroom)
        return qs


# ---------- Subject groups ----------

class SubjectGroupViewSet(viewsets.ModelViewSet):
    queryset = SubjectGroup.objects.all()
    serializer_class = SubjectGroupSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        user = self.request.user
        # Students only see groups they belong to
        if user.is_authenticated and user.role == "STUDENT":
            profile = getattr(user, "student_profile", None)
            if profile:
                return qs.filter(members=profile)
            return qs.none()
        return qs

    @action(detail=True, methods=["get", "post"])
    def messages(self, request, pk=None):
        group = self.get_object()
        if request.method == "POST":
            ser = GroupMessageSerializer(data=request.data)
            ser.is_valid(raise_exception=True)
            ser.save(sender=request.user, group=group)
            return Response(ser.data, status=201)
        msgs = group.messages.select_related("sender")
        return Response(GroupMessageSerializer(msgs, many=True).data)


# ---------- Exams & marks ----------

class ExamViewSet(viewsets.ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [AllowAny()]
        return [IsAdminOrPrincipal()]


class MarkViewSet(viewsets.ModelViewSet):
    serializer_class = MarkSerializer

    def get_queryset(self):
        user = self.request.user
        qs = Mark.objects.select_related("student__user", "subject", "exam")
        if user.role == "STUDENT":
            # students see only their own APPROVED marks
            return qs.filter(student__user=user, status="APPROVED")
        if user.role == "TEACHER":
            return qs.filter(subject__teacher=user)
        return qs  # staff see all

    def perform_create(self, serializer):
        # teacher-submitted marks start as pending
        serializer.save(submitted_by=self.request.user, status="PENDING")

    @action(detail=False, methods=["post"], permission_classes=[IsTeacher])
    def bulk_submit(self, request):
        """Teacher submits many marks at once for one exam+subject."""
        exam_id = request.data.get("exam")
        subject_id = request.data.get("subject")
        entries = request.data.get("marks", [])  # [{student, score}, ...]
        subject = Subject.objects.filter(id=subject_id, teacher=request.user).first()
        if not subject:
            return Response({"error": "Not your subject"}, status=403)
        created = []
        for e in entries:
            mark, _ = Mark.objects.update_or_create(
                exam_id=exam_id, subject_id=subject_id, student_id=e["student"],
                defaults={"score": e["score"], "status": "PENDING",
                          "submitted_by": request.user},
            )
            created.append(mark.id)
        return Response({"submitted": len(created)}, status=201)

    @action(detail=True, methods=["post"], permission_classes=[IsAdminOrPrincipal])
    def approve(self, request, pk=None):
        mark = self.get_object()
        mark.status = "APPROVED"
        mark.approved_by = request.user
        mark.save()
        return Response(MarkSerializer(mark).data)

    @action(detail=True, methods=["post"], permission_classes=[IsAdminOrPrincipal])
    def reject(self, request, pk=None):
        mark = self.get_object()
        mark.status = "REJECTED"
        mark.approved_by = request.user
        mark.save()
        return Response(MarkSerializer(mark).data)


# ---------- Assignments & submissions ----------

class AssignmentViewSet(viewsets.ModelViewSet):
    serializer_class = AssignmentSerializer

    def get_queryset(self):
        user = self.request.user
        qs = Assignment.objects.select_related("subject", "classroom")
        if user.role == "STUDENT":
            profile = getattr(user, "student_profile", None)
            if profile and profile.classroom:
                return qs.filter(classroom=profile.classroom)
            return qs.none()
        if user.role == "TEACHER":
            return qs.filter(subject__teacher=user)
        return qs

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsTeacher()]
        return [IsAuthenticated()]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    @action(detail=True, methods=["get", "post"])
    def submissions(self, request, pk=None):
        assignment = self.get_object()
        if request.method == "POST":
            profile = getattr(request.user, "student_profile", None)
            if not profile:
                return Response({"error": "Not a student"}, status=403)
            ser = SubmissionSerializer(data=request.data)
            ser.is_valid(raise_exception=True)
            ser.save(student=profile, assignment=assignment)
            return Response(ser.data, status=201)
        subs = assignment.submissions.select_related("student__user")
        return Response(SubmissionSerializer(subs, many=True).data)


class SubmissionViewSet(viewsets.ModelViewSet):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer

    @action(detail=True, methods=["post"], permission_classes=[IsTeacher])
    def grade(self, request, pk=None):
        sub = self.get_object()
        sub.grade = request.data.get("grade")
        sub.save()
        return Response(SubmissionSerializer(sub).data)

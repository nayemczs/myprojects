from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import (
    User, Faculty, Post, AboutPage, ClassRoom, Subject, StudentProfile,
    SubjectGroup, GroupMessage, Exam, Mark, Assignment, Submission,
)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "first_name", "last_name",
                  "role", "is_approved", "phone"]
        read_only_fields = ["is_approved"]


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)
    classroom = serializers.PrimaryKeyRelatedField(
        queryset=ClassRoom.objects.all(), required=False, allow_null=True
    )

    class Meta:
        model = User
        fields = ["username", "email", "password", "first_name",
                  "last_name", "phone", "classroom"]

    def create(self, validated_data):
        classroom = validated_data.pop("classroom", None)
        password = validated_data.pop("password")
        user = User(role=User.Role.STUDENT, **validated_data)
        user.set_password(password)
        user.is_approved = False  # students await approval
        user.save()
        StudentProfile.objects.create(user=user, classroom=classroom)
        return user


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["role"] = user.role
        token["username"] = user.username
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        if not self.user.is_approved:
            raise serializers.ValidationError("Account pending admin approval.")
        data["user"] = UserSerializer(self.user).data
        return data


class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source="author.username", read_only=True)

    class Meta:
        model = Post
        fields = "__all__"
        read_only_fields = ["author"]


class AboutPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutPage
        fields = "__all__"


class ClassRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassRoom
        fields = "__all__"


class SubjectSerializer(serializers.ModelSerializer):
    teacher_name = serializers.CharField(source="teacher.username", read_only=True)
    classroom_name = serializers.CharField(source="classroom.__str__", read_only=True)

    class Meta:
        model = Subject
        fields = "__all__"


class StudentProfileSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source="user.get_full_name", read_only=True)
    username = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = StudentProfile
        fields = ["id", "name", "username", "classroom", "roll"]


class GroupMessageSerializer(serializers.ModelSerializer):
    sender_name = serializers.CharField(source="sender.username", read_only=True)

    class Meta:
        model = GroupMessage
        fields = ["id", "group", "sender", "sender_name", "text", "created_at"]
        read_only_fields = ["sender"]


class SubjectGroupSerializer(serializers.ModelSerializer):
    subject_name = serializers.CharField(source="subject.name", read_only=True)

    class Meta:
        model = SubjectGroup
        fields = ["id", "subject", "subject_name", "members"]


class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = "__all__"


class MarkSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source="student.user.get_full_name", read_only=True)
    subject_name = serializers.CharField(source="subject.name", read_only=True)
    exam_name = serializers.CharField(source="exam.name", read_only=True)

    class Meta:
        model = Mark
        fields = "__all__"
        read_only_fields = ["status", "submitted_by", "approved_by"]


class AssignmentSerializer(serializers.ModelSerializer):
    subject_name = serializers.CharField(source="subject.name", read_only=True)

    class Meta:
        model = Assignment
        fields = "__all__"
        read_only_fields = ["created_by"]


class SubmissionSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source="student.user.get_full_name", read_only=True)

    class Meta:
        model = Submission
        fields = "__all__"
        read_only_fields = ["student", "grade"]

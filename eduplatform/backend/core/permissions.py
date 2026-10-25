from rest_framework.permissions import BasePermission, SAFE_METHODS

STAFF_ROLES = {"PRINCIPAL", "ADMIN"}


class IsPrincipal(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated
                    and request.user.role == "PRINCIPAL")


class IsAdminOrPrincipal(BasePermission):
    """Manages website content and approves marks/students."""
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated
                    and request.user.role in STAFF_ROLES)


class IsTeacher(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated
                    and request.user.role == "TEACHER")


class IsStudent(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated
                    and request.user.role == "STUDENT")


class ReadOnlyOrStaff(BasePermission):
    """Anyone can read; only admin/principal can write. Used for public content."""
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_authenticated
                    and request.user.role in STAFF_ROLES)

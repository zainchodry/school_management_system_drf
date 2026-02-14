from rest_framework.permissions import BasePermission

class IsAdminOrTeacher(BasePermission):
    def has_permission(self, request, view):
        return request.user.role in ["ADMIN","TEACHER"]

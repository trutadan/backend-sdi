from rest_framework import permissions

from api.models.user import User

class IsModeratorOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.user.role in [User.Role.MODERATOR, User.Role.ADMIN]:
                return True
        return False
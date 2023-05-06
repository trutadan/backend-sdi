from rest_framework import permissions

from api.models.user import User

class IsAdminOrModerator(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if (user.role == User.Role.ADMIN or user.is_superuser == True) or (user.role == User.Role.MODERATOR or user.is_staff == True):
            return True

        return False


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return user.role == User.Role.ADMIN or user.is_superuser == True
    

class IsModeratorWithNoDeletePrivilege(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return user.role == User.Role.MODERATOR or user.is_staff == True
    
    def has_object_permission(self, request, view, obj):
        # Moderators are not allowed to delete
        if request.method == 'DELETE':
            return False
        
        return True


class UserIsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj == request.user
    

class UserProfileIsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj == request.user.profile
    
    
class UserAddressIsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj == request.user.address
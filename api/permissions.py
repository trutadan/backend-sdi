from rest_framework import permissions

from api.models.user import User

# Role permissions
class IsAdminOrModerator(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if (user.role == User.Role.ADMIN or user.is_superuser) or (user.role == User.Role.MODERATOR or user.is_staff):
            return True

        return False


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return user.role == User.Role.ADMIN or user.is_superuser
    

class IsModeratorWithNoDeletePrivilege(permissions.BasePermission):
    def has_permission(self, request, view):        
        if request.method == 'DELETE':
            return False
        
        user = request.user
        return user.role == User.Role.MODERATOR or user.is_staff


# Object permissions
class IsUserCartItemOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.cart.user == request.user
    

class GetIfUserIsCartOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method == 'GET'
    
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
    

class IsUserOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj == request.user
    

class IsUserProfileOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj == request.user.profile
    
    
class IsUserAddressOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj == request.user.address
    

class IsUserOrderItemOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.order.user == request.user


class GetIfUserIsOrderOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method == 'GET'
    
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class GetIfUserIsPaymentOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method == 'GET'
    
    def has_object_permission(self, request, view, obj):
        return obj.order.user == request.user


class IsUserRefundOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.order.user == request.user


# Request permissions
class IsGetRequest(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method == 'GET'
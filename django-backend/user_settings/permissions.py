from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied
import rest_framework

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow creator of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the creator of the movie
        return obj.creator == request.user

class IsOwner(permissions.BasePermission):
    """
    Custom permission to only allow creator of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Permissions are only allowed to the creator
        return obj.creator == request.user

class IsAuthenticated(permissions.BasePermission):
    """
    Allows access only to authenticated users.
    """
    def has_permission(self, request, view):
        message = 'You must be authenticated'
        is_it = bool(request.user and request.user.is_authenticated)
        if is_it:
            return is_it
        else:
            raise PermissionDenied(detail=message)

class AdminAuthenticationPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.is_superuser

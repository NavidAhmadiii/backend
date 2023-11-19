from rest_framework import permissions
from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)


class IsStaffOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_staff
        )


class IsAuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in SAFE_METHODS:
            return True

        return bool(
            # get access to superuser
            request.user.is_authenticated and
            request.user.is_superuser or
            # get access to  author or object
            obj.author == request.user

        )


class IsSuperUserOrStaffOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS and request.user.is_authenticated and request.user.is_staff:
            return True

        return bool(
            request.user.is_superuser
        )

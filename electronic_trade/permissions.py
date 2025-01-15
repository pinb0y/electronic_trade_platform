from rest_framework import permissions


class ActiveUserPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if not request.user.is_active:
            return False
        return True

from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # authenticated users only can see list view
        if request.user.is_authenticated:
            return True
        # return True
        return False

    def has_object_permission(self, request, view, obj):
        # read permissions are allowed to any request so we'll allways allow GET, HEAD or OPTIONS requests
        if request.method in permissions.SAFE_METHODS:
            return False

        # writer permissions are only allowed to the author of post

        return obj.user == request.user

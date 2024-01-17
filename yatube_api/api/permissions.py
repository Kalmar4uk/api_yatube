from rest_framework import permissions

REQUEST_METHOD = [
    'PATCH',
    'PUT',
    'DELETE'
]


class AuthorOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.method in REQUEST_METHOD:
            if obj.author == request.user:
                return True
            return False
        return True

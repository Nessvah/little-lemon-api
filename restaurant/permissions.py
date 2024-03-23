from rest_framework.permissions import BasePermission, IsAuthenticated


class IsOwnerOrAdmin(BasePermission):
    """
    Custom permission to only allow owners of the object
    to edit it or view it.
    """

    def has_permission(self, request, view):
        # allow read and write access only for authenticated users
        if request.user.is_authenticated and request.method in ['GET', 'HEAD', 'OPTIONS', 'POST']:
            return True
        if request.user.is_staff:
            # allow all actions for admins
            return True
        # everyone else doesnt have access
        return False

    def has_object_permission(self, request, view, obj):
        # Admin or staff can view any object
        if request.user and request.user.is_authenticated:
            return request.user.is_staff or request.user.is_superuser
        # Otherwise, only the owner can view the object
        return obj.user == request.user
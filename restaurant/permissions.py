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
        # allow only read and write access only to the owner of the booking
        # or the admins
        if request.method in ['GET', 'HEAD', 'OPTIONS'] and (obj.user == request.user or request.user.is_staff):
            return True
        if request.method in ['POST', 'PUT', 'DELETE'] and (obj.user == request.user or request.user.is_staff):
            return True
        return False
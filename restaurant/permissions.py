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
        # everyone else doesn't have access
        return False

    def has_object_permission(self, request, view, obj):
        # Print the user and object details for debugging
        print(f"User: {request.user}")
        print(f"Object User: {obj.user}")
        # Admin or staff can view any object
        if request.user and request.user.is_authenticated:
            return request.user.is_staff or request.user.is_superuser
        # Otherwise, only the owner can view the object
        return obj.user == request.user


class IsAdminOrStaffOrOwner(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Admin or staff can perform any action
        if request.user.is_staff or request.user.is_superuser:
            return True
        # Otherwise, only the owner can perform actions on the object
        return obj.user == request.user

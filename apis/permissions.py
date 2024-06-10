# permissions.py
from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAuthenticatedOrReadOnly(BasePermission):
    """
    Custom permission to allow read-only access to any request,
    but write access to authenticated users only.
    """

    def has_permission(self, request, view):
        # Allow read-only methods for any request (GET, HEAD, OPTIONS)
        if request.method in SAFE_METHODS:
            return True
        # Allow write methods for authenticated users only
        return request.user and request.user.is_authenticated

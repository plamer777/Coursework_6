"""This file contains permissions to restrict access rights for users"""
from rest_framework.permissions import BasePermission
from users.models import UserRoles
# ------------------------------------------------------------------------


class UpdateDeleteAdPermission(BasePermission):
    """This permission is used to restrict access to update or delete
    advertisement"""
    message = 'Only owner can update or delete this advertisement'

    def has_permission(self, request, view):
        """Returns True only if the user is the owner of the advertisement"""
        if request.user.pk != view.get_object().author.id:
            return False

        return True


class UpdateDeleteCommentPermission(BasePermission):
    """This permission is used to restrict access to update or delete
    comments"""
    message = 'Only owner can update or delete this comment'

    def has_permission(self, request, view):
        """Returns True only if the user is the owner of the comment"""
        if request.user.pk != view.get_object().author.id:
            return False

        return True


class AdminPermission(BasePermission):
    """This permission is to get extended access for users having admin role"""
    def has_permission(self, request, view):
        if (getattr(request.user, 'role', None)
                and request.user.role == UserRoles.ADMIN):
            return True

        return False

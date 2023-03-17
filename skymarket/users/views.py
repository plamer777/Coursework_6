"""This file contains a DjoserUserViewSet class inherited from original Djoser
ViewSet to implement swagger documentation"""
from djoser.views import UserViewSet
from drf_spectacular.utils import extend_schema_view, extend_schema
from django.utils.translation import gettext_lazy as _
# ------------------------------------------------------------------------


@extend_schema_view(
    list=extend_schema(
        description=_(
            'Returns a list of all users'),
        summary=_('A list of users')
    ),
    retrieve=extend_schema(description=_(
        'Returns a detail user'),
                           summary=_('A detail user')
                           ),
    create=extend_schema(description=_(
        'Adds a new user to the database'),
                           summary=_('Add user')
                           ),
    update=extend_schema(description=_(
        'Updates all fields of the certain user'),
                           summary=_('Update user')
                           ),
    partial_update=extend_schema(description=_(
        'Updates chosen fields of the certain user'),
                           summary=_('Partially update user')
                           ),
    destroy=extend_schema(description=_(
        'Deletes the user from the database'),
                           summary=_('Delete user')
                           ),
    me=extend_schema(
        description=_(
            'Allows current user to get a detail info of his profile, change '
            'or delete it'),
        summary=_('Current user'),
    ),
    activation=extend_schema(description=_(
        'Activates account of the user'),
        summary=_('Account activation')
                             ),
    resend_activation=extend_schema(description=_(
        'Sends one more activation request to the user'),
        summary=_('Resend activation request')
    ),
    reset_password=extend_schema(description=_(
        'Sends a request to reset the password'),
        summary=_('Reset password request')
    ),
    reset_password_confirm=extend_schema(description=_(
        'Confirmation of reset password request'),
        summary=_('Reset password confirmation')
    ),
    set_password=extend_schema(description=_(
        'Allows user to set a new password'),
        summary=_('Change password')
    ),
    set_username=extend_schema(description=_(
        'Allows user to set a new username'),
        summary=_('Change username')
    ),
    reset_username=extend_schema(description=_(
        'Allows user to get a request to reset his username'),
        summary=_('Reset username request')
    ),
    reset_username_confirm=extend_schema(description=_(
        'Confirmation of reset username request'),
        summary=_('Reset username confirmation')
    ),
)
class DjoserUserViewSet(UserViewSet):
    """DjoserUserViewSet inherited from UserViewSet supplemented by
    documentation"""
    pass

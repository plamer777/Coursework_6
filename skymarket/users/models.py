"""This file contains a User model inherited from AbstractBaseUser to be
able to work with djoser"""
from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from users.managers import UserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _
# -------------------------------------------------------------------------


class UserRoles:
    """UserRoles class stores user's roles using in the model"""
    ADMIN = 'admin'
    USER = 'user'


class User(AbstractBaseUser):
    """User class to work with djoser"""
    class Roles(models.TextChoices):
        """Roles class serves to provide only two types of roles available
        for users"""
        ADMIN = 'admin', _('Admin')
        USER = 'user', _('User')

    email = models.EmailField(
        null=False,
        blank=False,
        max_length=30,
        help_text=_('This field is used to register and log-in'),
        unique=True
    )
    first_name = models.CharField(
        max_length=30,
        help_text=_('First name of user')
    )
    last_name = models.CharField(
        max_length=30,
        help_text=_('Last name of user')
    )
    phone = PhoneNumberField(
        max_length=20,
        region='RU',
        help_text=_('Your phone number')
    )
    role = models.CharField(
        max_length=5,
        choices=Roles.choices,
        default=Roles.USER,
        help_text=_('Role of user')
    )
    image = models.ImageField(
        upload_to='ava/',
        help_text=_('Path to an avatar to upload'),
        null=True,
        blank=True
    )
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'first_name',
        'last_name',
        'phone',
        'role',
        ]

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN

    @property
    def is_user(self):
        return self.role == UserRoles.USER

    def has_perm(self,  perm, obj=None):
        return self.is_admin

    def has_module_perm(self, app_label):
        return self.is_admin

    objects = UserManager()

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

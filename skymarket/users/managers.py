"""This file contains UserManager class adapted for work with djoser"""
from django.contrib.auth.models import (
    BaseUserManager
)
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
# -------------------------------------------------------------------------


class UserManager(BaseUserManager):
    """UserManager class realization to work with djoser"""
    def create_user(self, email: str, first_name: str, last_name: str,
                    phone: str, password: str = None, **kwargs):
        """This method creates a new user with common rules
        :param email: The string representing email address used instead
        of username
        :param first_name: The string representing first name
        :param last_name: The string representing last name
        :param phone: The string representing phone number
        :param password: The string representing password
        :param kwargs: Additional keyword arguments
        :return: User object
        """
        if not email:
            raise ValidationError(_('Email is required'))

        return self._save_user_data(email, first_name, last_name, phone,
                                    password, 'user')

    def create_superuser(self, email: str, first_name: str, last_name: str,
                         phone: str, password: str = '', **kwargs):
        """This method creates a new superuser with admin rules
        :param email: The string representing email address used instead
        of username
        :param first_name: The string representing first name
        :param last_name: The string representing last name
        :param phone: The string representing phone number
        :param password: The string representing password
        :param kwargs: Additional keyword arguments
        :return: User object
        """
        if not email:
            raise ValidationError(_('Email is required'))

        return self._save_user_data(email, first_name, last_name, phone,
                                    password, 'admin')

    def _save_user_data(self, email: str, first_name: str, last_name: str,
                         phone: str, password: str = '', role: str = 'user',
                        **kwargs):

        user = self.model(email=email,
                          first_name=first_name,
                          last_name=last_name,
                          phone=phone,
                          role=role)

        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)

        return user

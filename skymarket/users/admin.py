"""This file serves to register models to be available from admin panel"""
from django.contrib import admin
from users.models import User
# -------------------------------------------------------------------------

admin.site.register(User)

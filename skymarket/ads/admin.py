"""This file serves to register models to be available from admin panel"""
from django.contrib import admin
from ads.models import Ad, Comment
# --------------------------------------------------------------------------

admin.site.register(Ad)
admin.site.register(Comment)
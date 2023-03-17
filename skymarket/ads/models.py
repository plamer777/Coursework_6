"""This unit contains Ad and Comment models"""
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from users.models import User
# -------------------------------------------------------------------------


class Ad(models.Model):
    """Ad model representing advertisement"""
    title = models.CharField(
        max_length=200, help_text=_('Enter a title here'),
    )
    price = models.PositiveIntegerField(
        help_text=_('Enter your price here')
    )
    image = models.ImageField(
        upload_to='images/',
        help_text=_('Upload a photo for this ad'),
        null=True,
        blank=True
    )
    description = models.CharField(
        max_length=1000,
        help_text=_('Write your description here')
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        help_text=_('This field stores the author id')
    )
    created_at = models.DateTimeField(
        auto_now_add=False,
        default=timezone.now,
        help_text=_('The date this ad was created')
    )

    class Meta:
        verbose_name = _('Advertisement')
        verbose_name_plural = _('Advertisements')

    def __str__(self):
        return self.title


class Comment(models.Model):
    """Comment model representing comment"""
    text = models.CharField(
        max_length=1000,
        help_text=_('Enter a comment here')
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        help_text=_('This field stores the author id')
    )
    ad = models.ForeignKey(
        Ad,
        on_delete=models.CASCADE,
        help_text=_('This field stores the ad id')
    )
    created_at = models.DateTimeField(
        default=timezone.now,
        help_text=_('The date this comment was created')
    )

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")

    def __str__(self):
        return self.text

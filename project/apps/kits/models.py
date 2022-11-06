from django.db import models
from django.utils.translation import gettext_lazy as _


class Kit(models.Model):
    class KitType(models.IntegerChoices):
        HOME = 0, _("Home")
        CAR = 1, _("Car")
        OFFICE = 2, _("Office")

    owner = models.ForeignKey(
        'users.User',
        verbose_name=_('Owner'),
        related_name='kits',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    name = models.CharField(
        verbose_name=_('Kit name'),
        max_length=30
    )
    type = models.PositiveSmallIntegerField(
        verbose_name=_('Type'),
        choices=KitType.choices,
    )

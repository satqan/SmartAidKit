from django.db import models
from django.utils.translation import gettext_lazy as _


class Drug(models.Model):
    class DrugType(models.IntegerChoices):
        SALVE = 0, _("Salve")
        DROP = 1, _("Drop")
        CAPSULE = 2, _("Capsule")
        PILL = 3, _("Pill")

    kit = models.ForeignKey(
        'kits.Kit',
        verbose_name=_('Kit'),
        related_name='drugs',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    amount = models.IntegerField(
        verbose_name=_('Amount'),
    )
    expire_date = models.DateTimeField(
        verbose_name=_('Expire date'),
    )
    type = models.PositiveSmallIntegerField(
        verbose_name=_('Type'),
        choices=DrugType.choices,
    )
    description = models.CharField(
        verbose_name=_('Char Field'),
        max_length=300,
        blank=True,
    )

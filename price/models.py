from django.db import models
from django.utils.translation import gettext_lazy as _


class WorkType(models.Model):
    title = models.CharField(max_length=255)
    product_is_required = models.BooleanField(default=False)


class ActionType(models.Model):
    UNITS = {
        "PCS": _("Pieces"),
        "HRS": _("Hours"),
    }
    title = models.CharField(_("Title"), max_length=255)
    estimated_time = models.TimeField(_("Estimated time"))
    price = models.FloatField(_("Price"))
    number = models.FloatField(_("Number"))
    units = models.CharField(_("Units"), max_length=3, choices=UNITS)
    work_type = models.ForeignKey(WorkType, verbose_name=_("Work type"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("action type")
        verbose_name_plural = _("action types")
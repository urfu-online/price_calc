from django.db import models


class WorkType(models.Model):
    title = models.CharField(max_length=255)
    product_is_required = models.BooleanField(default=False)


class ActionType(models.Model):
    title = models.CharField(max_length=255)
    estimated_time = models.TimeField
    price = models.FloatField()
    work_type = models.ForeignKey(WorkType, on_delete=models.CASCADE)

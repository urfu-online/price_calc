from django.db import models
from sortedm2m.fields import SortedManyToManyField
from price.models import ActionType, WorkType
from person.models import Role, Person

from django.utils.translation import gettext_lazy as _


class Artefact(models.Model):
    STATUSES = {
        "NEW": _("New"),
        "APV": _("Approved"),
        "DSC": _("Discarded"),
        "CHK": _("On verification"),
        "LGC": _("Legacy"),
    }
    file = models.FileField(upload_to='artefacts')
    content = models.TextField(blank=True)
    status = models.CharField(max_length=3, choices=STATUSES, default='NEW')


class Action(models.Model):
    type = models.ForeignKey(ActionType, on_delete=models.PROTECT)
    real_time = models.TimeField()

    def __str__(self):
        return f"{self.type} {self.real_time}"


class Project(models.Model):
    title = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    product = models.ForeignKey('Product', blank=True, null=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.title


class Task(models.Model):
    title = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    prerequisites = SortedManyToManyField('self', blank=True)
    project = models.ForeignKey(Project, on_delete=models.PROTECT)

    def __str__(self):
        return self.title


class Product(models.Model):
    STATUSES = {
        "NEW": _("New"),
        "APV": _("Approved"),
        "DSC": _("Discarded"),
        "CHK": _("On verification"),
        "LGC": _("Legacy"),
    }
    title = models.TextField()
    artefact = models.ForeignKey(Artefact, blank=True, null=True, on_delete=models.PROTECT)
    file = models.FileField(upload_to='products')
    link = models.URLField(blank=True, null=True)
    task = models.ForeignKey(Task, blank=True, null=True, on_delete=models.PROTECT)
    status = models.CharField(max_length=3, choices=STATUSES, default='NEW')

    def __str__(self):
        return self.title


class Work(models.Model):
    STATUSES = {
        "NEW": _("New"),
        "ASG": _("Assigned"),
        "APV": _("Approved"),
        "DSC": _("Discarded"),
        "CHK": _("On verification"),
        "DNE": _("Done"),
    }
    work_type = models.ForeignKey(WorkType, on_delete=models.PROTECT)
    role = models.ForeignKey(Role, on_delete=models.PROTECT)
    executor = models.ForeignKey(Person, on_delete=models.PROTECT)
    prerequisites = SortedManyToManyField('self', blank=True)
    actions = SortedManyToManyField(Action)
    status = models.CharField(max_length=3, choices=STATUSES, default='NEW')
    task = models.ForeignKey(Task, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.task} {self.work_type} {self.executor}"

from django.db import models
from sortedm2m.fields import SortedManyToManyField
from price.models import ActionType, WorkType
from person.models import Role, Person


class Project(models.Model):
    title = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    product = models.ForeignKey(Role, blank=True, null=True, on_delete=models.PROTECT)


class Artefact(models.Model):
    STATUSES = {
        "NEW": "New",
        "APV": "Approved",
        "DSC": "Discarded",
        "CHK": "On verification",
        "LGC": "Legacy",
    }
    file = models.FileField(upload_to='artefacts')
    content = models.TextField(blank=True)
    status = models.CharField(max_length=3, choices=STATUSES, default='NEW')


class Action(models.Model):
    type = models.ForeignKey(ActionType, on_delete=models.PROTECT)
    real_time = models.TimeField()


class Task(models.Model):
    title = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    prerequisites = SortedManyToManyField('self')
    project = models.ForeignKey(Role, on_delete=models.PROTECT)


class Product(models.Model):
    STATUSES = {
        "NEW": "New",
        "APV": "Approved",
        "DSC": "Discarded",
        "CHK": "On verification",
        "LGC": "Legacy",
    }
    title = models.TextField()
    artefact = models.ForeignKey(Artefact, blank=True, null=True, on_delete=models.PROTECT)
    file = models.FileField(upload_to='products')
    link = models.URLField(blank=True, null=True)
    task = models.ForeignKey(Task, blank=True, null=True, on_delete=models.PROTECT)
    status = models.CharField(max_length=3, choices=STATUSES, default='NEW')


class Work(models.Model):
    STATUSES = {
        "NEW": "New",
        "ASG": "Assigned",
        "APV": "Approved",
        "DSC": "Discarded",
        "CHK": "On verification",
        "DNE": "Done",
    }
    work_type = models.ForeignKey(WorkType, on_delete=models.PROTECT)
    role = models.ForeignKey(Role, on_delete=models.PROTECT)
    executor = models.ForeignKey(Person, on_delete=models.PROTECT)
    prerequisites = SortedManyToManyField('self')
    actions = SortedManyToManyField(Action)
    status = models.CharField(max_length=3, choices=STATUSES, default='NEW')
    task = models.ForeignKey(Task, on_delete=models.PROTECT)

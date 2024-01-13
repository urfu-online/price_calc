from django.db import models
from django.conf import settings


class Skill(models.Model):
    title = models.TextField()


class Role(models.Model):
    title = models.CharField(max_length=36)
    skills = models.ManyToManyField(Skill)


class Person(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True,
                             related_name='person')
    first_name = models.CharField(max_length=36, blank=True, null=True)
    last_name = models.CharField(max_length=36, blank=True, null=True)
    roles = models.ManyToManyField(Role)

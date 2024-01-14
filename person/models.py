from django.db import models
from django.conf import settings


class Skill(models.Model):
    title = models.TextField()

    def __str__(self):
        return self.title


class Role(models.Model):
    title = models.CharField(max_length=36)
    skills = models.ManyToManyField(Skill)

    def __str__(self):
        return self.title


class Person(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True,
                             related_name='person')
    first_name = models.CharField(max_length=36, blank=True, null=True)
    last_name = models.CharField(max_length=36, blank=True, null=True)
    roles = models.ManyToManyField(Role)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

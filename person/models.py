from django.db import models


class Skill(models.Model):
    title = models.TextField()


class Role(models.Model):
    title = models.CharField(max_length=36)
    skills = models.ManyToManyField(Skill)


class Person(models.Model):
    first_name = models.CharField(max_length=36, blank=True, null=True)
    last_name = models.CharField(max_length=36, blank=True, null=True)
    roles = models.ManyToManyField(Role)

from django.contrib import admin

from .models import Skill, Role, Person


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    raw_id_fields = ('skills',)


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'first_name', 'last_name')
    list_filter = ('user',)
    raw_id_fields = ('roles',)

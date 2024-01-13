from django.contrib import admin

from .models import Project, Artefact, Action, Task, Product, Work


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'start_date', 'end_date', 'product')
    list_filter = ('start_date', 'end_date', 'product')


@admin.register(Artefact)
class ArtefactAdmin(admin.ModelAdmin):
    list_display = ('id', 'file', 'content', 'status')


@admin.register(Action)
class ActionAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'real_time')
    list_filter = ('type',)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'start_date', 'end_date', 'project')
    list_filter = ('start_date', 'end_date', 'project')
    raw_id_fields = ('prerequisites',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'artefact',
        'file',
        'link',
        'task',
        'status',
    )
    list_filter = ('artefact', 'task')


@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ('id', 'work_type', 'role', 'executor', 'status', 'task')
    list_filter = ('work_type', 'role', 'executor', 'task')
    raw_id_fields = ('prerequisites', 'actions')
from django.contrib import admin

from .models import WorkType, ActionType


@admin.register(WorkType)
class WorkTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'product_is_required')
    list_filter = ('product_is_required',)


@admin.register(ActionType)
class ActionTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'work_type')
    list_filter = ('work_type',)

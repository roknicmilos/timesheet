from django.contrib import admin
from main.admin import ModelAdmin
from projects.models import Project


@admin.register(Project)
class ProjectAdmin(ModelAdmin):
    fields = ('id', 'name', 'client', 'description', 'is_active', 'is_archived', 'lead_employee',)
    list_display = ('id', 'name', 'client', 'is_active', 'is_archived', 'lead_employee',)
    search_fields = ('name',)
    readonly_fields = ('id',)

from django.contrib import admin
from main.admin import ModelAdmin
from projects.models import Category


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    fields = ('id', 'name',)
    list_display = ('id', 'name',)
    search_fields = ('name',)
    readonly_fields = ('id',)

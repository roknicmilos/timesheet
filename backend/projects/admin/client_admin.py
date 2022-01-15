from django.contrib import admin
from main.admin import ModelAdmin
from projects.models import Client


@admin.register(Client)
class ClientAdmin(ModelAdmin):
    list_display = ('id', 'name', 'street', 'city', 'zip_code', 'country',)
    search_fields = ('name',)
    readonly_fields = ('id',)


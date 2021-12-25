from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from auth.models import User

admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('email', 'name', 'is_active', 'is_staff', 'is_superuser', 'is_admin',)
    list_filter = ('is_active', 'is_staff', 'is_superuser', 'is_admin',)
    search_fields = ('email', 'name',)
    ordering = ('email',)

    add_form = UserCreationForm
    fieldsets = (
        (None, {
            'fields': ('id', 'email', 'name', 'weekly_hours', 'is_admin', 'password',)
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined',)
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    readonly_fields = ('id', 'last_login', 'date_joined',)

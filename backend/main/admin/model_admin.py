from django.contrib import admin
from django.shortcuts import redirect
from main.admin import ModelAdminChecks
from main.models import BaseModel
from main.utils import remove_duplicates, get_model_admin_change_details_url


class ModelAdmin(admin.ModelAdmin):
    admin_namespace: str = 'admin'
    checks_class = ModelAdminChecks

    add_form_fieldsets: tuple = None
    add_form_fields: tuple = None
    with_inlines_when_adding: bool = False

    includes_timestamped_fields: bool = True
    timestamped_fields = ('created', 'modified',)

    def get_fieldsets(self, request, obj: BaseModel = None):
        self.prepare_fields(request=request, obj=obj)
        self.prepare_fieldsets(request=request, obj=obj)
        return super(ModelAdmin, self).get_fieldsets(request, obj)

    def prepare_fields(self, request, obj: BaseModel = None) -> None:
        self.fields = self.__class__.fields

        if self.should_use_add_form_fields(request, obj=obj):
            self.fields = self.add_form_fields

        if self.includes_timestamped_fields and self.fields:
            self.fields += self.timestamped_fields

    def should_use_add_form_fields(self, request, obj: BaseModel = None) -> bool:
        return not obj and self.add_form_fields is not None

    def prepare_fieldsets(self, request, obj: BaseModel = None) -> None:
        self.fieldsets = self.__class__.fieldsets

        if self.should_use_add_form_fieldsets(request, obj=obj):
            self.fieldsets = self.add_form_fieldsets

        elif self.includes_timestamped_fields and self.fieldsets:
            self.extend_fieldsets_with_timestamped_fields()

    def extend_fieldsets_with_timestamped_fields(self, fieldset_index: int = 0) -> None:
        updated_fieldset_fields = tuple(self.fieldsets[fieldset_index][1].get('fields')) + self.timestamped_fields
        self.fieldsets[fieldset_index][1]['fields'] = remove_duplicates(updated_fieldset_fields)

    def should_use_add_form_fieldsets(self, request, obj: BaseModel = None) -> bool:
        return not obj and self.add_form_fieldsets is not None

    def get_readonly_fields(self, *args, **kwargs) -> tuple:
        if self.includes_timestamped_fields:
            self.readonly_fields += self.timestamped_fields
        return tuple(set(self.readonly_fields))

    def get_inline_instances(self, request, obj: BaseModel = None):
        inlines = super(ModelAdmin, self).get_inline_instances(request, obj=obj)

        if obj:
            return inlines

        return inlines if self.with_inlines_when_adding else []

    def response_add(self, request, obj: BaseModel, post_url_continue=None):
        return redirect(get_model_admin_change_details_url(obj=obj) or '.')

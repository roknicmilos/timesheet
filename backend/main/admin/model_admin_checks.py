from itertools import chain
from django.contrib.admin.checks import ModelAdminChecks as BaseModelAdminChecks, must_be
from django.contrib.admin.utils import flatten
from django.core import checks


class ModelAdminChecks(BaseModelAdminChecks):

    def check(self, admin_obj, **kwargs):
        return [
            *super().check(admin_obj),
            *self._check_add_form_fields(admin_obj),
            *self._check_add_form_fieldsets(admin_obj),
        ]

    def _check_fields(self, obj):
        """ Check that `fields` only refer to existing fields, doesn't contain
        duplicates. Check if at most one of `fields` and `fieldsets` is defined.
        """

        if obj.fields is None:
            return []
        elif not isinstance(obj.fields, (list, tuple)):
            return must_be('a list or tuple', option='fields', obj=obj, id='admin.E004')
        elif obj.fieldsets:
            return [
                self._create_both_fields_and_fieldsets_specified(
                    obj_class=obj.__class__,
                    fields_name='fields',
                    fieldsets_name='fieldsets'
                )
            ]
        elif obj.add_form_fieldsets:
            return [
                self._create_both_fields_and_fieldsets_specified(
                    obj_class=obj.__class__,
                    fields_name='fields',
                    fieldsets_name='add_form_fieldsets'
                )
            ]

        fields = flatten(obj.fields)
        if len(fields) != len(set(fields)):
            return [
                checks.Error(
                    "The value of 'fields' contains duplicate field(s).",
                    obj=obj.__class__,
                    id='admin.E006',
                )
            ]

        return list(chain.from_iterable(
            self._check_field_spec(obj, field_name, 'fields')
            for field_name in obj.fields
        ))

    @staticmethod
    def _create_both_fields_and_fieldsets_specified(obj_class, fields_name: str, fieldsets_name: str) -> checks.Error:
        return checks.Error(
            f"Both '{fieldsets_name}' and '{fields_name}' are specified.",
            obj=obj_class,
            id='admin.E005',
        )

    def _check_add_form_fieldsets(self, obj):
        """ Check that add_form_fieldsets is properly formatted and doesn't contain duplicates. """

        if obj.add_form_fieldsets is None:
            return []
        elif not isinstance(obj.add_form_fieldsets, (list, tuple)):
            return must_be('a list or tuple', option='add_form_fieldsets', obj=obj, id='admin.E007')
        else:
            seen_fields = []
            return list(chain.from_iterable(
                self._check_fieldsets_item(obj, fieldset, 'add_form_fieldsets[%d]' % index, seen_fields)
                for index, fieldset in enumerate(obj.add_form_fieldsets)
            ))

    def _check_add_form_fields(self, obj):
        """
        Check that `add_form_fields` only refer to existing fields, doesn't contain duplicates.
        Check if at most one of `add_form_fields` and `add_form_fieldsets` is defined.
        """

        if obj.add_form_fields is None:
            return []
        elif not isinstance(obj.add_form_fields, (list, tuple)):
            return must_be('a list or tuple', option='add_form_fields', obj=obj, id='admin.E004')
        elif obj.fieldsets:
            return [
                self._create_both_fields_and_fieldsets_specified(
                    obj_class=obj.__class__,
                    fields_name='add_form_fields',
                    fieldsets_name='fieldsets'
                )
            ]
        elif obj.add_form_fieldsets:
            return [
                self._create_both_fields_and_fieldsets_specified(
                    obj_class=obj.__class__,
                    fields_name='add_form_fields',
                    fieldsets_name='add_form_fieldsets'
                )
            ]

        fields = flatten(obj.add_form_fields)
        if len(fields) != len(set(fields)):
            return [
                checks.Error(
                    "The value of 'add_form_fields' contains duplicate field(s).",
                    obj=obj.__class__,
                    id='admin.E006',
                )
            ]

        return list(chain.from_iterable(
            self._check_field_spec(obj, field_name, 'add_form_fields')
            for field_name in obj.add_form_fields
        ))

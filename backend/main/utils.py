from django.contrib.contenttypes.models import ContentType
from django.db.models import Model, QuerySet
from django.urls import reverse


def mask_string(string: str, masked_chars_count: int = None, starts_from_end: bool = True) -> str:
    if masked_chars_count is None:
        return ''.join(['*' for _ in range(len(string))])

    string_visible_part = string[:masked_chars_count] if starts_from_end else string[masked_chars_count:]
    string_masked_part = ''.join(['*' for _ in range(masked_chars_count)])

    if starts_from_end:
        return string_visible_part + string_masked_part
    return string_masked_part + string_visible_part


def remove_duplicates(collection: list | tuple) -> list | tuple:
    collection_type = type(collection)
    return collection_type(dict.fromkeys(collection))


def get_model_admin_change_details_url(obj: Model) -> str:
    content_type = ContentType.objects.get_for_model(obj.__class__)
    return reverse(f'admin:{content_type.app_label}_{content_type.model}_change', args=(obj.id,))


def paginate_queryset(queryset: QuerySet, request) -> QuerySet:
    page = int(request.query_params.get('page', 1))
    items_per_page = int(request.query_params.get('ipp', 50))
    limit = items_per_page * page
    offset = limit - items_per_page
    return queryset[offset:limit]

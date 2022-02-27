from django.contrib.contenttypes.models import ContentType
from django.db.models import Model, QuerySet
from django.urls import reverse
from datetime import datetime as datetime_type
from main.settings import DATETIME_FORMAT


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


def paginate_queryset(queryset: QuerySet, request, default_items_per_page: int = 50) -> QuerySet:
    page = int(request.query_params.get('page', 1))
    items_per_page = int(request.query_params.get('ipp', default_items_per_page))
    limit = items_per_page * page
    offset = limit - items_per_page
    return queryset[offset:limit]


def format_datetime(datetime: datetime_type) -> str:
    return datetime.strftime(DATETIME_FORMAT)


def get_bool_url_param_value(url_params: dict, param_name: str) -> bool | None:
    if param_name not in url_params:
        return None

    param_value_str = url_params.get(param_name).lower()

    if param_value_str == 'true':
        return True

    if param_value_str == 'false':
        return False

    return None

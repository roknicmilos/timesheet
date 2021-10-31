from django.core.exceptions import ValidationError


def validate_raw_password(raw_password: str) -> None:
    if not raw_password:
        raise ValidationError('Password must be provided')
    if len(raw_password) < 8:
        raise ValidationError('Password must be at least 8 characters long')
    if not _has_digit(string=raw_password):
        raise ValidationError('Password must consist at least 1 number')
    if not _has_letter(string=raw_password):
        raise ValidationError('Password must consist at least 1 letter')


def _has_digit(string: str) -> bool:
    for char in string:
        if char.isdigit():
            return True
    return False


def _has_letter(string: str) -> bool:
    for char in string:
        if char.isalpha():
            return True
    return False


def mask_string(string: str, masked_chars_count: int = None, starts_from_end: bool = True) -> str:
    if masked_chars_count is None:
        return ''.join(['*' for _ in range(len(string))])

    string_visible_part = string[:masked_chars_count] if starts_from_end else string[masked_chars_count:]
    string_masked_part = ''.join(['*' for _ in range(masked_chars_count)])

    if starts_from_end:
        return string_visible_part + string_masked_part
    return string_masked_part + string_visible_part

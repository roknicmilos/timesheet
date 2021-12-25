def mask_string(string: str, masked_chars_count: int = None, starts_from_end: bool = True) -> str:
    if masked_chars_count is None:
        return ''.join(['*' for _ in range(len(string))])

    string_visible_part = string[:masked_chars_count] if starts_from_end else string[masked_chars_count:]
    string_masked_part = ''.join(['*' for _ in range(masked_chars_count)])

    if starts_from_end:
        return string_visible_part + string_masked_part
    return string_masked_part + string_visible_part

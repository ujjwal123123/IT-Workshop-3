from typing import List


def string_into_characters(string: str) -> List[str]:
    """
    >>> string_into_characters("abc")
    ['a', 'b', 'c']
    >>> string_into_characters("")
    []
    """
    return [char for char in string]

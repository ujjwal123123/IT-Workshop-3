from typing import List


def chars_into_string(chars: List[str]) -> str:
    """
    >>> chars_into_string(['a', 'b', 'c'])
    'abc'
    >>> chars_into_string([])
    ''
    """
    return "".join(chars)

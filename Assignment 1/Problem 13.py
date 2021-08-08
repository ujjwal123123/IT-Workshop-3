from typing import List


def uppercase(words: List[str]) -> List[str]:
    """
    >>> print(uppercase(["aa", "bb", "cc", "e"]))
    ['AA', 'BB', 'CC', 'E']
    >>> print(uppercase(["hello", "world"]))
    ['HELLO', 'WORLD']
    """
    return list(map(lambda x: x.upper(), words))

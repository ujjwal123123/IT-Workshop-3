from typing import List


def generate_squares(num: int) -> List[int]:
    """
    >>> print(generate_squares(5))
    [0, 1, 4, 9, 16, 25]
    >>> print(generate_squares(10))
    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    """
    return [i * i for i in range(num + 1)]

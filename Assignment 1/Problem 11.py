from typing import Dict


def squares(num: int) -> Dict[int, int]:
    """
    >>> print(squares(5))
    {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
    >>> print(squares(10))
    {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
    """
    return {i: i * i for i in range(num + 1)}

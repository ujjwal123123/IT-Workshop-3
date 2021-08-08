from functools import reduce
from typing import List


def multiply(nums: List[int]) -> int:
    """
    >>> print(multiply([1, 2, 3]))
    6
    >>> print(multiply([1, 2, 3, 4, 5]))
    120
    """
    return reduce(lambda x, y: x * y, nums)

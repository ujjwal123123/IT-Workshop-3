from typing import Dict, List
from collections import Counter


def count_frequency(nums: List[int]) -> Dict[int, int]:
    """
    >>> count_frequency([1,1,3,2,3,2,3,2,2])
    {1: 2, 3: 3, 2: 4}
    >>> count_frequency([1,2,3,2,3,2,3,2,2])
    {1: 1, 2: 5, 3: 3}
    """
    return dict(Counter(nums))

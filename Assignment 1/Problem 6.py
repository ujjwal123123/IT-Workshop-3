from typing import List, Set


def get_uniques(nums: List[int]) -> Set[int]:
    """
    >>> get_uniques([1, 1, 3, 2, 3, 2, 3, 2, 2])
    {1, 2, 3}
    >>> get_uniques([2, 1, 3, 4, 8])
    {1, 2, 3, 4, 8}
    """
    return set(nums)
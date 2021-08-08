""" Write a function a sort a given list of numbers in descending order. """

from typing import List


def sort_in_descending(nums: List[int]) -> List[int]:
    """
    >>> sort_in_descending([1, 2, 3, 4])
    [4, 3, 2, 1]
    >>> sort_in_descending([1, 4, 3, 2])
    [4, 3, 2, 1]
    """
    return sorted(nums, reverse=True)

from typing import List, Set


def first_repeating_element(nums: List[int]) -> int | None:
    """
    >>> first_repeating_element([1,2,3,4,5,1,2])
    1
    >>> first_repeating_element([1,2,3,4,5,3,2])
    3
    """
    seen: Set[int] = set()

    for num in nums:
        if num in seen:
            return num
        else:
            seen.add(num)

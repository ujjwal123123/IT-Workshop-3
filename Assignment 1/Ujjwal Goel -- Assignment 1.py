import random
import time
from collections import Counter
from functools import reduce
from typing import Any, Dict, List, Set, Tuple, Callable


def string_into_characters(string: str) -> List[str]:
    """
    Problem 1
    >>> string_into_characters("abc")
    ['a', 'b', 'c']
    >>> string_into_characters("")
    []
    """
    return [char for char in string]


def chars_into_string(chars: List[str]) -> str:
    """
    Problem 2
    >>> chars_into_string(['a', 'b', 'c'])
    'abc'
    >>> chars_into_string([])
    ''
    """
    return "".join(chars)


random.seed(time.time())  # this is already the default!!


def generate_random(length: int):
    """
    Problem 3 Write a function generate a list of n random numbers. Use the inbuilt `random`
    module.
    >>> len(generate_random(5))
    5
    >>> len(generate_random(0))
    0
    """
    return [random.random() for _ in range(length)]


def sort_in_descending(nums: List[int]) -> List[int]:
    """
    Problem 4 Write a function a sort a given list of numbers in descending order.
    >>> sort_in_descending([1, 2, 3, 4])
    [4, 3, 2, 1]
    >>> sort_in_descending([1, 4, 3, 2])
    [4, 3, 2, 1]
    """
    return sorted(nums, reverse=True)


def count_frequency(nums: List[int]) -> Dict[int, int]:
    """
    Problem 5
    >>> count_frequency([1,1,3,2,3,2,3,2,2])
    {1: 2, 3: 3, 2: 4}
    >>> count_frequency([1,2,3,2,3,2,3,2,2])
    {1: 1, 2: 5, 3: 3}
    """
    return dict(Counter(nums))


def get_uniques(nums: List[int]) -> Set[int]:
    """
    Problem 6
    >>> get_uniques([1, 1, 3, 2, 3, 2, 3, 2, 2])
    {1, 2, 3}
    >>> get_uniques([2, 1, 3, 4, 8])
    {1, 2, 3, 4, 8}
    """
    return set(nums)


def first_repeating_element(nums: List[int]) -> int | None:
    """
    Problem 7
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


def squares_and_cubes(num: int) -> Dict[int, List[int]]:
    """
    Problem 8
    >>> squares_and_cubes(0)
    {0: [0, 0]}
    >>> squares_and_cubes(4)
    {0: [0, 0], 1: [1, 1], 2: [4, 8], 3: [9, 27], 4: [16, 64]}
    """
    dictionary: Dict[int, List[int]] = dict()
    for i in range(num + 1):
        dictionary[i] = [i ** 2, i ** 3]
    return dictionary


def create_tuples(list1: List[Any], list2: List[Any]) -> List[Tuple[Any, Any]]:
    """
    Problem 9
    >>> create_tuples([1, 2, 3, 4], ['a', 'b', 'c', 'd'])
    [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
    >>> create_tuples([3, 4, 6, 7], ["i", "am", "ujjwal", "goel"])
    [(3, 'i'), (4, 'am'), (6, 'ujjwal'), (7, 'goel')]
    """

    return list(zip(list1, list2))


def generate_squares(num: int) -> List[int]:
    """
    Problem 10
    >>> print(generate_squares(5))
    [0, 1, 4, 9, 16, 25]
    >>> print(generate_squares(10))
    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    """
    return [i * i for i in range(num + 1)]


def squares(num: int) -> Dict[int, int]:
    """
    Problem 11
    >>> print(squares(5))
    {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
    >>> print(squares(10))
    {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
    """
    return {i: i * i for i in range(num + 1)}


class problem12:
    """
    Problem 12:
    # I could not get multiline doctests to work which are needed for this
    # Problem
    """

    def __init__(self, saved_list: List[Any]) -> None:
        self.saved_list = saved_list

    def apply(self, func: Callable[[Any], List[Any]]) -> List[Any]:
        try:
            return list(map(func, self.saved_list))
        except:
            raise Exception("Could not apply the function to the list")


def uppercase(words: List[str]) -> List[str]:
    """
    Problem 13
    >>> print(uppercase(["aa", "bb", "cc", "e"]))
    ['AA', 'BB', 'CC', 'E']
    >>> print(uppercase(["hello", "world"]))
    ['HELLO', 'WORLD']
    """
    return list(map(lambda x: x.upper(), words))


def multiply(nums: List[int]) -> int:
    """
    Problem 14
    >>> print(multiply([1, 2, 3]))
    6
    >>> print(multiply([1, 2, 3, 4, 5]))
    120
    """
    return reduce(lambda x, y: x * y, nums)

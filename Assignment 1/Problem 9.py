from typing import Any, List, Tuple


def create_tuples(list1: List[Any], list2: List[Any]) -> List[Tuple[Any, Any]]:
    """
    >>> create_tuples([1, 2, 3, 4], ['a', 'b', 'c', 'd'])
    [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
    >>> create_tuples([3, 4, 6, 7], ["i", "am", "ujjwal", "goel"])
    [(3, 'i'), (4, 'am'), (6, 'ujjwal'), (7, 'goel')]
    """

    return list(zip(list1, list2))

from typing import Dict, List


def squares_and_cubes(num: int) -> Dict[int, List[int]]:
    """
    >>> squares_and_cubes(0)
    {0: [0, 0]}
    >>> squares_and_cubes(4)
    {0: [0, 0], 1: [1, 1], 2: [4, 8], 3: [9, 27], 4: [16, 64]}
    """
    dictionary: Dict[int, List[int]] = dict()
    for i in range(num + 1):
        dictionary[i] = [i ** 2, i ** 3]
    return dictionary

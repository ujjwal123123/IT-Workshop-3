""" Write a function generate a list of n random numbers. Use the inbuilt `random`
module. """

import random
import time

random.seed(time.time())  # this is already the default!!


def generate_random(length: int):
    """
    >>> len(generate_random(5))
    5
    >>> len(generate_random(0))
    0
    """
    return [random.random() for _ in range(length)]

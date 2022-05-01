from typing import Callable, List
import math


class DistanceFuncs:
    def calc_distance(
        self, point_a: List[float], point_b: List[float], dist_func: Callable, /
    ) -> float:
        return dist_func(point_a, point_b)

    @staticmethod
    def euclidean(point_a: List[float], point_b: List[float], /) -> float:
        return math.dist(point_a, point_b)

    @staticmethod
    def manhattan_distance(point_a: List[float], point_b: List[float], /) -> float:
        dist: float = 0
        for a, b in zip(point_a, point_b):
            dist += abs(a - b)
        return dist

    @staticmethod
    def jaccard_distance(point_a: List[float], point_b: List[float], /) -> float:
        intersection_len = len(set(point_a) & set(point_b))
        len_union = len(point_a) + len(point_b) - intersection_len

        return 1 - intersection_len / len_union


def main():
    pass


if __name__ == "__main__":
    main

"""
helpers.py — contains all helper functions used in this project.
"""

import math
import random
from typing import Tuple, Dict


def distance(point_1: Tuple[int, int], point_2: Tuple[int, int]) -> float:
    """
    Calculate euclidean distance between two points.

    Parameters:
    ----------
    point_1: Tuple[int, int]
        (x,y) coordinates of the first point.
    point_2: Tuple[int, int]
        (x,y) coordinates of the second point.
    """
    x1, y1 = point_1
    x2, y2 = point_2
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)


def shuffle_dictionary(dict_old: Dict, seed: int) -> Dict:
    """
    Rearranges the order in which key: value pairs appear
    in the dictionary.

    Parameters:
    ----------
    dict_old: dict
        Dictionary to be shuffled.
    seed: int
        Seed for the random permutation of the keys.
    """
    keys = list(dict_old.keys())
    random.seed(seed)
    random.shuffle(keys)
    new_dict = {k: dict_old[k] for k in keys}
    return new_dict

#!/usr/bin/env python3

""" to_kv function """

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Takes string k and/or float v and returns tuple

        Args:
            k: String
            v: Float

        Returns: Tuple
    """
    return (k, v * v)

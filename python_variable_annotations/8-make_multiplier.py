#!/usr/bin/env python3

""" Make_multiplier function """


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:

    def multi_func(n: float) -> float:
        return (n * multiplier)
    return multi_func

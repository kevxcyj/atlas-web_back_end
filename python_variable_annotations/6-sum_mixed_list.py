#!/usr/bin/env python3

""" Returns sum of integers and floats """

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ Adds together values and returns sum

        Args:
            mxd_list: Integers/floats

        Returns:
            Sum of Integers/floats
    """

    return sum(mxd_lst)

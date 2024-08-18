#!/usr/bin/env python3
"""  type-annotated function make_multiplier """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def multiplier_function(value: float) -> float:
        """ return the value multiplie """
        return value * multiplier
    """ return multi function """
    return multiplier_function

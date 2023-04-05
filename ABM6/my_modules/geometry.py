# -*- coding: utf-8 -*-
import math

def get_distance(x0, y0, x1, y1):
    """
    calculate the diatance between x0y0 and x1y1

    Parameters
    ----------
    x0 : int
    y0 : int
    x1 : int
    y1 : int
    """
    # Calculate the difference in the x coordinates.
    dx = x0 - x1
    # Calculate the difference in the y coordinates.
    dy = y0 - y1
    # Square the differences and add the squares
    ssd = (dx * dx) + (dy * dy)
    # Calculate the square root
    distance = ssd ** 0.5
    return distance
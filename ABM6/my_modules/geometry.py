# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 10:35:47 2023

@author: 肉松
"""

import math


def get_distance(x0, y0, x1, y1):
    # Calculate the difference in the x coordinates.
    dx = x0 - x1
    # Calculate the difference in the y coordinates.
    dy = y0 - y1
    # Square the differences and add the squares
    ssd = (dx * dx) + (dy * dy)
    # Calculate the square root
    distance = ssd ** 0.5
    return distance
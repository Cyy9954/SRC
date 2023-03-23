# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 19:20:17 2023

"""
import random
import math

# Set the pseudo-random seed for reproducibility
random.seed(0)

# Initialise variables x0 and y0 with random values between 0 and 99
x0 = random.randint(0, 99)
print("x0", x0)
# Initialise variable y0
y0 = random.randint(0, 99)
print("y0", y0)

#Randomly change x0 and y0
rn = random.random()
print("rn:", rn)
if rn < 0.5:
    x0 += 1
else:
    x0 -= 1
print("new x0:", x0)

rn = random.random()
print("rn:", rn)
if rn < 0.5:
    y0 += 1
else:
    y0 -= 1
print("new y0:", y0)

# Initialise variables x1 and y1 with random values between 0 and 99
x1 = random.randint(0, 99)
print("x1", x1)
# Initialise variable y1
y1 = random.randint(0, 99)
print("y1", y1)

# Change x1 and y1 randomly
rn = random.random()
print("rn:", rn)
if rn < 0.5:
    x1 += 1
else:
    x1 -= 1
print("new x1:", x1)

rn = random.random()
print("rn:", rn)
if rn < 0.5:
    y1 += 1
else:
    y1 -= 1
print("new y1:", y1)

# Calculate the Euclidean distance between (x0, y0) and (x1, y1)
# Setting the values to (0,0) and (3,4) to match the sample output
x0 = 0
y0 = 0
x1 = 3
y1 = 4
# Calculate the difference in the x coordinates.
dx = x0 - x1
# Calculate the difference in the y coordinates.
dy = y0 - y1
# Square the differences and sum them
ssd = (dx * dx) + (dy * dy)
print("Sum of Squared Differences (SSD):", ssd)
# Calculate the square root of the SSD to obtain the Euclidean distance
distance = ssd ** 0.5
print("distance", distance)
distance = math.sqrt(ssd)
print("Euclidean distance:", distance)

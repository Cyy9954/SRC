# -*- coding: utf-8 -*-
import random
import math
import matplotlib.pyplot as plt
import operator

# Set the pseudo-random seed for reproducibility
random.seed(0)

# A variable to store the number of agents
n_agents = 10

# Initialise agents
agents = []
for i in range(n_agents):
    # Each agent is represented as a list of x and y coordinates
    agents.append([random.randint(0, 99), random.randint(0, 99)])
print("Initial agents:",agents)

# Move agents
for i in range(n_agents):
    # Change agents[i] coordinates randomly
    # x-coordinate
    rn = random.random()
    #print("rn", rn)
    if rn < 0.5:
        agents[i][0] = agents[i][0] + 1
    else:
        agents[i][0] = agents[i][0] - 1
    # y-coordinate
    rn = random.random()
    #print("rn", rn)
    if rn < 0.5:
        agents[i][1] = agents[i][1] + 1
    else:
        agents[i][1] = agents[i][1] - 1
print("Moved agents:", agents)

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

# Plot
for i in range(n_agents):
    plt.scatter(agents[i][0], agents[i][1], color='black')
# Plot the coordinate with the largest x red
lx = max(agents, key=operator.itemgetter(0))
plt.scatter(lx[0], lx[1], color='red')
# Plot the coordinate with the smallest x blue
sx = min(agents, key=operator.itemgetter(0))
plt.scatter(sx[0], sx[1], color='blue')
# Plot the coordinate with the largest y yellow
ly = max(agents, key=operator.itemgetter(1))
plt.scatter(ly[0], ly[1], color='yellow')
# Plot the coordinate with the smallest y green
sy = min(agents, key=operator.itemgetter(1))
plt.scatter(sy[0], sy[1], color='green')
plt.show()
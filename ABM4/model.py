import random
import math
import matplotlib.pyplot as plt
import operator
import time
import agentframework as af

# Set the pseudo-random seed for reproducibility
random.seed(0)

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

def get_max_distance(agents):
    max_distance = 0
    for i in range(len(agents)):
        a = agents[i]
        for j in range(i + 1, len(agents)):
            #print("i", i, "j", j)
            b = agents[j]
            distance = get_distance(a.x, a.y, agents[j].x, agents[j].y)
            #distance = get_distance(a.x, a.y, b.x, b.y)
            #print("distance between", a, b, distance)
            max_distance = max(max_distance, distance)
            #print("max_distance", max_distance)
    return max_distance

def get_min_distance():
    min_distance = math.inf
    for i in range(len(agents)):
        a = agents[i]
        for j in range(i + 1, len(agents)):
            #print("i", i, "j", j)
            b = agents[j]
            distance = get_distance(a.x, a.y, agents[j].x, agents[j].y)
            #distance = get_distance(a.x, a.y, b.x, b.y)
            #print("distance between", a, b, distance)
            min_distance = min(min_distance, distance)
            #print("min_distance", min_distance)
    return min_distance


# A variable to store the number of agents
n_agents = 10

#Create a list to store agents
agents = [af.Agent(i) for i in range(n_agents)]

# Move agents
for agent in agents:
    # Change agent coordinates randomly
    # x-coordinate
    rn = random.random()
    if rn < 0.5:
        agent.x += 1
    else:
        agent.x -= 1
    # y-coordinate
    rn = random.random()
    if rn < 0.5:
        agent.y += 1
    else:
        agent.y -= 1


# Variables for constraining movement.
# The minimum x coordinate.
x_min, y_min = 0, 0
# The maximum x coordinate.
x_max, y_max = 99, 99

# Apply movement constraints.
n_iterations=10
for i in range(n_iterations):
    for agent in agents:
        agent.move(x_min, y_min, x_max, y_max) 
        
# Plot
for i in range(n_agents):
    plt.scatter(agents[i].x, agents[i].y, color='black')
# Plot the coordinate with the largest x red
lx = max(agents, key=operator.attrgetter('x'))
plt.scatter(lx.x, lx.y, color='red')
# Plot the coordinate with the smallest x blue
sx = min(agents, key=operator.attrgetter('x'))
plt.scatter(sx.x, sx.y, color='blue')
# Plot the coordinate with the largest y yellow
ly = max(agents, key=operator.attrgetter('y'))
plt.scatter(ly.x, ly.y, color='yellow')
# Plot the coordinate with the smallest y green
sy = min(agents, key=operator.attrgetter('y'))
plt.scatter(sy.x, sy.y, color='green')

plt.show()

# -*- coding: utf-8 -*-

import random
import math
import matplotlib.pyplot as plt
import operator
import time

# Set the pseudo-random seed for reproducibility
random.seed(0)

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

def get_max_distance():
    max_distance = 0
    for i in range(len(agents)):
        a = agents[i]
        for j in range(i + 1, len(agents)):
            #print("i", i, "j", j)
            b = agents[j]
            distance = get_distance(a[0], a[1], b[0], b[1])
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
            distance = get_distance(a[0], a[1], b[0], b[1])
            #print("distance between", a, b, distance)
            min_distance = min(min_distance, distance)
            #print("min_distance", min_distance)
    return min_distance

# Change x0 and y0 randomly
def movement(list1):
    rn = random.random()
    if rn < 0.5:
       list1[0] = list1[0] + 1
    else:
        list1[0] = list1[0] - 1
    rn = random.random()
    if rn < 0.5:
        list1[1] = list1[1] + 1
    else:
        list1[1] = list1[1] - 1
    
    return list1

# A list to store times
run_times = []
n_agents_range = range(500, 5000, 500)

for n_agents in n_agents_range:
    
    # Initialise agents
    agents = []
    for i in range(n_agents):
        agents.append([random.randint(0, 99), random.randint(0, 99)])
    #print(agents)
    
    # Print the maximum distance between all the agents
    start = time.perf_counter()
    print("Maximum distance between all the agents", get_max_distance())
    print("Minimum distance between all the agents", get_min_distance())
    end = time.perf_counter()
    run_time = end - start
    print("Time taken to calculate maximum distance", run_time)
    run_times.append(run_time)

# Plot
plt.title("Time taken to calculate maximum distance for different numbers of agent")
plt.xlabel("Number of agents")
plt.ylabel("Time")
j = 0
for i in n_agents_range:
    plt.scatter(i, run_times[j], color='black')
    j = j + 1
plt.show()

# Variables for constraining movement.
# The minimum x coordinate.
x_min = 0
# The minimum y coordinate.
y_min = 0
# The maximum x coordinate.
x_max = 99
# The maximum y coordinate.
y_max = 99
# Apply movement constraints.

n_agents = 10
agents = []
for i in range(n_agents): 
    agents.append([random.randint(0, 99), random.randint(0, 99)])
for i in range(n_agents):
    plt.scatter(agents[i][0], agents[i][1], color='black')    
    
plt.show()    
    
n_iterations=1000
for i in range(n_iterations):
    for j in range(len(agents)):
        
        agents[j] = movement(agents[j])
        if agents[j][0] < x_min:
            agents[j][0] = x_min
        if agents[j][1] < y_min:
            agents[j][0] = y_min
        if agents[j][0] > x_max:
            agents[j][0] = x_max
        if agents[j][1] > y_max:
            agents[j][1] = y_max
for i in range(n_agents):
    plt.scatter(agents[i][0], agents[i][1], color='black')  
plt.show()

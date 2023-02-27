# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 19:42:19 2023

@author: 肉松
"""

import random
from matplotlib import pyplot as plt
import time

# Set the pseudo-random seed for reproducibility
random.seed(0)

# A variable to store the number of agents
#n_agents = 500

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
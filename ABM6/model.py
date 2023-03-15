# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 10:33:09 2023

@author: 肉松
"""

import random
import math
import matplotlib.pyplot as plt
import operator
import time
import my_modules.agentframework as af
import my_modules.io as io
import os
import imageio


def sum_agent_stores(agents):
    sum_store=0
    for i in range(len(agents)):
        sum_store+=agents[i].store
    return sum_store

def sum_environment(environment):
    sum_env=0
    for a in range(len(environment)):
        for j in range(len(environment[a])):
            sum_env +=environment[a][j]
    return sum_env

n_cols, n_rows, environment= io.read_data()
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

def get_max_distance(agents):
    max_distance = 0
    for i in range(len(agents)):
        a = agents[i]
        for j in range(i + 1, len(agents)):
            #print("i", i, "j", j)
            b = agents[j]
            distance = get_distance(a.x, a.y, b.x, b.y)
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
            distance = get_distance(a.x, a.y, b.x, b.y)
            #print("distance between", a, b, distance)
            min_distance = min(min_distance, distance)
            #print("min_distance", min_distance)
    return min_distance

if __name__ == '__main__':
    # Change x0 and y0 randomly
    '''def movement(list1):
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
    '''
    # Set the pseudo-random seed for reproducibility
    random.seed(0)

    # A variable to store the number of agents
    n_agents = 10

    #Create a new outer For Loop to loop through moving agents n_iteration times. 
    #An outer loop is wanted rather than an inner loop as in each iteration we want each agents to move in turn. 
    n_iterations=100

    # Initialise agents

    #a = af.Agent()
    #print("type(a)", type(a))

    agents = []
    for i in range(n_agents):
        # Create an agent
        agents.append(af.Agent(agents, i, environment, n_rows, n_cols))
        print(agents[i])
    print(agents)

    # Variables for constraining movement.
    # The minimum x coordinate.
    x_min = 0
    # The minimum y coordinate.
    y_min = 0
    # def 
    neighbourhood=50

    '''
    # The maximum x coordinate.
    x_max = 99
    # The maximum y coordinate.
    y_max = 99
    '''
    # Apply movement constraints.
    # The maximum an agents x coordinate is allowed to be.
    x_max = n_cols - 1
    # The maximum an agents y coordinate is allowed to be.
    #y_max = 99
    y_max = n_rows - 1

    # Create directory to write images to.
    try:
        os.makedirs('../../data/output/images/')
    except FileExistsError:
        print("path exists")

    # For storing images
    global ite
    ite = 0
    images = [] 
   
    # Model loop
    for ite in range(n_iterations):
        print("Iteration", ite)
        # Move agents
        print("Move")
        for i in range(n_agents):
            agents[i].move(x_min, y_min, x_max, y_max)
            agents[i].eat()
            #print(agents[i])
        # Share store
        # Distribute shares
        for i in range(n_agents):
            agents[i].share(neighbourhood)
        # Add store_shares to store and set store_shares back to zero
        for i in range(n_agents):
            print(agents[i])
            agents[i].store = agents[i].store_shares
            agents[i].store_shares = 0
        print(agents)
        # Print the maximum distance between all the agents
        print("Maximum distance between all the agents", get_max_distance(agents))
        # Print the total amount of resource
        sum_as = sum_agent_stores(agents)
        print("sum_agent_stores", sum_as)
        sum_e = sum_environment(environment)
        print("sum_environment", sum_e)
        print("total resource", (sum_as + sum_e))
        plt.imshow(environment)

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

        # A variable to store the number of agents
        #n_agents = 500

        plt.ylim(y_max / 3, y_max * 2 / 3)
        plt.xlim(x_max / 3, x_max * 2 / 3)
        '''
        plt.ylim(y_min, y_max)
        plt.xlim(x_min, x_max) 
        '''
        filename = '../../data/output/images/image' + str(ite) + '.png'
    #filename = '../../data/output/images/image' + str(ite) + '.gif'
        plt.savefig(filename)
        plt.show()
        plt.close()
        images.append(imageio.imread(filename))
          
        imageio.mimsave('../../data/output/out.gif', images, fps=3)
        print("1")









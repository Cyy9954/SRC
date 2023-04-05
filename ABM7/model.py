# -*- coding: utf-8 -*-
import matplotlib
import random
import math
import matplotlib.pyplot as plt
import operator
import time
import my_module.agentframework as af
import my_module.io as io
import os
import imageio
import matplotlib.animation as anim
import my_module.geometry as geo

# read environment data
n_cols, n_rows, environment = io.read_data()

# Set the pseudo-random seed for reproducibility
random.seed(0)

# calculates the total store value across all agents.
# It initializes a variable "sum_store" to zero and then loops through each agent in the "agents" list
def sum_agent_stores():
    sum_store=0
    for i in range(len(agents)):
        sum_store+=agents[i].store
    return sum_store

def sum_environment():
    sum_env=0
    for a in range(len(environment)): # Loop over each row in the matrix
        for j in range(len(environment[a])): # Loop over each column in the row
            sum_env +=environment[a][j]  # Add the value of each element to the sum
    return sum_env

# the largest and smallest x and y values using different colors.
def plot():
    # Clear the previous figure and set the x and y limits of the plot
    fig.clear()
    plt.ylim(y_min, y_max)
    plt.xlim(x_min, x_max)
    # Display the matrix "environment" as an image
    plt.imshow(environment)
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
    global ite
    filename = '../../data/output/images/image' + str(ite) + '.png'
    plt.savefig(filename)
    plt.show
    images.append(imageio.imread(filename))
    return fig

def update(frames):
    # Model loop
    global carry_on
    #for ite in range(n_iterations):
    print("Iteration", frames)
    # Move agents
    print("Move and eat")
    for i in range(n_agents):
        agents[i].move(x_min, y_min, x_max, y_max)
        agents[i].eat()
        #print(agents[i])
    # Share store
    print("Share")
    # Distribute shares
    for i in range(n_agents):
        agents[i].share(neighbourhood)
    # Add store_shares to store and set store_shares back to zero
    for i in range(n_agents):
        #print(agents[i])
        agents[i].store = agents[i].store_shares
        agents[i].store_shares = 0
    #print(agents)
    # Print the maximum distance between all the agents
    print("Maximum distance between all the agents", geo.get_max_distance(agents))
    # Print the total amount of resource
    sum_as = sum_agent_stores()
    print("sum_agent_stores", sum_as)
    sum_e = sum_environment()
    print("sum_environment", sum_e)
    print("total resource", (sum_as + sum_e))

    # Stopping condition
    # Random
    if random.random() < 0.1:
        #if sum_as / n_agents > 80:
        carry_on = False
        print("stopping condition")

    # Plot
    global ite
    plot()
    ite = ite + 1

def gen_function():
    global ite #controls the number of iterations
    ite = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (ite < n_iterations) & (carry_on) :
        yield ite # Returns control and waits next call.
        ite = ite + 1
    global data_written
    if data_written == False:
        # Write data
        print("write data")
        io.write_data('../../data/output/out7.txt', environment)
        imageio.mimsave('../../data/output/out7.gif', images, fps=3)
        data_written = True


if __name__ == '__main__':
    # A variable to store the number of agents
    n_agents = 10

    # Number of iterations
    n_iterations=100

    #creat agents
    agents = []
    for i in range(n_agents):
    # Create an agent and add it to the list of agents
        agents.append(af.Agent(agents, i, environment, n_rows, n_cols))

# Animate
# Initialise fig and carry_on
    fig = matplotlib.pyplot.figure(figsize=(7, 7))
    ax = fig.add_axes([0, 0, 1, 1])
    carry_on = True
    data_written = False
    animation = anim.FuncAnimation(fig, update, init_func=plot, frames=gen_function, repeat=False)

  # Variables for constraining movement
    x_min, y_min, neighbourhood = 0, 0, 50
    x_max, y_max = n_cols - 1, n_rows - 1
    
    # Create directory to write images to.
    try:
        os.makedirs('../../data/output/images/')
    except FileExistsError:
        print("path exists")

    # For storing images
    global ite
    ite = 0
    images = [] 
   









# -*- coding: utf-8 -*-


import random
import my_module.geometry
import matplotlib
matplotlib.use('TkAgg')
class Agent:
    def __init__(self, agents, i, environment, n_rows, n_cols):

        self.agents = agents
        self.i = i
        self.environment = environment
        tnc = int(n_cols / 3)
        self.x = random.randint(tnc - 1, (2 * tnc) - 1)
        tnr = int(n_rows / 3)
        self.y = random.randint(tnr - 1, (2 * tnr) - 1)
        self.store = 0
        self.store_shares = 0
        
    def eat(self):
        """
        eat environment variable

        """
        if self.environment[self.y][self.x] >= 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
        else:
            self.store += self.environment[self.y][self.x]
            self.environment[self.y][self.x] = 0

    # Define the string representation for Agent instan     
    def __str__(self):
        # Return the class name and the agent's x and y coordinates as a string.
        return self.__class__.__name__ + "(x=" + str(self.x) \
        + ", y=" + str(self.y) + ")"+ str(self.i)
      
    # Define the representation method for Agent instances.
    def __repr__(self):
        # Return the string representation of the agent.
        return str(self)
    
    # Indicates the minimum and maximum limits for movement
    def move(self, x_min, y_min, x_max, y_max):
        rn = random.random()
        # If the random number is less than 0.5, increase the x-coordinate, otherwise decrease the x-coordinate.
        if rn < 0.5:
            self.x = self.x + 1
        else:
            self.x = self.x - 1
        rn = random.random()
        if rn < 0.5:
            self.y = self.y + 1
        else:
            self.y = self.y - 1
        if self.x < x_min:
            self.x = x_min
        if self.y < y_min:
            self.y = y_min
        if self.x > x_max:
            self.x = x_max
        if self.y > y_max:
            self.y = y_max
        return self  
    
    def share(self, neighbourhood):
    # Create a list of agents in neighbourhood
        neighbours = []
    #print(self.agents[self.i])
        for a in self.agents:
            distance = my_module.geometry.get_distance(a.x, a.y, self.x, self.y)
            if distance < neighbourhood:
                neighbours.append(a.i)
    # Calculate amount to share
        n_neighbours = len(neighbours)
    #print("n_neighbours", n_neighbours)
        shares = self.store / n_neighbours
    #print("shares", shares)
    # Add shares to store_shares
        for i in neighbours:
            self.agents[i].store_shares += shares

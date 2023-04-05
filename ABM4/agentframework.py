# -*- coding: utf-8 -*-

import random

class Agent:
        """
        defines a class named Agent
        """
    def __init__(self, i):
        self.i = i
        self.x = random.randint(0, 99)
        self.y = random.randint(0, 99)
        pass
    
# Define the string representation for Agent instances.
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
    
        





        

# ABM Model Simulation README

## Introduction
This README provides an overview of the Agent-Based Model (ABM) simulation program that simulates agents moving in an environment, consuming resources, sharing resources, and generating plots. The program demonstrates how to use various Python libraries to create animations, read and write data, and generate plots.

## Requirements
This program requires Python 3.0 or higher and several additional packages, including tkinter, matplotlib, imageio, and bs4.

## Usage
To use the program, simply run the main simulation file model.py. The program will begin executing and display a visualization of the agent-based model simulation.

## Files
The program includes the following files:
- model.py: the main simulation file
- my_module/agentframework.py: contains the Agent class, which defines the behavior of the agents in the simulation
- my_module/io.py: contains functions for reading and writing data from/to files
- my_module/geometry.py: contains functions for calculating distances between agents
- data/in.txt: the input data file containing the initial environment data for the simulation
- data/output/: a directory containing output data generated during the simulation, including images and text files

## Program Overview
The program begins by initializing the environment and setting the random seed. It then defines two functions to calculate the total store value across all agents and the total value of the environment.

Next, the program defines a function to plot the environment, agents' locations, and the agents' locations with the highest and lowest x and y coordinates. The function saves the plots in a folder and appends the image to a list of images.

The program then defines a function to update the agents' positions and stores and triggers the stopping condition when the agents' average store exceeds 80. The function calls the plot function to create a plot at each iteration.

Next, the program defines a generator function that loops through the iterations and calls the update function until the stopping condition is met.

Finally, the program defines a function to create an animation object and draw the animation on a canvas. The program then calls the function and writes the data and creates a gif file.

## Conclusion
In conclusion, this program demonstrates how to use various Python libraries to simulate an ABM and generate useful plots that help to visualize the agents' behavior and the environment. The program also includes functions for reading and writing data, calculating distances between agents, and creating animations.

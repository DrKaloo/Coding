#A Python-based animated simulation of random neuronal activity using NetworkX and Matplotlib. 
#This project visualizes spike-like firing patterns in a simple neuron network to demonstrate basic principles of 
#network dynamics and brain-inspired activity


import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#Creating a neuron network (random connectivity)
num_neurons = 20
G = nx.erdos_renyi_graph(num_neurons, 0.3)

#Seting up figure for the animation 
fig, ax = plt.subplots(figsize=(6, 6))
pos = nx.spring_layout(G)  # Node positions
node_colours = [0] * num_neurons  # Initialize colour intensity

#Animation function
def update(frame):
    global node_colours
    node_colours = np.random.rand(num_neurons)  # Random activation levels
    ax.clear()
    nx.draw(G, pos, with_labels=True, node_colour=node_colours, cmap='inferno', edge_colour='gray', node_size=300)
    ax.set_title(f"Neuron Activity - Frame {frame}")

#Run animation
ani = animation.FuncAnimation(fig, update, frames=50, interval=200)
plt.show()
              

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#Create a neuron network (random connectivity)
num_neurons = 20
G = nx.erdos_renyi_graph(num_neurons, 0.3)

#Set up figure for animation
fig, ax = plt.subplots(figsize=(6, 6))
pos = nx.spring_layout(G)  # Node positions
node_colors = [0] * num_neurons  # Initialize color intensity

#Animation function
def update(frame):
    global node_colors
    node_colors = np.random.rand(num_neurons)  # Random activation levels
    ax.clear()
    nx.draw(G, pos, with_labels=True, node_color=node_colors, cmap='inferno', edge_color='gray', node_size=300)
    ax.set_title(f"Neuron Activity - Frame {frame}")

#Run animation
ani = animation.FuncAnimation(fig, update, frames=50, interval=200)
plt.show()
              
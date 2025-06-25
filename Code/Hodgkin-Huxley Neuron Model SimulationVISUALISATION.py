import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Network setup
N = 25  # number of nodes
p_conn = 0.25  # connection probability
net = nx.erdos_renyi_graph(N, p_conn, seed=42)

# Get layout once and keep it fixed
layout = nx.spring_layout(net, k=1.5, iterations=50)

# Start
fig, ax = plt.subplots(figsize=(8, 8))
activities = np.zeros(N)

def animate_network(frame):
    ax.clear()
    
    # Simple activity model - some random, with decay
    global activities
    activities = activities * 0.8 + np.random.exponential(0.3, N)
    activities = np.clip(activities, 0, 1)
    
    # Draw network
    nx.draw_networkx_edges(net, layout, ax=ax, alpha=0.4, edge_color='gray', width=0.8)
    nx.draw_networkx_nodes(net, layout, ax=ax, 
                          node_color=activities, 
                          cmap='plasma',
                          node_size=400,
                          vmin=0, vmax=1)
    
    ax.set_title(f'Network Activity (t={frame})')
    ax.set_aspect('equal')

# Run animation
anim = animation.FuncAnimation(fig, animate_network, frames=100, 
                              interval=150, repeat=True)

plt.tight_layout()
plt.show()

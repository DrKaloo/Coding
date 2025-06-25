# I&F neuron simulation
import numpy as np
import matplotlib.pyplot as plt

# setup parameters
dt = 0.1        
T = 100         
V_thresh = 1.0      
V_rst = 0.0   
tau = 10.0    
I_app = 1.5     # increased this up to get spikes

t = np.arange(0, T, dt)
V = np.zeros(len(t))
spikes = []

# run simulation
for i in range(1, len(t)):
    V[i] = V[i-1] + dt * (-V[i-1] + I_app) / tau
    
    if V[i] >= V_thresh:
        spikes.append(t[i])
        V[i] = V_rst

print(f"Got {len(spikes)} spikes")
if spikes:
    print(f"First at {spikes[0]:.1f}ms, ISI = {np.mean(np.diff(spikes)):.1f}ms")

# plotting
plt.figure(figsize=(10,5))
plt.plot(t, V, 'b-')
plt.axhline(V_thresh, color='r', linestyle='--', alpha=0.7)
plt.xlabel('Time (ms)')
plt.ylabel('V')
plt.title('I&F Neuron')
plt.show()

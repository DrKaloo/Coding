#This model is a simplified abstraction of neuronal firing and helps illustrate core dynamics of
#membrane potential integration, firing thresholds, and reset mechanisms.

#Libraries used: NumPy, Matplotlib

#Future improvements:
# - Add variable input current or time-varying stimuli
# - Extend to include refractory period or spike output vector
# - Use real data for comparison or parametrisation



# Simple neuron model
import numpy as np
import matplotlib.pyplot as plt

# Setup
dt = 1  # time step
T = 100  # total time
steps = int(T/dt)
t = np.linspace(0, T, steps)
V = np.zeros(steps)  # voltage

# neuron params - playing around with these values
V_th = 1.0    
V_reset = 0.0   
I = 0.05      # input
tau_m = 10    # membrane time constant

# run simulation
for i in range(1, steps):
    # basic integration step
    dV = (I - V[i-1]) / tau_m * dt
    V[i] = V[i-1] + dV
    
    # check for spike
    if V[i] >= V_th:
        V[i] = V_reset

# plot
plt.figure(figsize=(10, 5))
plt.plot(t, V, 'b-', linewidth=1.5)
plt.axhline(V_th, color='red', linestyle='--', alpha=0.7)
plt.xlabel('Time (ms)')
plt.ylabel('Membrane potential')
plt.title('I&F Neuron')
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
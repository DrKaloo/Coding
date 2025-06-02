import numpy as np
import matplotlib.pyplot as plt

# Parameters
time = np.arange(0, 100, 1)           # Time in ms
voltage = np.zeros_like(time)        # Membrane voltage
threshold = 1.0                      # Firing threshold
reset = 0.0                          # Voltage reset value
input_current = 0.05                 # Constant input current
tau = 10                             # Membrane time constant

# Simulate integrate-and-fire
for t in range(1, len(time)):
    dv = (input_current - voltage[t-1]) / tau
    voltage[t] = voltage[t-1] + dv
    if voltage[t] >= threshold:
        voltage[t] = reset  # Reset after firing

# Plot the voltage over time
plt.figure(figsize=(8, 4))
plt.plot(time, voltage, label="Membrane Voltage")
plt.axhline(threshold, color='r', linestyle='--', label="Threshold")
plt.xlabel("Time (ms)")
plt.ylabel("Voltage")
plt.title("Integrate-and-Fire Neuron Simulation")
plt.legend()
plt.grid(True)
plt.show()

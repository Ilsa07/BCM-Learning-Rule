import numpy as np
from random import randrange
import matplotlib.pyplot as plt



# Simulation Parameters
# *********************
no_of_inputs = 2            # Number of inputs
T = 10**4                   # Simulation Length
dt = 1                      # Simulation time step
alpha = 10**(-6)            # Learning rate
ytarget = 10                # Output target
x = [[20, 0], [0, 20]]      # Input options
time_constant = 50          # Tau theta


# Initialisation
# **************
y = np.zeros(T)                     # Initialise output vector as 0s
w = np.full((T, no_of_inputs), 0.5) # Initialise the weights as 0.5
theta = [5]*T                       # Initialise the threshold as 5


# Run the Simulation
# ******************
for t in range(T-1):
    # Randomly choose the input to the neurons
    choice = randrange(2)

    # The output is vector multiplication of weights and input
    y[t] = np.array(w[t]).dot(np.array(x[choice]))

    # Update the Threshold
    theta[t+1] = theta[t] + dt/time_constant * (y[t]**2/ytarget - theta[t])

    # Update the weights for the next time step
    for iterator in range(2):
        updated_weight = w[t][iterator] + alpha * x[choice][iterator]*y[t] * (y[t] - theta[t])

        # Apply the boundary to the new weights
        if updated_weight < 0:
            updated_weight = 0

        w[t+1][iterator] = updated_weight


# Plot the results of the simulation
# **********************************
fig, (ax1, ax2, ax3) = plt.subplots(3)
fig.suptitle('Simulation Results')

ax1.plot(w)
ax1.set(xlabel = 'Time (ms)')
ax1.set(ylabel = 'Synaptic Weight W')

ax2.plot(theta)
ax2.set(xlabel = 'Time (ms)')
ax2.set(ylabel = 'Synaptic Threshold Theta')

ax3.scatter(list(range(T)), y)
ax3.set(xlabel = 'Time (ms)')
ax3.set(ylabel = 'Output Magnitude')
plt.show()
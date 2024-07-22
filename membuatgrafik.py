import matplotlib.pyplot as plt
import numpy as np

# Data
iterasi = np.arange(1, 46, 1)
x = 1 - np.exp(-0.1 * iterasi)
xnew = 1 - np.exp(-0.1 * (iterasi - 1))

# Plotting
plt.figure()
plt.plot(iterasi, x, 'bo-', label='x')
plt.plot(iterasi, xnew, 'r.-', label='xnew')
plt.xlabel('iterasi')
plt.ylabel('x')
plt.legend()
plt.grid(True)
plt.show()

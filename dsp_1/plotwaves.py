import numpy as np
import matplotlib.pyplot as plt

# Time axis
n = np.arange(-20, 21)
f=2
fs=100

# Basic signals
delta = np.where(n == 0, 1, 0)
step = np.where(n >= 0, 1, 0)
sine = np.sin(2 * np.pi * n*f/fs)

# Plot the 3 input signals
plt.figure(figsize=(10, 6))

plt.subplot(3, 1, 1)
plt.stem(n, delta)
plt.title("Impulse Signal (δ[n])")
plt.grid()

plt.subplot(3, 1, 2)
plt.stem(n, step)
plt.title("Step Signal (u[n])")
plt.grid()

plt.subplot(3, 1, 3)
plt.stem(n, sine)
plt.title("Sine Signal (sin(0.2πn))")
plt.grid()

plt.tight_layout()
plt.show()

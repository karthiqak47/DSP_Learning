# Define the difference equation system
def difference_eq(x):
    y = np.zeros_like(x, dtype=float)
    for i in range(1, len(x)):
        y[i] = 0.3 * y[i - 1] + x[i]
    return y

# Outputs from difference equation
h = difference_eq(delta)
y_step = difference_eq(step)
y_sine = difference_eq(sine)

# Plot outputs from difference equation
plt.figure(figsize=(10, 6))

plt.subplot(3, 1, 1)
plt.stem(n, h)
plt.title("Impulse Response h[n] (from difference eq)")
plt.grid()

plt.subplot(3, 1, 2)
plt.stem(n, y_step)
plt.title("Output for Step Input (via difference eq)")
plt.grid()

plt.subplot(3, 1, 3)
plt.stem(n, y_sine)
plt.title("Output for Sine Input (via difference eq)")
plt.grid()

plt.tight_layout()
plt.show()

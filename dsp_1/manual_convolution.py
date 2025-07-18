# Manual convolution function
def manual_convolution(x, h):
    N = len(x) + len(h) - 1
    y = np.zeros(N)
    for i in range(N):
        for k in range(len(x)):
            if 0 <= i - k < len(h):
                y[i] += x[k] * h[i - k]
    return y

# Manual convolution outputs
conv_step = manual_convolution(step, h)
conv_sine = manual_convolution(sine, h)
n_conv = np.arange(2 * n[0], 2 * n[-1] + 1)

# Plot outputs from manual convolution
plt.figure(figsize=(10, 5))

plt.subplot(2, 1, 1)
plt.stem(n_conv, conv_step)
plt.title("Output for Step Input (via manual convolution)")
plt.grid()

plt.subplot(2, 1, 2)
plt.stem(n_conv, conv_sine)
plt.title("Output for Sine Input (via manual convolution)")
plt.grid()

plt.tight_layout()
plt.show()

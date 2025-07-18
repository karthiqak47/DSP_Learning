n = np.arange(0, 100)
clean_signal = np.sin(2 * np.pi * n*f/fs)

# Gaussian Noise
np.random.seed(0)
noise = np.random.normal(0, 0.3, size=clean_signal.shape)
noisy_signal = clean_signal + noise

def low_pass_filter(x, alpha):
    y = np.zeros_like(x)
    for i in range(1, len(x)):
        y[i] = (1 - alpha) * y[i - 1] + alpha * x[i]
    return y

# Filter outputs for different alpha values
filtered_01 = low_pass_filter(noisy_signal, alpha=0.1)
filtered_03 = low_pass_filter(noisy_signal, alpha=0.3)
filtered_07 = low_pass_filter(noisy_signal, alpha=0.7)
def plot_filtered(alpha, filtered):
    plt.figure()
    plt.stem(n, clean_signal, 'g', label='Clean Signal')
    plt.stem(n, noisy_signal, 'r', label='Noisy Signal')
    plt.stem(n, filtered, 'b', label=f'Filtered (α={alpha})')
    plt.title(f'Low-Pass Filtering with α = {alpha}')
    plt.xlabel('n')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.grid(True)
    plt.show()

plot_filtered(0.1, filtered_01)
plot_filtered(0.3, filtered_03)
plot_filtered(0.7, filtered_07)

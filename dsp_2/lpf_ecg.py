y=ecg.copy()
fft_new=fft.copy()
fft_freq=freq.copy()
print(fft_freq)
for i in range(len(fft_new)):
    if (fft_freq[i])>40:
        fft_new[i]=0
print(fft_new)
iff=np.fft.ifft(fft_new)
plt.figure(figsize=(10,5))
plt.plot(t,ecg,label="original")
plt.plot(t,iff,label="filtered")
plt.xlabel("Time(s)")
plt.ylabel("EMG")
plt.grid()
plt.legend()
plt.show()

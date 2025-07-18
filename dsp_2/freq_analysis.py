X=np.fft.fft(ecg)
freq=np.fft.fftfreq(N_new,d=1/Fs)
print(freq)
print(freq[-3])
plt.stem(freq[:N_new//2],np.abs(X[:N_new//2]))
plt.xlabel("Frequency")
plt.ylabel("FFT(Magnitude)")
plt.show()

index=np.argmax(np.abs(X[:N_new//2]))
b=np.argmax(np.abs(X[index+1:N_new//2]))
req_freq=freq[index]
heart_beat=60*req_freq
print("Highest frequency component = ",req_freq)
print("Heartbeat= ", heart_beat)
print("freq2=",freq[b])


N_new=len(ecg)
fft=np.fft.fft(ecg)
ecg1=ecg.copy()
e_t= np.sum(np.abs(ecg)**2)
e_f= (1/N_new)*np.sum(np.abs(fft)**2)

print(e_t,"time energy")
print(e_f,"freq energy")

from time import time
N_val=[2,4,8,16,64,128,256,512,1024]

def fft_matrix(N):
    w=np.zeros((N,N),dtype=complex)
    for i in range(N):
        for j in range(N):
            w[i,j]=np.exp(-2j*np.pi*i*j*(1/N))
    return w


fft_time=[]
matrix_time=[]

for i in N_val:
    start=time()
    m=fft_matrix(i)
    fft_m= m@ecg[:i]
    matrix_time.append(time()-start)

    nstart=time()
    fft=np.fft.fft(ecg)
    fft_time.append(time()-nstart)


plt.plot(N_val,fft_time,label="fft_np")
plt.plot(N_val,matrix_time,label="matrix_fft")
plt.xlabel("N values")
plt.ylabel("Time(s)")
plt.legend()
plt.show()
            

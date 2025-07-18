import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv("ecg_signal.csv")
t=df["Time (s)"].values
ecg=df["ECG (mV)"].values
Fs=1/(t[1]-t[0])
n_4sec=int(Fs*4)
print(Fs)
print(n_4sec)
plt.figure(figsize=(12,5))
plt.plot(t[:n_4sec],ecg[:n_4sec])
plt.xlabel("Time (s)")
plt.ylabel("ECG")
plt.show()

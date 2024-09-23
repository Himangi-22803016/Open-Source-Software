import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt

time = np.linspace(0, 24, 1440) 
vehicle_count = np.linspace(0, 50, 1440)
noise = np.random.randint(0, 50, 1440)

freq = 0.1
order = 3
b,a = butter(order, freq)

#reduce noise
smoothed_data = filtfilt(b, a, noise)
hourly_av = np.mean(smoothed_data.reshape(24, 60), axis=1)

plt.plot(time, noise, color='red', label="Noise")
plt.plot(time, smoothed_data, color='skyblue', label="Smoothed Data")
plt.plot(np.arange(24), hourly_av, color='green', label="Average vehicles per hour")
#plt.legend()
plt.show()

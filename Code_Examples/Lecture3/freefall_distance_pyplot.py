import numpy as np
import matplotlib.pyplot as plt

time = np.arange(0., 10., 0.2)
velocity = np.zeros_like(time, dtype=float)
distance = np.zeros_like(time, dtype=float)

g = 9.8

velocity = g * time
distance = 0.5 * g * np.power(time, 2)

plt.figure(figsize=(9,7), dpi=100)
plt.plot(time,distance,'bo-')
plt.xlabel("Time")
plt.ylabel("Distance")
plt.legend(["Distance"])
plt.grid(True)
plt.show()
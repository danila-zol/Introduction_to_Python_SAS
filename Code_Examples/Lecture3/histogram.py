import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng()
data = rng.normal(0, 1, 1000)

fig, ax1 = plt.subplots()
ax1.hist(data)
plt.show()
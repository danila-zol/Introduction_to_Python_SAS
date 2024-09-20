import matplotlib.pyplot as plt
import numpy.random as npr

fig, ax = plt.subplots()
ax.scatter(npr.random_sample(20), npr.random_sample(20))

plt.show()
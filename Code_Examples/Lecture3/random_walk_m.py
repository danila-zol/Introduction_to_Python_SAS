# One of my first programs!
#   -- Danila

from random import choice
import matplotlib.pyplot as plt

x_value=0
y_value=0
points=choice([3,4])
num_steps='1000'
x=[x_value]
y=[y_value]
for step in range(0, int(num_steps)):
    x_chge=choice([1, -1])
    y_chge=choice([1, -1])
    
    x_value=int(x_value) + int(x_chge)
    y_value=int(y_value) + int(y_chge)
    
    x.append(x_value)
    y.append(y_value)

plt.axis('off')
plt.plot(x,y)
plt.scatter(0, 0, c='green', s=70)
plt.scatter(x[-1],y[-1], c='red', s=70)
plt.show()

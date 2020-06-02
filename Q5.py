# Q5 To create random numbers using Box Muller method according to Gaussian distribution

import numpy as np
import matplotlib.pyplot as plt

def dist(x):
	return np.exp(-(x**2)/2)/np.sqrt(2*np.pi)


x = np.arange(-10,10,0.1)
pdf = dist(x)   # Uniform pdf


#For Box Muller method
x1 = np.random.rand(10000)
x2 = np.random.rand(10000)
z1 = np.sqrt(-2*np.log(x1))*np.cos(2*np.pi*x2)
z2 = np.sqrt(-2*np.log(x1))*np.sin(2*np.pi*x2)

# For plot
plt.hist(z1, bins=20, histtype='step',density=True,color='r',label="PDF of 1st random number variable of Box Muller method")
plt.hist(z2, bins=20, histtype='step',density=True,color='b',label="PDF of 2nd random number variable of Box Muller method")
plt.plot(x,pdf,color='g',label="PDF of uniform random number")
plt.xlabel("x")
plt.ylabel('Probability distribution')
plt.title('Density Histogram')
plt.legend()
plt.show()
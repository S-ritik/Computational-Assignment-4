# Q6 - Using rejection method to produce random numbers

import numpy as np
import matplotlib.pyplot as plt


def f(x):  # Given Distribution
	return np.sqrt(2/np.pi)*np.exp(-(x**2)/2)

def F(x):  # Envelope
	return 1.5*np.exp(-x)


x1=np.arange(0, 10, 0.01)
x=np.random.rand(1000)
x=-np.log(x)
y=np.random.rand(1000)*F(x)
x_g=x[y<f(x)]
x_b=x[y>f(x)]
y_g=y[y<f(x)]
y_b=y[y>f(x)]
bin=np.histogram(x_g)

plt.hist(x_g,bins=20, histtype='stepfilled',density=True,color='g',label="PDF of random.rand numbers")

plt.plot(x1, f(x1),'b', label= 'Given PDF')
plt.xlabel("x")
plt.ylabel('Probability distribution')
plt.title('Density Histogram')
plt.legend()
plt.show()
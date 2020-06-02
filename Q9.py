# Q9 - To get sample using MCMC

import numpy as np
import matplotlib.pyplot as plt

def f(x):  # Given Distribution
	if (x<7 and x>3):
		return 1
	else:
		return 0

t=np.linspace(-10,10,10000)
pdf=np.zeros(len(t))

nsteps = 10000
x=np.zeros(10000)
x[0]=5.0


for i in range(nsteps-1):
	pdf[i]=f(t[i])/4  # PLotting the given distribution
	y=x[i] + np.random.normal(loc=0, scale=2)
	r=np.random.rand()
	if(f(y)/f(x[i])>r):
		x[i+1]=y
	else:
		x[i+1]=x[i]

# For plotting Markov Chain
plt.plot(x,ls='--',color='g',label="Markov Chain")
plt.xlabel("i th step")
plt.ylabel("Value")
plt.legend()
plt.show()

# For ploting probability distrubtion
plt.hist(x, bins=20, histtype='step',density=True,color='r',label="PDF using MCMC")
plt.plot(t,pdf,color='g',label="PDF of given distribution")
plt.xlabel("x")
plt.ylabel('Probability distribution')
plt.title('Density Histogram')
plt.legend()
plt.show()
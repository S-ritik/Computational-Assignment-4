# Q8 - To integrate using Monte Carlo integration 

import numpy as np


def integral(d):
	count=0
	for i in range(500000):
	f=np.random.uniform(-1,1,d)
	dist=np.sum(np.multiply(f,f))
	if(dist<=1):
		count=count+1
	return (2**d)*(count/(i+1))
print("Area of Circle = ",integral(2))
print("Volume of 10-d hypersphere = ",integral(10))

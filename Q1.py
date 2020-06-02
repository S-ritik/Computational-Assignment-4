# Q1 - To make linear congruential random number generator

import numpy as np
import matplotlib.pyplot as plt
import time


n=10000
c=980384626
a=8103512450 
m=2**32
rand=np.zeros(n)
t1 = time.time()
rand[0]=1
for i in range(1,n):
	rand[i]=((a*rand[i-1]+c)%m)/m
t2=time.time()
x=np.linspace(0,1,10000)
pdf=np.full(n,1)
print("Time taken =",t2-t1)
plt.hist(rand, bins=20, histtype='step',density=True,color='r',label="PDF of liner congruential random number")
plt.plot(x,pdf,color='g',label="PDF of uniform random number")
plt.xlabel("i")
plt.ylabel('Probability density')
plt.title('Density Histogram')
plt.legend()
plt.show()
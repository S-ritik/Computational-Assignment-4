# Q2- To make random numbers using random.rand
import numpy as np
import matplotlib.pyplot as plt
import time

t1 = time.time()
rand=np.random.rand(10000)
t2=time.time()
print('Time=', t2-t1)
print(rand)
x=np.linspace(0,1,10000)
pdf=np.full(10000,1)
plt.hist(rand, bins=20, histtype='step',density=True,color='r',label="PDF of random.rand numbers")
plt.plot(x,pdf,color='g',label="PDF of uniform random number")
plt.xlabel("x")
plt.ylabel('Probability distribution')
plt.title('Density Histogram')
plt.legend()
plt.show()
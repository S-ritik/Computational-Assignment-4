# Q10- To fit data using MCMC 

import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt
import emcee
import corner

def pr(x):   # For prior
	a, b, c=x
	if(a>-500 and a<500 and b>-500 and b<500 and c>-500 and c<500):
		return 0
	else:
		return -np.inf


def llh(x0, x, y, sigma):  # For likelihood  
	a,b,c=x0
	model = a*(x**2) + b*x + c
	sigma2 = sigma**2
	return 0.5 * np.sum((y - model) ** 2 / sigma2 + np.log(2 * np.pi * sigma2))

def prob(x0, x, y, sigma):     # For posterior
	lp = pr(x0)
	if not np.isfinite(lp):
		return -np.inf
	else:
		return lp - llh(x0, x, y, sigma)



data=np.loadtxt('data.txt',skiprows=5,delimiter='&')
x=data[:, 1]
y=data[:, 2]
sigma=data[:, 3]



inital=(1,10,100)
fsol = minimize(llh,inital,args=(x,y,sigma))
n=50
d=3
pos=fsol.x +10**-4 * np.random.randn(n, d)

samplerun = emcee.EnsembleSampler(50, 3, prob, args=(x, y, sigma))
samplerun.run_mcmc(pos, 4000)
s=samplerun.get_chain()


# Plotting MC chains
plt.subplot(3, 1, 1)
plt.plot(s[:, :, 0], 'r',label="Marcov chains for a") 
plt.legend()
plt.ylabel("a")
plt.xlabel("Number of itretaions")
plt.subplot(3, 1, 2)
plt.plot(s[:, :, 1], 'b',label="Marcov chains for a") 
plt.legend() 
plt.ylabel("b")
plt.xlabel("Number of itretaions")
plt.subplot(3, 1, 3)
plt.plot(s[:, :, 2], 'g',label="Marcov chains for a")  
plt.legend()
plt.ylabel("c")
plt.xlabel("Number of itretaions")
plt.show()

# Taking 50 burn in points
samp = np.zeros([197500, 3])
samp[:, 0] = s[50:4000, :, 0].reshape((197500))
samp[:, 1] = s[50:4000, :, 1].reshape((197500))
samp[:, 2] = s[50:4000, :, 2].reshape((197500))
medians = np.median(samp, axis=0)
asol, bsol, csol = medians


# Plotting corner histogram with best fit and one-sigma values
fig = corner.corner(samp, labels=['a', 'b', 'c'], truths=[asol, bsol, csol], show_titles=True)

# Plotting model vs data
plt.errorbar(x, y, yerr=sigma)
xsol = np.linspace(np.min(x), np.max(x), 1000)
ysol = asol*(xsol**2) + bsol*xsol + csol
for i in np.random.randint(170000, size=100):
	yd = samp[i, 0]*(xsol**2) + samp[i, 1]*xsol + samp[i, 2]
	plt.plot(xsol, yd, 'r')

plt.plot(xsol, ysol, 'b', label="Fit")
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.show()

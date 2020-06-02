# Q7 - To apply χ^2 test

import numpy as np
from scipy import stats

def result(p):
	if p<1:
		print('Not Sufficiently Random')
	elif p>1 and p<5:
		print('suspect')
	elif p>5 and p<10:
		print('almost Suspect')
	else:
		print('sufficiently Random')

def test(sample): # To apply test
	n=np.sum(sample)
	s=np.array([n/36,2*n/36,3*n/36,4*n/36,5*n/36,6*n/36,5*n/36,4*n/36,3*n/36,2*n/36,n/36]) #  Statistical sample
	l=((sample-s)**2)/s
	ls=np.sum(l)
	p=(1-stats.chi2.cdf(ls,len(sample)-1))*100
	result(p)


s1=np.array([4, 10, 10, 13, 20, 18, 18, 11, 13, 14, 13]) # sample 1
s2 = np.array([3, 7, 11, 15, 19, 24, 21, 17, 13, 9, 5]) # sample 2

test(s1)
test(s2)
#http://projecteuler.net/problem=47
#Distinct primes factors
#by Alexandre Pinto

import math

def findFirstFour(upperbound):
	
	factors=findFactors(upperbound)

	consec=4
	for i in xrange(1,upperbound):			#search
		distinct=True
		for j in xrange(i,i+consec):
			if(factors[j]<consec):
				distinct=False
		if(distinct==True):
			return i
	return 0

def findFactors(n):				#generate a list of numbers representing the number of distinct prime factors

	nfactors=n*[0]

	for i in xrange(2,n):
		if nfactors[i]==0:
			for j in xrange(i,n,i):
				nfactors[j]+=1

	return nfactors

if __name__ == '__main__':
	
	print findFirstFour(150000)


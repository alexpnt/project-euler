#http://projecteuler.net/problem=46
#Goldbach's other conjecture
#by Alexandre Pinto

import math
def findSmallestOdd(upperbound):

	primes=findPrimes(upperbound)
	odds=genOddComposites(upperbound)

	for i in odds:
		if testConjecture(i,primes)==0:
			return i
	return 0

def testConjecture(n,primes):

	maxSquare=int(math.sqrt(n/2))		#get the max posible value for the square

	j=0
	while primes[j]<n:
		for i in xrange(1,maxSquare+1):
			if(n==primes[j]+2*i**2):
				# print str(n)+'='+str(primes[j])+'+2*'+str(i)+'^2'
				return 1
		j+=1
	return 0



def findPrimes(n):				#generate a list of primes, using the sieve of eratosthenes

	primes=(n+2)*[True]

	for i in xrange(2,int(math.sqrt(n))+1):
		if primes[i]==True:
			for j in xrange(i**2,n+1,i):
				primes[j]=False

	primes=[i for i in xrange(2,len(primes)-1) if primes[i]==True]
	return primes

def genOddComposites(n):		#generate a list of odd composite numbers, using the sieve of eratosthenes

	odds=(n+2)*[True]

	for i in xrange(2,int(math.sqrt(n))+1):
		if odds[i]==True:
			for j in xrange(i**2,n+1,i):
				odds[j]=False

	odds=[i for i in xrange(2,len(odds)-1) if odds[i]==False and i%2==1]
	return odds

if __name__ == '__main__':
	print findSmallestOdd(6000)

#http://projecteuler.net/problem=23
#Non-abundant sums
#by Alexandre Pinto

import math

def calcSums(n,primes):	#generate all the combinations

	abundants=findAbundant(n,primes)
	i=j=0
	sums=set()
	for i in range(0,len(abundants)):
		for j in range(i,len(abundants)):
			sums.update([abundants[i]+abundants[j]])	#save possible sum
	return sums

def findAbundant(n,primes):		#generate the abundant numbers
	ab=[]
	for i in range(1,n+1):
		if (d(i,primes)-i)>i:	#abundant number property
			ab.append(i)
	return ab

def d(n,primes):				#sum of proper divisors

	prod=1
	factors=primeFactorization(n,primes);
	while(len(factors)>0):					
		counter=factors.count(factors[0])
		prod*=sigma(factors[0],counter)			#multiplicativity property of the sigma function
		for i in range(0,counter):
			factors.remove(factors[0])
	return prod

def sigma(p,n):					#sigma(n,p) is the sum of divisors of the natural number, p. p is a also a prime.
	return (p**(n+1)-1)/(p-1)	

def findPrimes(n):				#generate a list of primes, using the sieve of eratosthenes

	primes=(n+2)*[True]

	for i in range(2,int(math.sqrt(n))+1):
		if primes[i]==True:
			for j in range(i**2,n+1,i):
				primes[j]=False

	primes=[i for i in range(2,len(primes)-1) if primes[i]==True]
	return primes

def primeFactorization(n,primes):	#find the factors of a number

	factors=[]

	i=0
	while(n!=1):
		if(n%primes[i]==0):
			factors.append(primes[i])
			n/=primes[i]
		else:
			i+=1

	return factors

if __name__ == '__main__':

	sum=0
	primes=findPrimes(100000)	#upper bound for the number of primes
	abundantSums=calcSums(20162,primes)	#Every number greater than 20161 can be expressed as a sum of two abundant numbers
	for i in range(1,20162):
		if i not in abundantSums:
			sum+=i
	print sum


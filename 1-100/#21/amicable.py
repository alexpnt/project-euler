#http://projecteuler.net/problem=21
#Amicable numbers
#by Alexandre Pinto

import math

def isAmicable(a,primes):
	b=d(a,primes)-a
	if(a==d(a,primes)-a):return 0
	if(a==(d(b,primes)-b)):		#a pair of amicable numbers
		return 1
	return 0

def d(n,primes):	#sum of proper divisors

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
	i=2
	primes=findPrimes(100000)	#upper bound for the number of primes
	while(i<10000):
		if isAmicable(i,primes)==1:
			sum+=i
			# print i
		i+=1

	print sum


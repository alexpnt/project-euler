#http://projecteuler.net/problem=12
#Highly divisible triangular number
#by Alexandre Pinto

import math

def triangular(n,primes):

	tri=n*(n+1)/2
	factors=primeFactorization(tri,primes);		#prime factors

	ndiv=1
	while(len(factors)>0):					
		counter=factors.count(factors[0])
		ndiv*=(counter+1)						#sum up the exponents, that's the answer 
		for i in range(0,counter):
			factors.remove(factors[0])

	return [tri,ndiv]

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
	
	i=1
	candidate=[1,1]
	primes=findPrimes(20000)	#upper bound for the number of primes
	while(candidate[1]<=500):				
		candidate=triangular(i,primes)
		i+=1
	print candidate[0]


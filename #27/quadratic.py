#http://projecteuler.net/problem=27
#Quadratic primes
#by Alexandre Pinto

import math

def quadraticPrimes():
	primes=findPrimes(100000)	#upper bound for the number of primes

	prod=1
	best=0
	for i in range(-1000,1001):			#brute force
		for j in range(-1000,1001):
			n=0
			counter=0
			if((1+i+j)%2==1 and isPrime(j,primes)==1):	 #every prime number, except for 2, is odd. Also, for n=0, b must be prime
				while isPrime(n**2+i*n+j,primes)==1:
					n+=1
					counter+=1
					if(counter>best):
						best=counter
						besti=i
						bestj=j
						prod=i*j
	return besti,bestj,prod

def isPrime(n,primes):
    
    i = 0;
    while(primes[i]<=n):
        if(primes[i]==n):
            return 1
        i+=1;
    return 0;

def findPrimes(n):				#generate a list of primes, using the sieve of eratosthenes

	primes=(n+2)*[True]

	for i in range(2,int(math.sqrt(n))+1):
		if primes[i]==True:
			for j in range(i**2,n+1,i):
				primes[j]=False

	primes=[i for i in range(2,len(primes)-1) if primes[i]==True]
	return primes

if __name__ == '__main__':
	print quadraticPrimes()
	

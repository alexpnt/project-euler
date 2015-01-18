#http://projecteuler.net/problem=37
#Truncatable primes
#by Alexandre Pinto

import math,re
def findSum():
	
	sum=0
	primes=findPrimes(1000000)
	for i in xrange(11,1000000):
		if i%2!=0 and isTruncablePrime(i,primes)==1:
			#print i
			sum+=i

	return sum

def isTruncablePrime(n,primes):

	for i in xrange(0,len(str(n))):	#remove digits from left to right
		test=int(str(n)[i:])
		if binary_search(primes,test)==-1:
			return 0

	while(n!=0):					#remove digits from right to left
		if binary_search(primes,n)==-1:
			return 0
		n/=10	
	return 1

def findPrimes(n):				#generate a list of primes, using the sieve of eratosthenes

	primes=(n+2)*[True]

	for i in xrange(2,int(math.sqrt(n))+1):
		if primes[i]==True:
			for j in xrange(i**2,n+1,i):
				primes[j]=False

	primes=[i for i in xrange(2,len(primes)-1) if primes[i]==True]
	return primes

#perform a binary search
def binary_search(l, target):
    low=0
    high = len(l)
    while low < high:
        mid = (low+high)//2
        midval = l[mid]
        if midval < target:
            low = mid+1
        elif midval > target: 
            high = mid
        else:
            return mid
    return -1


if __name__ == '__main__':
	print findSum()

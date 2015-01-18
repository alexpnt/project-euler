#http://projecteuler.net/problem=49
#Prime permutations
#by Alexandre Pinto

import math

def find4digit():
	
	primes=findPrimes(9999)
	l=len(primes)
	counter=0
	for i in xrange(0,l):			#search
		for j in xrange(i+1,l):
			if(set(list(str(primes[i])))==set(list(str(primes[j])))):
				expected=primes[j]+(primes[j]-primes[i])
				if(binary_search(primes,expected)!=-1 and set(list(str(primes[i])))==set(list(str(expected)))):
						print int(str(primes[i])+str(primes[j])+str(expected))
						counter+=1
						if(counter==2):return
	return 0

def findPrimes(n):				#generate a list of primes, using the sieve of eratosthenes

	primes=(n+2)*[True]

	for i in xrange(2,int(math.sqrt(n))+1):
		if primes[i]==True:
			for j in xrange(i**2,n+1,i):
				primes[j]=False

	primes=[i for i in xrange(2,len(primes)-1) if primes[i]==True and i>=1000 and i<=9999]
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
	
	print find4digit()


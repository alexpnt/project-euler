#http://projecteuler.net/problem=50
#Consecutive prime sum
#by Alexandre Pinto

import math

def findPrime():
	
	primes=findPrimes(1000000)
	length=len(primes)
	summations=[0]*length
	summations[0]=primes[0]
	mPrime=0
	mlen=0

	for i in xrange(1,length):							#cumulative sums
		summations[i]+=summations[i-1]+primes[i]
		if(summations[i]>primes[length-1]):
			break
		if(binary_search(primes,summations[i])!=-1):
			mPrime=summations[i]
			mlen=i+1


	count=0
	diff=[[0]*length]*length
	for i in xrange(0,length):								#search differences
		for j in xrange(i+mlen,length):
			diff[i][j]=summations[j]-summations[i-1]
			l=j-i+1
			if(diff[i][j]>primes[length-1]):
				break
			if diff[i][j]%2==0:
				continue
			if(binary_search(primes,diff[i][j])!=-1 and l>mlen):
				mPrime=diff[i][j]
				mlen=l
				count+=1
				if(count==3):
					return mPrime
		
	return mPrime

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
	
	print findPrime()


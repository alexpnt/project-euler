#http://projecteuler.net/problem=35
#Circular primes
#by Alexandre Pinto

import math,numpy,re
def countCircularPrimes(limit):
	
	counter=1
	primes=findPrimes(1000000)
	for i in xrange(2,limit):
		if(i%2!=0 and (i<=9 or (i>9 and not re.findall('[0,2,4,5,6,8]+',str(i)))) and isCircular(i,primes)==1): #only consider combinations of 1,3,7,9
			#print i 																							#if the number has at least 2 digits
			counter+=1
	return counter

def isCircular(n,primes):

	l=nLength(n)
	while(l!=0):	
		rotated=list(numpy.roll(list(str(n)),int(-l)))	#rotate
		num=int(''.join(rotated))						
		if(binary_search(primes,num)==-1):				#check if its a prime number
			return 0
		l-=1

	return 1

def findPrimes(n):				#generate a list of primes, using the sieve of eratosthenes

	primes=(n+2)*[True]

	for i in range(2,int(math.sqrt(n))+1):
		if primes[i]==True:
			for j in range(i**2,n+1,i):
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

#returns the length of a given number
def nLength(n):
	return math.floor(math.log(n,10))+1

if __name__ == '__main__':
	print countCircularPrimes(1000000)

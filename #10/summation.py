#http://projecteuler.net/problem=10
#Summation of primes
#by Alexandre Pinto

import math

def findSum(n):

	sum=0
	list=(n+2)*[True]

	for i in range(2,int(math.sqrt(n))+1):		#generate a list of primes, using the sieve of eratosthenes
		if list[i]==True:
			for j in range(i**2,n+1,i):
				list[j]=False

	index=0
	for i in range(2,len(list)-1):
		if list[i]==True:						#is a prime
			index+=1
			# print "%d: %d" %(index,i)
			sum+=i

	return sum

if __name__ == '__main__':
	print findSum(2000000)

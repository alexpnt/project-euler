#http://projecteuler.net/problem=32
#Pandigital products
#by Alexandre Pinto

import math

def findSum(upperBound):

	sum=0
	for i in xrange(1000,upperBound):	#brute force
		if(isPanProduct(i)==1):
			sum+=i
	return sum


def isPanProduct(n):

	previous=0
	for i in xrange(1,n+1):
		if(n%i==0):
			array=[0]*9														#boolean array used to check if a number is a pandigit
			multiplier=i
			multiplicand=n/i
			if(multiplier==previous):break									#avoid repetitions	
			previous=multiplicand
			pan=mergeIntegers(n,multiplier,multiplicand)					#merge integers
			if(nLength(pan)==9 and set(str(pan))==set('123456789')):		#be sure its 9 digit lenght
				print str(n)+" = "+str(multiplier)+"x"+str(multiplicand) 	#solutions
				return 1
	return 0



#returns the length of a given number
def nLength(n):
	return math.floor(math.log(n,10))+1

#merge the given integer values
def mergeIntegers(a,b,c):
	return int(str(a)+str(b)+str(c))


if __name__ == '__main__':
	print findSum(8000)

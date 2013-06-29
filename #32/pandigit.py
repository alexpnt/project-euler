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
			if(nLength(pan)==9):											#be sure its 9 digit lenght
				while(pan!=0):
					array[pan%10-1]=1 										#mark that position
					pan/=10
				if(sum(array)==9):											#check if product is a pandigit	
					for l in str(mergeIntegers(n,multiplier,multiplicand)):	#check if product doesnt have any 0
						if(l=='0'):
							return 0
					print str(n)+" = "+str(multiplier)+"x"+str(multiplicand) #solutions
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

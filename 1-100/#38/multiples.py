#http://projecteuler.net/problem=38
#Pandigital multiples
#by Alexandre Pinto

import math
def findBiggestPan():
	m=0
	for i in xrange(193,1000000):
		n=i
		j=2
		while(nLength(n)<10):
			n=mergeIntegers(n,i*j)
			if(nLength(n)==9 and set(str(n))==set('123456789') and n>m):
				m=n
				break
	 		j+=1

	return m

def isPanDigit(n):

	original=n
	array=[0]*9													#boolean array used to check if a number is a pandigit
	while(n!=0):
		array[n%10-1]=1 										#mark that position
		n/=10
	if(sum(array)==9):											#check if number is a pandigit	
		for l in str(original):									#check if numbre doesnt have any 0
			if(l=='0'):
				return 0
		return 1
	return 0



#returns the length of a given number
def nLength(n):
	return math.floor(math.log(n,10))+1

#merge the given integer values
def mergeIntegers(a,b):
	return int(str(a)+str(b))

if __name__ == '__main__':
	print findBiggestPan()

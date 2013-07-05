#http://projecteuler.net/problem=45
#Triangular, pentagonal, and hexagonal
#by Alexandre Pinto

import sys,math
def nextTri(upperbound):
	
	for i in xrange(286,upperbound):
		h=int(i*(2*i-1))
		if(isPentagonal(h)==True):
			return h

def isPentagonal(x):				#check whether a number is a pentagonal number or not
	test=(math.sqrt(24*x+1)+1)/6
	return test==int(test)

if __name__ == '__main__':
	print nextTri(30000)

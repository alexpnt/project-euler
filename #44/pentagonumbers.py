#http://projecteuler.net/problem=44
#Pentagon numbers
#by Alexandre Pinto

import sys,math
def findD():
	D=sys.maxint
	N=2200
	penta=genPentagonalNumbers(N)
	for i in xrange(0,N):
		for j in xrange(i+1,N):
			s=penta[i]+penta[j]
			d=abs(penta[i]-penta[j])
			if isPentagonal(s)==True and isPentagonal(d)==True and d<D:
				D=d
				return D

def isPentagonal(x):				#check whether a number is a pentagonal number or not
	test=(math.sqrt(24*x+1)+1)/6
	return test==int(test)

def genPentagonalNumbers(n):

	penta=[]
	for i in xrange(1,n+1):
		penta+=[int(i*(3*i-1)/2)]
	return penta

if __name__ == '__main__':
	print findD()

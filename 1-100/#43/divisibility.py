#http://projecteuler.net/problem=43
#Sub-string divisibility
#by Alexandre Pinto

import math,itertools,operator

def findSum():
	s=0
	perm=list(itertools.permutations([0,1,2,3,4,5,6,7,8,9]))	#generate all 0 to 9 pandigital numbers
	divisors=[2,3,5,7,11,13,17]
	for p in perm:
		divisible=True
		for i in xrange(1,8):				#test property
			if(div(p[i],p[i+1],p[i+2],divisors[i-1])!=0):
				divisible=False
				break
		if(divisible==True):
			s+=int(''.join(map(str,p)))		#sum up
	return s
def div(d1,d2,d3,divisor):
	return (d1*100+d2*10+d3)%divisor

if __name__ == '__main__':
	print findSum()

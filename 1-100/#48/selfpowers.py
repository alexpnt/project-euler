#http://projecteuler.net/problem=48
#Self powers
#by Alexandre Pinto

import math
def selfPower(nth):
	
	s=0
	for i in xrange(1,nth+1):
		s+=i**i
	return s
if __name__ == '__main__':
	print selfPower(1000)%10**10

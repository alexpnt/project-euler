#http://projecteuler.net/problem=20
#Factorial digit sum
#by Alexandre Pinto

import math
def sum(n):
	sum=0
	for l in str(math.factorial(n)):
		sum+=int(l)
	return sum
if __name__ == '__main__':
	print sum(100)	

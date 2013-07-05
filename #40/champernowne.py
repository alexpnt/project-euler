#http://projecteuler.net/problem=40
#Champernowne's constant
#by Alexandre Pinto
import math
def d(n):

	product=1
	counter=1
	for i in xrange(1,n+1):
		for d in str(i):
			if(counter==1 or counter==10 or counter==100 or counter==1000 or counter==10000 or counter==100000 or counter==1000000):
				# print d,counter
				product*=int(d)
			counter+=1
	return product

#returns the length of a given number
def nLength(n):
	return int(math.floor(math.log(n,10))+1)

if __name__ == '__main__':

	print d(1000000)

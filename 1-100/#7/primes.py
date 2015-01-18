#http://projecteuler.net/problem=7
#10001st prime
#by Alexandre Pinto

import math

def findPrimes(n):

	list=(n+2)*[True]

	for i in range(2,int(math.sqrt(n))+1):
		if list[i]==True:
			for j in range(i**2,n+1,i):
				list[j]=False

	index=0
	for i in range(2,len(list)-1):
		if list[i]==True:
			index+=1
			print "%d: %d" %(index,i)
		if(index==10001):
			break
		



if __name__ == '__main__':
	findPrimes(1000000)

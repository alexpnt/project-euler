#http://projecteuler.net/problem=41
#Pandigital prime
#by Alexandre Pinto

import math,itertools,operator

def findBiggestPan():
	biggest=1
	
	pandigitalN=[[1,2,3,4],[1,2,3,4,5,6,7]]			#5,6,8 and 9 numbers cannot be done (always dividable by 3)
	
	for i in xrange(0,2):										#try all permutations
		numList=list(itertools.permutations(pandigitalN[i]))
		numList=sorted(numList,key=operator.itemgetter(0,1,2,3))	#sort permutations
		for j in xrange(len(numList)-1,0,-1):
			num = int(''.join(map(str,numList[j])))
			if(isPrime(num)==True and num>biggest):	#if we find a new solution, there is no need to keep searching since it will always be a lower value
				biggest=num
				break				
	return biggest

def isPrime(n):							#check whether a number is prime or not
    for i in xrange(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

if __name__ == '__main__':

	print findBiggestPan()

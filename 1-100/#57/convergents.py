#http://projecteuler.net/problem=57
#Square root convergents
#by Alexandre Pinto

import math
def countFractions():
	counter=0

	num=1
	den=2
	for i in xrange(0,1000):
		res=result(num,den)
		if(nLength(res[0])>nLength(res[1])):
			counter+=1
		#print 'Iteration '+str(i)+': '+str(res[0])+'/'+str(res[1])+' = '+str(float(res[0])/res[1])
		next=nextInnerTerm(num,den)
		num=next[0]
		den=next[1]

	return counter

def nextInnerTerm(num,den):
	innerTerm=[den,2*den+num]
	return innerTerm
	
def result(num,den):
	innerTerm=nextInnerTerm(num,den)
	return [innerTerm[0]+innerTerm[1],innerTerm[1]]

#returns the length of a given number
def nLength(n):
	return int(math.floor(math.log(n,10))+1)

if __name__=='__main__':
	print countFractions()

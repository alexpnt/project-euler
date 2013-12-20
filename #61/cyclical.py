#http://projecteuler.net/problem=61
#Cyclical figurate numbers
#by Alexandre Pinto

import math,itertools

def findSum():

	f=[lambda n: (n*(n+1))/2,lambda n: n**2,lambda n: (3*n**2-n)/2,lambda n: 2*n**2-n,lambda n: (5*n**2-3*n)/2 ,lambda n: 3*n**2-2*n]
	start=[45,32,26,23,21,19]
	figures=[]
	for i in xrange(0,6):
		figures+=[genFigurateNumbers(start[i],f[i])]	

	perm=list(itertools.permutations([1,2,3,4,5]))	#generate permutations
	for a in figures[0]:
		for order in perm:
			if search(figures,0,order,a,a,a,2)==True:
				return

#Perform a Backtracking Search
def search(figures,i,order,before,first,s,depth):

	if(depth==6):
		for b in figures[order[i]]:
			if before%100==b/100 and first/100==b%100:
				s+=b
				print "The sum of the only ordered set of six cyclic 4-digit is: ",s
				return True
		return False
	else:	
		for b in figures[order[i]]:
			if before%100==b/100:
				if search(figures,i+1,order,b,first,s+b,depth+1)==True:
					return True
		return False

#generate figurate numbers according to the given formula and starting on the given start number
def genFigurateNumbers(start,formula):

	figurate=[]
	n=start
	l=4
	while(l==4):
		figurate+=[formula(n)]
		l=nLength(figurate[-1])
		n+=1

	return figurate[:-1]


#returns the length of a given number
def nLength(n):
	return int(math.floor(math.log(n,10))+1)


if __name__ == "__main__":
	findSum()
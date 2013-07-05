#http://projecteuler.net/problem=39
#Integer right triangles
#by Alexandre Pinto

import math
def maximizeNSol():

	N=1000
	squares=[i*i for i in xrange(1,N+1)]
	roots=[x for x in xrange(1,2*N+1)]
	dic={}
	for x in xrange (1,N):							#generate pythagorean triples
		for y in xrange (x+1,N):
			z=roots[int(math.sqrt(squares[x-1]+squares[y-1]))-1]
			if z**2 == x**2 + y**2 and z<N:
				p=x+y+z
				if(p<=1000):
					if p in dic:
						dic[p]+=1 					#update previous entry
					else:
						dic[p]=1 					#add new entry
	bestP=0
	bestK=0
	for key in dic.keys():							#find the biggest perimeter
		if(dic[key]>bestP):
			bestK=key
			bestP=dic[key] 
	return bestK
if __name__ == '__main__':

	print maximizeNSol()

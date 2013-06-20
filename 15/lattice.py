#http://projecteuler.net/problem=15
#Lattice paths
#by Alexandre Pinto

from math import factorial as fact

def lattice(a,b):

	comb=fact(a+b)/(fact(a)*fact(b))	#Lattice Path
	return comb

if __name__ == '__main__':
	print lattice(20,20)	

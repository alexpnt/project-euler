#http://projecteuler.net/problem=58
#Spiral primes
#by Alexandre Pinto

import math,random

def spiral():
	ratio=1.0

	side=1
	countPrimes=1.0
	total=1.0
	while(ratio>0.1):
		side+=2
		oddSquare=side**2
		for i in xrange(0,4):
			n=oddSquare-i*(side-1)
			if n>3 and n%2!=0 and checkMillerRabin(n,10)==True:
				countPrimes+=1.0

		total+=4	
		ratio=countPrimes/total
		# print 'primes= '+str(countPrimes)+', total= '+str(total)+', ratio= '+str(ratio)+', side= '+str(side)
	return side

#Miller-Rabin primality test
def checkMillerRabin(n,k):
	if n==2: return True
	if n==1 or n%2==0: return False

	#find s and d, with d odd
	s=0
	d=n-1
	while(d%2==0):
		d/=2
		s+=1
	assert (2**s*d==n-1)

	#witness loop
	composite=1
	for i in xrange(k):
		a=random.randint(2,n-1)
		x=modular_pow(a,d,n)
		if x==1 or x==n-1: continue
		for j in xrange(s-1):
			composite=1
			x=modular_pow(x,2,n)
			if x==1: return False #is composite
			if x==n-1: 
				composite=0
				break
		if composite==1:
			return False		#is composite
	return True					#is probably prime

#perform a Modular exponentiation
def modular_pow(base, exponent, modulus):
    result=1
    while exponent>0:
        if exponent%2==1:
           result=(result * base)%modulus
        exponent=exponent>>1
        base=(base * base)%modulus
    return result

if __name__ == "__main__":
	print spiral()

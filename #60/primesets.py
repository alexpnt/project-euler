#http://projecteuler.net/problem=60
#Prime pair sets
#by Alexandre Pinto

import math,random

def lowestSum(upperbound):
		
		primes=findPrimes(upperbound)
		combs=[]
		precision=10
		for i in xrange(len(primes)):
			combs+=[[0]*len(primes)]


		#build a boolean matrix that indicates about possible concatenations
		print 'building boolean matrix ...'
		for p1 in xrange(len(primes)):
			for p2 in xrange(p1+1,len(primes)):
				if checkMillerRabin(int(str(primes[p1])+str(primes[p2])),precision)==True and checkMillerRabin(int(str(primes[p2])+str(primes[p1])),precision)==True:
					combs[p1][p2]=1
					combs[p2][p1]=1

		print 'searching ...'
		s=30000	#upperbound
		for p1 in xrange(len(primes)):
			for p2 in xrange(p1+1,len(primes)):
				if primes[p1]+primes[p2]<s and combs[p2][p1]==1:
					for p3 in xrange(p2+1,len(primes)):
						if primes[p1]+primes[p2]+primes[p3]<s and combs[p3][p1]==1 and combs[p3][p2]==1:
							for p4 in xrange(p3+1,len(primes)):
								if primes[p1]+primes[p2]+primes[p3]+primes[p4]<s and combs[p4][p1]==1 and combs[p4][p2]==1 and combs[p4][p3]==1:
									for p5 in xrange(p4+1,len(primes)):
										temp=primes[p1]+primes[p2]+primes[p3]+primes[p4]+primes[p5]
										if temp<s and combs[p5][p1]==1 and combs[p5][p2]==1 and combs[p5][p3]==1 and combs[p5][p4]==1:
											s=temp
											print 'primes: '+str(primes[p1])+', '+str(primes[p2])+', '+str(primes[p3])+', '+str(primes[p4])+', '+str(primes[p5])
											print 'sum: '+str(s)
											return

def findPrimes(n):				#generate a list of primes, using the sieve of eratosthenes

	primes=(n+2)*[True]

	for i in xrange(2,int(math.sqrt(n))+1):
		if primes[i]==True:
			for j in xrange(i**2,n+1,i):
				primes[j]=False

	primes=[i for i in xrange(2,len(primes)-1) if primes[i]==True]
	return primes


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
	lowestSum(10000)
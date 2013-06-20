#http://projecteuler.net/problem=3
#Largest prime factor
#by Alexandre Pinto

def calcMaxPrime(n):
	prime=2
	i=0
	q=n
	while(q!=1):
		if q%prime==0:
			q/=prime
		else:
			prime=calcNextPrime(prime+1)
		
	print "The max prime factor is",prime

def calcNextPrime(p):

	count=0

	while isPrime(p)==0:
		p+=1

	return p


def isPrime(n):

	count=0

	for i in range(1,n+1):
		if n%i==0:
			count+=1

	if count==2:
		return 1
	else:
	 	return 0

if __name__ == '__main__':

	calcMaxPrime(input())

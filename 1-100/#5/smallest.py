#http://projecteuler.net/problem=5
#Smallest multiple
#by Alexandre Pinto

def smallestEvenlyDivisible():

	n=20
	while(not isEvenly(n,20)):
		n+=20
		print n
	return n

def isEvenly(n,k):

	counter=0

	for i in range(1,k+1):
		if(n%i==0):
			counter+=1

	return counter==k

if __name__ == '__main__':

	print smallestEvenlyDivisible()

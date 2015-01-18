#http://projecteuler.net/problem=34
#Digit factorials
#by Alexandre Pinto

def findSum(upperbound):
	sum=0

	for i in xrange(3,upperbound):
		if(isCurious(i)==1):
			sum+=i
	return sum

def isCurious(n):
	facts=[1,1,2,6,24,120,720,5040,40320,362880]
	sum=0
	expected=n
	
	while(n!=0):
		sum+=facts[n%10]
		n/=10

	if(sum==expected):return 1
	return 0

if __name__ == '__main__':
	print findSum(41000)

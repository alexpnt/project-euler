#http://projecteuler.net/problem=30
#Digit fifth powers
#by Alexandre Pinto

def findSum(upperbound):
	
	sum=0
	for i in xrange(2,upperbound):
		if(isDigitPower(i)==1):
			sum+=i
	return sum

def isDigitPower(n):
	
	while (n > 0) {
    	int d = number % 10;
        number /= 10;

	original=n
	sum=0
	for d in str(n):
		sum+=int(d)**5;
	if(sum==n):
		return 1
	return 0


if __name__ == '__main__':
	print findSum(354294) 			#upper bound = 6*9^5

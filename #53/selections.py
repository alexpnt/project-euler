#http://projecteuler.net/problem=53
#Combinatoric selections
#by Alexandre Pinto

def findHowMany():
	
	pascal=triPascal(100)
	counter=0
	for row in pascal:
		for p in row:
			if(p>1000000):
				counter+=1 		#count how many numbers are greater than 1 000 000
	print counter

def triPascal(n):		#build a pascal triangle

	pascal=[[1],[1,1]]

	length=2
	for i in xrange(2,n+1):
		newRow=[1]
		for j in xrange(1,length):
			newRow+=[pascal[i-1][j-1]+pascal[i-1][j]]
		newRow+=[1]
		pascal+=[newRow]
		length+=1
	return pascal

if __name__ == '__main__':
	print findHowMany()
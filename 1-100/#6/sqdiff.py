#http://projecteuler.net/problem=6
#Sum square difference
#by Alexandre Pinto

def findDiff(n):

	squareSum=0
	sumSquares=0

	for i in range(1,n+1):
		sumSquares+=i**2

	for i in range(1,n+1):
		squareSum+=i
	squareSum=squareSum**2

	return squareSum-sumSquares

if __name__ == '__main__':
	print findDiff(100)

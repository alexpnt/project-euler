#http://projecteuler.net/problem=55
#Lychrel numbers
#by Alexandre Pinto

def countLychrels():

	count=0
	cache=[]
	for i in xrange(10,10000):
		if isLychrel(i):
			count+=1
			# print i
	return count

def isLychrel(n):

	iterations=0
	while(iterations<50):
		n+=int(str(n)[::-1])
		if(str(n)==str(n)[::-1]):
			return False
		iterations+=1
	return True
	
if __name__ == '__main__':
	print countLychrels()

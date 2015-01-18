#http://projecteuler.net/problem=52
#Permuted multiples
#by Alexandre Pinto

def findSmallest():

	start=10
	end=16			#we only need to check 10-16/ 100-160 / 1000-1600 / ... Beyond this we only get more digits
	while(True):
		start*=10
		end*=10
		for i in xrange(start,end):
			# print i
			if(check(i)):
				return i

def check(n):			#check the existence of permuted multiples

	if(set(str(n))==set(str(n*2))==set(str(n*3))==set(str(n*4))==set(str(n*5))==set(str(n*6))):
		return True
	else:
		return False

if __name__ == '__main__':
	print findSmallest()
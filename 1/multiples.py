#http://projecteuler.net/problem=1
#Multiples of 3 and 5 
#by Alexandre Pinto

def findmultiples():

	sum=0
	for i in range(1,1000):
		if i%3==0 or i%5==0:
			sum+=i
	print sum


if __name__ == '__main__':
	findmultiples()

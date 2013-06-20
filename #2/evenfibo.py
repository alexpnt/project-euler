#http://projecteuler.net/problem=2
#Even Fibonacci numbers 
#by Alexandre Pinto

def evenfib():

	prev = 0
	actual = 1
	sum=0
	
	while(actual<4000000):
		next = prev + actual
		prev = actual
		actual = next
		if actual%2==0:
			sum+=actual

	print sum
if __name__ == '__main__':
	evenfib();

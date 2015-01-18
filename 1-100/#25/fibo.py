#http://projecteuler.net/problem=25
#1000-digit Fibonacci number
#by Alexandre Pinto

def fibo():

	prev = 0
	actual = 1
	i=1
	while(len(str(actual))<1000):
		next = prev + actual
		prev = actual
		actual = next
		i+=1
	return i
if __name__ == '__main__':
	print fibo();

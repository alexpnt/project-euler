#http://projecteuler.net/problem=16
#Power digit sum
#by Alexandre Pinto

def powersum(n):

	sum=0
	power=str(2**n)
	for i in power:
		sum+=int(i)
	return sum

if __name__ == '__main__':
	print powersum(1000)	

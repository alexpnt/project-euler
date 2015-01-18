#http://projecteuler.net/problem=13
#Large sum
#by Alexandre Pinto

def firsten():

	sum=0
	for i in range(0,100):
		string=raw_input()
		sum+=int(string)

	return sum

if __name__ == '__main__':
	print firsten()

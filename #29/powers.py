#http://projecteuler.net/problem=29
#Distinct powers
#by Alexandre Pinto

def powers():
	
	distinct=set()
	for i in range(2,101):
		for j in range(2,101):
			distinct.add(j**i)
	
	return len(distinct)
	
if __name__ == "__main__":
	print powers()

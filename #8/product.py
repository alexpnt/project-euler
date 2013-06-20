#http://projecteuler.net/problem=8
#Largest product in a series
#by Alexandre Pinto

def findGreatestProd(n):
	
	best=0
	string=raw_input()

	for i in range(0,len(string)-n+1):
		candidate=prod(i,i+n,string)
		#	print "--"
		if candidate>best:
			best=candidate

	return best
def prod(begin,end,string):

	prod=1
	for i in range(begin,end):
		prod=prod*int(string[i])
		#print string[i]
	#print prod
	return prod

if __name__ == '__main__':
	print findGreatestProd(5)

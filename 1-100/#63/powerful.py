#http://projecteuler.net/problem=63
#Powerful digit counts
#by Alexandre Pinto

def findHowmany():

	counter=0
	ndigits=1
	lowerbound=0
	upperbound=9
	while lowerbound<upperbound:
		lowerbound=int(10**((ndigits-1)/float(ndigits)))
		for i in xrange(lowerbound,upperbound+1):
			if len(str(i**ndigits))==ndigits:
				print i,"^",ndigits,"=",i**ndigits
				counter+=1
		ndigits+=1

	print "\nThere are",counter,"n-digit positive integers which are also an nth power"

if __name__ == "__main__":
	findHowmany()
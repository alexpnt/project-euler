#http://projecteuler.net/problem=31
#Coin sums
#by Alexandre Pinto

def countTwo():

	coins=[1,2,5,10,20,50,100,200]

	comb=[0]*201
	comb[0]=1

	for i in xrange(0,8):
		for j in xrange(coins[i],201):
			comb[j]+=comb[j-coins[i]]		#dynamic programming
 	
 	print comb
		
if __name__ == '__main__':
	print countTwo()

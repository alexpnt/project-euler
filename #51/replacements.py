#http://projecteuler.net/problem=51
#Prime digit replacements
#by Alexandre Pinto

import itertools,math

def findBestRep():

	primes=findPrimes(1000000)
	#perm4=["".join(seq) for seq in itertools.product("01", repeat=4) if(seq.count('1')==3)]	#generate all possible masks for 5 digits
	perm5=["".join(seq) for seq in itertools.product("01", repeat=5) if(seq.count('1')==3)]	#generate all possible masks for 6 digits

	for p in primes:
	 	# if(len(str(p))==5):
	 	# 	perms=perm4
	 	# else:
	 	# 	perms=perm5

 		for perm in perm5:	#consider only 6 digits
 			counter=0
 			best=1000000
 			# print '---'
 			for i in xrange(0,10):							#test replacements
 				candidate=replace(p,perm,i)
 				if(binary_search(primes,candidate)!=-1):	#chek if its a prime number 
 					if(candidate<best):best=candidate		#save the first one(the smallest)
 					# print candidate
					counter+=1
					if(counter==8):
						return best

def replace(prime,permutation,substitute):		#apply the mask

	replaced=list(str(prime))
	for i in xrange(0,len(replaced)-1):
		if permutation[i]=='1':
			replaced[i]=str(substitute)
	return int(''.join(map(str,replaced)))

def findPrimes(n):				#generate a list of primes, using the sieve of eratosthenes

	primes=(n+2)*[True]

	for i in xrange(2,int(math.sqrt(n))+1):
		if primes[i]==True:
			for j in xrange(i**2,n+1,i):
				primes[j]=False

	primes=[i for i in xrange(2,len(primes)-1) if primes[i]==True and len(str(i))>=6] 	#consider only 6 digits
	return primes

#perform a binary search
def binary_search(l, target):
    low=0
    high = len(l)
    while low < high:
        mid = (low+high)//2
        midval = l[mid]
        if midval < target:
            low = mid+1
        elif midval > target: 
            high = mid
        else:
            return mid
    return -1

if __name__ == '__main__':
	print findBestRep()
	


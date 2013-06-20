#http://projecteuler.net/problem=14
#Longest Collatz sequence
#by Alexandre Pinto

def findLongestSeq(n):
	dic={}
	longest=0
	index=0

	i=1
	while(i<n):
		candidate=collatz(i,dic)
		dic[i]=candidate			#memoization technique for intermediate values
		if(candidate>longest):
			longest=candidate
			index=i
		i+=1
	return index

def collatz(n,dic):	#returns the lenght of a collatz sequence

	counter=1

	while(n!=1):
		if n in dic:			
			counter+=dic[n]
			break
		if n%2==0:
			n/=2
		else:
			n=3*n+1
		counter+=1
	
	return counter


if __name__ == '__main__':
	print findLongestSeq(1000000)	

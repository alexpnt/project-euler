#http://projecteuler.net/problem=26
#Reciprocal cycles
#by Alexandre Pinto

def findLongestCycle():

	best=0
	index=0

	for i in range(1000,0,-1):
		candidate=countCycleLen(1,i)
		if(candidate>best):				#update best
			best=candidate
			index=i
		if(best>i):						#for a given value i, the max possible length is i-1, so we can guarantee that there isnt any better
			break

	return index

def countCycleLen(d,D):					#returns the length of the recurring cycle, for a given dividend and divisor
	remainders=[]
	r=q=1
	while r!=0 and r not in remainders:	#when we find a repeated remainder, we have a cycle (or not)
		q=d/D
		r=d%D
		remainders+=[r]					#save the remainders
		d=r*10
		r=d%D
	return len(remainders)

if __name__ == '__main__':
	print findLongestCycle()

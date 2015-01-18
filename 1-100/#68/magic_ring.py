# http://projecteuler.net/problem=68
# Magic 5-gon ring
# by Alexandre Pinto

import math
import itertools
from collections import deque

#returns the length of a given number
def nLength(n):
	return int(math.floor(math.log(n,10))+1)

#check of this candidate solution fits the description of a magic 5-gon ring
#[ abc dce feg hgi jib ] becomes [ abcdefghij]  (deleting duplicates)
def is_magic_ring(candidate):

	expected_sum=candidate[0]+candidate[1]+candidate[2]	#sum of the first side
	sides=[(3,2,4),(5,4,6),(7,6,8),(9,8,1)]				#representation of other sides

	for s in sides:
		if (candidate[s[0]]+candidate[s[1]]+candidate[s[2]])!=expected_sum:	#property of a magic ring
			return False
	return True

#transform into a complete solution, instead of a compressed representation
def decode_candidate(candidate):
	sides=[(0,1,2),(3,2,4),(5,4,6),(7,6,8),(9,8,1)]
	solution=[]
	for s in sides:
		solution+=[(candidate[s[0]],candidate[s[1]],candidate[s[2]])]
	return solution

def convert_to_number(solution):
	s=''
	for t in solution:
		s+=''.join(map(str,t))
	return int(s)

if __name__ == "__main__":
	candidates=list(itertools.permutations(range(1,11),10))		#generate solutions

	best=0
	for c in candidates:				#brute force search, still fast (representation helps)
		if is_magic_ring(c)==True:
			solution=decode_candidate(c)
			if solution[0][0]<solution[1][0] and solution[0][0]<solution[2][0] and solution[0][0]<solution[3][0] and solution[0][0]<solution[4][0]: #respect order
				n=convert_to_number(solution)
				if(nLength(n)==16 and n>best):
					best=n

	print "The maximum 16-digit string for a magic 5-gon ring is ",best
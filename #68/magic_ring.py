# http://projecteuler.net/problem=68
# Magic 5-gon ring
# by Alexandre Pinto

import itertools
from collections import deque
	
def is_magic_ring(candidate):

	expected_sum=candidate[0]+candidate[1]+candidate[2]
	sides=[(3,2,4),(5,4,6),(7,6,8),(9,8,1)]

	for s in sides:
		if (candidate[s[0]]+candidate[s[1]]+candidate[s[2]])!=expected_sum:
			return False
	return True

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
	candidates=list(itertools.permutations(range(1,11),10))

	best=0
	for c in candidates:
		if is_magic_ring(c)==True:
			solution=decode_candidate(c)
			if solution[0][0]<solution[1][0] and solution[0][0]<solution[2][0] and solution[0][0]<solution[3][0] and solution[0][0]<solution[4][0]: 
				print "yes: ",convert_to_number(solution)
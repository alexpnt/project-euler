#http://projecteuler.net/problem=62
#Cubic permutations
#by Alexandre Pinto

def findSmallest():
	uppper=10000
	cubes=genSortedCubes(uppper)

	l=len(cubes)
	counter=[]
	sortedCubes=[]
	for i in xrange(l):
		for j in xrange(len(sortedCubes)):
			if cubes[i]==sortedCubes[j]:		#possible permutation
				counter[j][1]+=1
				if(counter[j][1]==5):			#this cube reached five permutations
					print "The smallest cube for which exactly five permutations of its digits are cube is:",counter[j][0]
					return
				break
		else:
			counter+=[[(i+1)**3,1]]				#create new entry
			sortedCubes+=[cubes[i]]

def genSortedCubes(upperbound):

	cubes=[]
	for i in xrange(1,upperbound):
		srted=list(str(i**3))
		srted.sort()
		cubes+=[srted]
	return cubes
if __name__ == "__main__":
	findSmallest()
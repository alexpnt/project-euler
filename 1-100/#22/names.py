#http://projecteuler.net/problem=22
#Names scores
#by Alexandre Pinto

def score():

	sum=0
	names=raw_input()
	names=names.translate(None,'"').split(",")
	names.sort()

	index=0
	for word in names:
		sumL=0
		index+=1
		for l in word:
			sumL+=ord(l)-64
		sum+=sumL*index

	return sum
if __name__ == '__main__':
	print score()
	


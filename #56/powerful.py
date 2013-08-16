#http://projecteuler.net/problem=56
#Powerful digit sum
#by Alexandre Pinto

def maxSum():

	m=0
	for a in xrange(1,100):
		for b in xrange(1,100):
			candidate=digitSum(a**b)
			if candidate>m:
				m=candidate
	return m

def digitSum(n):
	s=0
	for d in list(str(n)):
		s+=int(d)
	return s
if __name__ == '__main__':
	print maxSum()

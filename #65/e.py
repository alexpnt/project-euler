#http://projecteuler.net/problem=65
#Convergents of e
#by Alexandre Pinto


def findSum():

	#generate values of a (a0,a1,a2,....)
	quotients=[2]
	for k in xrange(1,35):
		quotients+=[1,2*k,1]

	#apply recursive relation
	hn=[0,1]
	kn=[1,0]
	for i in xrange(2,102):
		hn+=[quotients[i-2]*hn[i-1]+hn[i-2]]
		kn+=[quotients[i-2]*kn[i-1]+kn[i-2]]

		#print 'iteration',str(i-2)+':',hn[i],'/',kn[i]
	print sum_digits(hn[i])

def sum_digits(n):
    s=0
    while n:
        s+=n%10
        n/=10
    return s
if __name__ == "__main__":
	findSum()
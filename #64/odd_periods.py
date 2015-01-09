#http://projecteuler.net/problem=64
#Odd period square roots
#by Alexandre Pinto

from math import sqrt,floor

#n + floor(1/2 + sqrt(n))
def non_square_root(n):
	return n + int(floor(0.5+sqrt(n)))

def generate_non_square_roots(N):
	return [non_square_root(i) for i in xrange(1,N+1) if non_square_root(i)<=N]


#http://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Continued_fraction_expansion
#obtain a list of triplets (mn, dn, an). The sequence [a0; a1, a2, a3,...] is the continued fraction expansion
def continued_fraction_expansion(n):
	m_before=0
	d_before=1
	a0=a_before=int(floor(sqrt(n)))

	mda_triplets=[]
	period_lenght=0

	while True:

		m_next=d_before*a_before-m_before
		d_next=int((n-m_next**2)/d_before)
		a_next=int(floor((a0+m_next)/d_next))

		if( ((m_next,d_next,a_next) in mda_triplets) or a_before==2*a0):
			break
		else:
			mda_triplets+=[(m_next,d_next,a_next)]
			m_before=m_next
			d_before=d_next
			a_before=a_next
			period_lenght+=1

	return mda_triplets,period_lenght

if __name__ == "__main__":
	count=0
	nsr=generate_non_square_roots(10000)
	for n in nsr:
		cfe,l=continued_fraction_expansion(n)
		if l%2!=0:
			count+=1

	print "There are "+str(count)+" continued fractions with an odd period, for N<=1000"
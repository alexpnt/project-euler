# http://projecteuler.net/problem=66
# Diophantine equation
# by Alexandre Pinto

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

		if(a_before==2*a0 or ((m_next,d_next,a_next) in mda_triplets)):
			break
		else:
			mda_triplets+=[(m_next,d_next,a_next)]
			m_before=m_next
			d_before=d_next
			a_before=a_next
			period_lenght+=1

	return mda_triplets,period_lenght

# compute the continued fraction convergents to sqrt(D) (potential solutions for the Pell Equation)
# compute the convergents using the recurrent relations presented in http://mathworld.wolfram.com/PellEquation.html
def continued_fraction_covergents(D,n_periods):

	expansion,l=continued_fraction_expansion(D)

	for p in xrange(n_periods):			#add periods of triplets (m,d,a)
		expansion+=expansion[0:l]

	a0=int(floor(sqrt(D)))

	#initialize
	pn_2=1
	pn_1=a0

	qn_2=0
	qn_1=1

	convergents=[]
	for i in xrange(0,l*(n_periods+1)):			#recursive relations to find convergents	
		pn=expansion[i][2]*pn_1+pn_2
		pn_2=pn_1
		pn_1=pn

		qn=expansion[i][2]*qn_1+qn_2
		qn_2=qn_1
		qn_1=qn

		convergents+=[(pn,qn)]
	return convergents

#find the minimal solution in x , for the Pell Equation
def find_minimal_solution(convergents,D):
	found=False
	max_x=2**128
	y=0
	for c in convergents:
		if c[0]**2-D*c[1]**2==1 and c[0]<max_x:		#check if convergent is solution of the Pell Equation
			max_x=c[0]
			y=c[1]
			found=True

	return [found,max_x,y]

if __name__ == "__main__":
	max_x=0
	nsr=generate_non_square_roots(1000)
	for d in nsr:
		n_periods=0
		while True:
			conv=continued_fraction_covergents(d,n_periods)
			solution=find_minimal_solution(conv,d)

			if solution[0]==False:		#did not find a solution, increase period of the fraction expansion and try again
				n_periods+=1
			else:
				break
		if solution[1]>max_x:			#save best D value
			max_x=solution[1]
			D=d
	print "The largest value of x is obtained for D = "+str(D)

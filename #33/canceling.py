#http://projecteuler.net/problem=33
#Digit canceling fractions
#by Alexandre Pinto

def findDen():

	nums=[]
	dens=[]

	for i in xrange(11,100):
		for j in xrange(11,100):
			if((i%10)!=0 and (j%10)!=0 and i!=j and isCurious(i,j)==1):
				nums+=[i]
				dens+=[j]
				print i,"/",j 	#curious fractions

	return reduce(lambda x,y:float(x*y),nums)/reduce(lambda x,y:x*y,dens)


def isCurious(num,den):

	expected=num/float(den)
	n=list(str(num))
	d=list(str(den))

	potential=False
	for i in xrange(0,2):
		for j in xrange(0,2):
			if(n[i]==d[j]):
				n.pop(i)
				d.pop(j)
				if((float(int(n[0]))/int(d[0]))==expected and expected<1.0):
					return 1
				else:
					return 0
	return 0

if __name__ == '__main__':
	print findDen()

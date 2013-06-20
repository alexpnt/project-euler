#http://projecteuler.net/problem=9
#Special Pythagorean triplet
#by Alexandre Pinto

def findTriplet():

	for i in range(1,1000):				#brute force, ...
		for j in range(i+1,1000):
			for z in range(j+1,1000):
				if(i**2+j**2==z**2):
					print i,j,z
					if(i+j+z==1000):
						print i*j*z
						return

if __name__ == '__main__':
	print findTriplet()

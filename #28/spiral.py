#http://projecteuler.net/problem=28
#Number spiral diagonals
#by Alexandre Pinto

def spiral():
	sum=1
	
	for i in range(3,1002,2):
		sum+=4*i**2-6*i+6		#optimized version
		# sum+=i**2
		# sum+=i**2-(i*3-3)
		# sum+=i**2-(i*2-2)
		# sum+=i**2-(i-1)
	return sum


if __name__ == "__main__":
	print spiral()

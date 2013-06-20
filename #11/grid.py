#http://projecteuler.net/problem=11
#Largest product in a grid
#by Alexandre Pinto

def maxprod(n):

	maxprod=-1
	grid=[]

	#input
	for i in range(0,n):
		line=raw_input().split()
		grid+=[line]
	
	#convert input to ints	
	for i in range(0,n):
		for j in range(0,n):
			grid[i][j]=int(grid[i][j])

	#search horizontally
	for i in range(0,n):
		for j in range(0,n-3):
			prod=1
			for z in range(0,4):	
				prod*=grid[i][j+z]
			if(prod>maxprod):
				maxprod=prod

	#search vertically
	for i in range(0,n-3):
		for j in range(0,n):
			prod=1
			for z in range(0,4):	
				prod*=grid[i+z][j]
			if(prod>maxprod):
				maxprod=prod
	#search diagonally left-right
	for i in range(0,n-3):
		for j in range(0,n-3):
			prod=1
			for z in range(0,4):	
				prod*=grid[i+z][j+z]
			if(prod>maxprod):
				maxprod=prod

	#search diagonally right-left
	for i in range(0,n-3):
		for j in range(3,n):
			prod=1
			for z in range(0,4):	
				prod*=grid[i+z][j-z]
			if(prod>maxprod):
				maxprod=prod

	return maxprod

if __name__ == '__main__':
	print maxprod(20)


#http://projecteuler.net/problem=4
#Largest palindrome product
#by Alexandre Pinto

def calmaxpalin():

	max=0
	for i in range(100,1000):			#brute force
		for j in range(100,1000):
			prod=i*j
			if(isPalindrome(prod)==1):
				if(prod>max):
					max=prod
	print max

def isPalindrome(prod): #check if a number is a palindrome

	prod=str(prod)
	if(prod[len(prod):-(len(prod)+1):-1]==prod):
		return 1

if __name__ == '__main__':

	calmaxpalin()

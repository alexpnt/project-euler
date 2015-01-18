#http://projecteuler.net/problem=36
#Double-base palindromes
#by Alexandre Pinto

def findSum():
	sum=0

	for i in xrange(0,1000000):
		if isPalindrome(i) and isPalindrome(bin(i)[2:]):
			print i
			sum+=i
	return sum

def isPalindrome(n): #check if a number is a palindrome

	n=str(n)
	if(n[len(n):-(len(n)+1):-1]==n):
		return 1

if __name__ == '__main__':
	print findSum()

#http://projecteuler.net/problem=42
#Coded triangle numbers
#by Alexandre Pinto

import math
def countTriangleWords():
	counter=0

	words=raw_input()
	words=words.translate(None,'"').split(",")

	for word in words:
		if(isTriangle(getWordValue(word))):
			counter+=1 
	return counter

def getWordValue(word):
	dic={'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,
		'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
	value=0
	for l in word:
		value+=dic[l]
	return value

def isTriangle(x):					#check whether a number is a triangular number or not
	test=(math.sqrt(8*x+1)+1)
	return test==int(test)
def genTriangleNumbers(n):

	tri=[]
	for i in xrange(0,n+1):
		tri+=[int(0.5*i*(i+1))]
	return tri
if __name__ == '__main__':

	print countTriangleWords()

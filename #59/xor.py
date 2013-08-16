#http://projecteuler.net/problem=59
#XOR decryption
#by Alexandre Pinto

import io

def decrypt(key):
	f=open('cipher1.txt','r')
	encrypted=f.read().split(',')

	i=0
	s=0
	for l in xrange(len(encrypted)):										#decrypt the message with the given key
		encrypted[l]=chr(int(str(int(encrypted[l])^ord(key[i%3]))))
		i+=1
		s+=ord(encrypted[l])												#sum the ascii values

	analysis=freqAnalysis(encrypted)										#perform a frequency analysis

	f.close()
	return [analysis,sum(analysis.values()),encrypted,s]

def freqAnalysis(m):
	freq={}
	for l in m:
		if l in freq.keys():
			freq[l]+=1
		else:
			freq[l]=1
	return freq

if __name__ == "__main__":

	key=['','','']
	for i in xrange(97,123):				#brute force attack plus frequency analysis
		for j in xrange(97,123):
			for z in xrange(97,123):		
				key[0]=chr(i)
				key[1]=chr(j)
				key[2]=chr(z)
				result=decrypt(key)
				if ' ' in result[0].keys() and 'e' in result[0].keys():			#the most common letter in english alphabet is 'e'
					if float(result[0]['e'])/(result[1]-result[0][' '])>=0.12:	#http://en.wikipedia.org/wiki/Letter_frequencies
						print 'key: '+''.join(key)
						print 'message: '+''.join(result[2])
						print 'sum of the ASCII values: '+str(result[3])
						exit()
	

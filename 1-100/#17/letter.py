#http://projecteuler.net/problem=17
#Number letter counts
#by Alexandre Pinto

def count():

	sum=0
	
	#number of letters
	units={0:0,1:3,2:3,3:5,4:4,5:4,6:3,7:5,8:5,9:4}	#1,2,3,..
	tens={0:0,1:3,2:6,3:6,4:5,5:5,6:5,7:7,8:6,9:6}	#20,30,40,..
	hundreds={1:10,2:10,3:11,4:11,5:11,6:10,7:12,8:12,9:11} #100,200,300,..
	special={0:3,1:6,2:6,3:8,4:8,5:7,6:7,7:9,8:8,9:8} #11,12,..
	
	for i in range(0,10):
		sum+=units[i]						#1-9
		sum+=special[i]						#10-19
	
	#20-99
	for i in range(2,10):
		for j in range(0,10):
			sum+=tens[i]+units[j]
	cacheTens=sum
	
	for i in range(1,10):
		sum+=hundreds[i]					#100,200,300,..
		sum+=(hundreds[i]+3)*99+cacheTens	#i[1-99]
	sum+=111
	return sum

if __name__ == '__main__':
	print count()	

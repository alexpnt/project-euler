#http://projecteuler.net/problem=54
#Poker hands
#by Alexandre Pinto

import io
def countWins():

	player1=[]
	player2=[]
	count=0
	
	f=open("poker.txt",'r')
	for line in f:
		player1=line[0:14].split()
		player2=line[14:].split()

		if(checkHands(player1,player2)):
			count+=1

	return count

def checkHands(hand1,hand2):
	
	if(checkRoyal(hand1)):
		return True
	elif(checkRoyal(hand2)):
		return False
	else:
		score=straightFlush(hand1,hand2)
		if(score==1):
			return True
		elif(score==-1):
			return False
		else:
			score=fourOfaKind(hand1,hand2)
			if(score==1):
				return True
			elif(score==-1):
				return False
			else:
				score=fullHouse(hand1,hand2)
				if(score==1):
					return True
				elif(score==-1):
					return False
				else:
					score=flush(hand1,hand2)
					if(score==1):
						return True
					elif(score==-1):
						return False
					else:
						score=straight(hand1,hand2)
						if(score==1):
							return True
						elif(score==-1):
							return False
						else:
							score=trio(hand1,hand2)
							if(score==1):
								return True
							elif(score==-1):
								return False
							else:
								score=twoPairs(hand1,hand2)
								if(score==1):
									return True
								elif(score==-1):
									return False
								else:
									score=onePair(hand1,hand2)
									if(score==1):
										return True
									elif(score==-1):
										return False
									else:
										score=highestCard(hand1,hand2)
										if(score==1):
											return True
										elif(score==-1):
											return False

def translate(hand):
	seq={'T':'10','J':'11','Q':'12','K':'13','A':'14'}

	for c in xrange(0,5):
		if hand[c][:-1] in seq.keys():
			hand[c]=seq[hand[c][:-1]]+hand[c][-1]			#translate figures to numbers

	return hand
def genFreq(hand):
	hand=translate(hand)
	freq={}

	for c in xrange(0,5):									#frequencies
		if int(hand[c][:-1]) in freq.keys():
			freq[int(hand[c][:-1])]+=1
		else:
			freq[int(hand[c][:-1])]=1

	return freq

def checkRoyal(hand):
	suite=hand[0][-1]
	if(('T'+suite in hand) and ('J'+suite in hand) and ('Q'+suite in hand) and ('K'+suite in hand) and ('A'+suite in hand)):
		return True
	else:
		return False

def straightFlush(hand1,hand2):
	
	score1=checkStraightFlush(hand1)
	score2=checkStraightFlush(hand2)

	if score1>score2:
		return 1
	elif score1<score2:
		return -1
	else:
		return 0

def checkStraightFlush(hand):
	suite=hand[0][-1]
	score=0
	values=[]
	seq={'T':'10','J':'11','Q':'12','K':'13','A':'14'}

	hand=translate(hand)
	for c in xrange(0,5):
		if(hand[c][-1]!=suite):								
			return 0
		else:
			values+=[int(hand[c][:-1])]						

	values.sort()
	for c in xrange(1,5):
		if(values[c]!=values[c-1]+1):						
			return 0

	return sum(values)

def fourOfaKind(hand1,hand2):
	score1=checkFourOfaKind(hand1)
	score2=checkFourOfaKind(hand2)

	if score1[0]>score2[0]:
		return 1
	elif score1[0]<score2[0]:
		return -1
	elif score1[0]==0 and score2[0]==0:
		return 0
	else:
		del score1[1][score1[0]]
		del score2[1][score2[0]]

		if(score1[1].keys()[0]>score2[1].keys()[0]):
			return 1
		elif(score1[1].keys()[0]<score2[1].keys()[0]):
			return -1
		else:
			return 0

def checkFourOfaKind(hand):
	freq={}
	seq={'T':'10','J':'11','Q':'12','K':'13','A':'14'}

	hand=translate(hand)
	freq=genFreq(hand)

	if 4 in freq.values():
		if freq[int(hand[0][:-1])]==4: return [int(hand[0][:-1]),freq]
		else: return [int(hand[1][:-1]),freq]
	else:
		return [0,0]


def fullHouse(hand1,hand2):
	score1=checkFullHouse(hand1)
	score2=checkFullHouse(hand2)

	if score1=={} and score2!={}:
		return -1
	elif score2=={} and score1!={}:
		return 1
	elif score1=={} and score2=={}:
		return 0
	else:
		cards1=score1.items()
		cards1[0]=cards1[0][::-1]
		cards1[1]=cards1[1][::-1]
		cards1.sort()
		cards2=score2.items()
		cards2[0]=cards2[0][::-1]
		cards2[1]=cards2[1][::-1]
		cards2.sort()

		if cards1[0][1]>cards2[0][1]:
			return 1
		elif cards1[0][1]<cards2[0][1]:
			return -1
		else:
			if cards1[1][1]>cards2[1][1]:
				return 1
			elif cards1[1][1]<cards2[1][1]:
				return -1
			else:
				return 0
def checkFullHouse(hand):
	seq={'T':'10','J':'11','Q':'12','K':'13','A':'14'}
	freq={}
	
	hand=translate(hand)
	freq=genFreq(hand)

	if len(freq.keys())==2  and (2 in freq.values()) and (3 in freq.values()):
		return freq
	else:
		return {}

def flush(hand1,hand2):
	cards1=checkFlush(hand1)
	cards2=checkFlush(hand2)

	if cards1==[] and cards2!=[]:
		return -1
	elif cards2==[] and cards1!=[]:
		return 1
	elif cards1==[] and cards2==[]:
		return 0
	else:
		cards1.sort()
		cards1.reverse()

		cards2.sort()
		cards2.reverse()

		for i in xrange(0,5):
			if(cards1[i]>cards2[i]):
				return 1
			else:
				return -1
		return 0
def checkFlush(hand):
	suite=hand[0][-1]
	seq={'T':'10','J':'11','Q':'12','K':'13','A':'14'}
	cards=[]

	hand=translate(hand)
	for c in xrange(0,5):
		if hand[c][-1]==suite:
			cards+=[int(hand[c][:-1])]
		else:
			return []
	return cards
def straight(hand1,hand2):
	cards1=checkStraight(hand1)
	cards2=checkStraight(hand2)

	if cards1==[] and cards2!=[]:
		return -1
	elif cards2==[] and cards1!=[]:
		return 1
	elif cards1==[] and cards2==[]:
		return 0
	else:
		cards1.reverse()
		cards2.reverse()

		for i in xrange(0,5):
			if(cards1[i]>cards2[i]):
				return 1
			else:
				return -1
		return 0

def checkStraight(hand):
	seq={'T':'10','J':'11','Q':'12','K':'13','A':'14'}
	cards=[]

	hand=translate(hand)
	for c in xrange(0,5):
			cards+=[int(hand[c][:-1])]

	cards.sort()
	for c in xrange(1,5):
		if(cards[c]!=cards[c-1]+1):
			return []

	return cards

def trio(hand1,hand2):
	score1=checkTrio(hand1)
	score2=checkTrio(hand2)

	if score1==[] and score2!=[]:
		return -1
	elif score2==[] and score1!=[]:
		return 1
	elif score1==[] and score2==[]:
		return 0
	else:
		if score1[0]>score2[0]:
			return 1
		elif score1[0]<score2[0]:
			return -1
		else:
			score1[1].sort()
			score1[1].reverse()
			score2[1].sort()
			score2[1].reverse()

			for c in xrange(0,3):	
				if score1[1][c]>score2[1][c]:
					return 1
				elif score1[1][c]<score2[1][c]:
					return -1
			return 0

def checkTrio(hand):
	seq={'T':'10','J':'11','Q':'12','K':'13','A':'14'}
	freq={}
	
	hand=translate(hand)
	freq=genFreq(hand)

	cards=[0,[]]
	if 3 in freq.values():
		for key in freq:
			if freq[key]==3:
				cards[0]=key
			else:
				cards[1]+=[key]
		return cards
	else:
		return []

def twoPairs(hand1,hand2):
	score1=checkTwoPairs(hand1)
	score2=checkTwoPairs(hand2)

	if score1==[] and score2!=[]:
		return -1
	elif score2==[] and score1!=[]:
		return 1
	elif score1==[] and score2==[]:
		return 0
	else:
		score1[0].sort()
		score1[0].reverse()
		score2[0].sort()
		score2[0].reverse()

		for c in xrange(0,2):
			if score1[0][c]>score2[0][c]:
				return 1
			elif score1[0][c]<score2[0][c]:
				return -1
		if score1[1]>score2[1]:
			return 1
		elif score1[1]<score2[1]:
			return -1
		else:
			return 0
def checkTwoPairs(hand):
	seq={'T':'10','J':'11','Q':'12','K':'13','A':'14'}
	freq={}
	
	hand=translate(hand)
	freq=genFreq(hand)

	cards=[[],0]	
	cards[0]=[key for key in freq.keys() if freq[key]==2]
	if(len(cards[0])==2):
		for key in freq.keys():
			if freq[key]==1:
				cards[1]=key
		return cards
	else:
		return []
def onePair(hand1,hand2):
	score1=checkOnePair(hand1)
	score2=checkOnePair(hand2)

	if score1==[] and score2!=[]:
		return -1
	elif score2==[] and score1!=[]:
		return 1
	elif score1==[] and score2==[]:
		return 0
	else:
		if score1[0]>score2[0]:
			return 1
		elif score1[0]<score2[0]:
			return -1
		else:
			score1[1].sort()
			score1[1].reverse()
			score2[1].sort()
			score2[1].reverse()

			for c in xrange(0,3):	
				if score1[1][c]>score2[1][c]:
					return 1
				elif score1[1][c]<score2[1][c]:
					return -1
			return 0
def checkOnePair(hand):
	seq={'T':'10','J':'11','Q':'12','K':'13','A':'14'}
	freq={}
	
	hand=translate(hand)
	freq=genFreq(hand)

	cards=[0,[]]
	if 2 in freq.values():
		for key in freq:
			if freq[key]==2:
				cards[0]=key
			else:
				cards[1]+=[key]
		return cards
	else:
		return []

def highestCard(hand1,hand2):
	
	score1=checkHighestCard(hand1)
	score2=checkHighestCard(hand2)

	if score1>score2:
		return 1
	elif score1<score2:
		return -1
	else:
		return 0
def checkHighestCard(hand):
	highest=0
	seq={'T':'10','J':'11','Q':'12','K':'13','A':'14'}

	hand=translate(hand)

	for c in xrange(0,5):
		if int(hand[c][:-1])>highest:
			highest=int(hand[c][:-1])
	return highest

if __name__ == '__main__':
	print countWins()

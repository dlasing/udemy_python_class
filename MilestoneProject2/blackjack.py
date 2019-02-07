import random
from colorama import Fore
from colorama import Style


# Declare fixed variable
#suits = ('Hearts', 'Clubs', 'Diamonds', 'Spades')
suits = ('\u2665', '\u2663', '\u2666', '\u2660')
ranks = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10, 'A':11}
playing = True


def suit_color(suit):
			
	if suit == '\u2665' or suit == '\u2666':
		return Fore.RED
	else:
		return Fore.BLACK



def take_bet():
	
	while True:
		try:
			bet = int(input('Please make the bet.  '))
		except:
			print ('Ooops. money amount only!')
			continue
		else:
			print (f'Thanks! You bet ${bet}')
			break
			return bet
		

def hit(deck,hand):
	# function to hit 
	pop_card = deck.deal()
	hand.add_card(pop_card)
	


def hit_or_stand(deck,hand):
	global playing
	
	while True:
		try:
			hit_or_stand = input('Do you want to [h]it or [s]tand ?')
		except:
			print ('Enter [h]it or [s]tand')
			continue
		else:
			if hit_or_stand == 'h':
				playing = True
				hit(deck, hand)
				break
			
			if hit_or_stand == 's':
				playing = False
				print ('You stand')
				break
				
				
				
def show_some (player, dealer):
	
	
	print ('DEALER HAND')
	print ('===========')
		
	for item in range(0,len(dealer)):
		print (dealer[item])	
		
	
	print ('PLAYER HAND')
	print ('===========')

	for item in range(0,len(player)):
		print (dealer[item])				
	
	

class Deck():
# The Class for the while deck with method of shuffle and deal	
	def __init__(self):
		self.deck = []
		for suit in suits:
			for rank in ranks:
				self.deck.append([suit,rank])
				
		
	def __str__(self):
		print ('List of Deck')
		for x in range(0,52):	
			print (f'{suit_color(self.deck[x][0])}{self.deck[x][0]} {self.deck[x][1]} {Style.RESET_ALL}')
							
		return "DONE"


	def shuffle(self):
		random.shuffle(self.deck)
		print ('shuffled')
		for x in range(0,52):
			print (f'{suit_color(self.deck[x][0])}{self.deck[x][0]} {self.deck[x][1]} {Style.RESET_ALL}')



	def deal(self):
		single_card = self.deck.pop()	
		#print (f"single card is........{suit_color(single_card[0])}{single_card[0]}  {single_card[1]} {Style.RESET_ALL}")
		return single_card
		
		

class Card():
	
	def __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank
		
	def __str__(self):
		return f"the card @ Card() is.. {suit_color(self.suit)}{self.suit} {self.rank}{Style.RESET_ALL}"
			
	
	
	
class Hand():
			
	def __init__(self):
		self.card = []  # list to hold the cards on hand
		self.value = 0  # the value of all the cards
		self.aces = 0
		
	def add_card(self, cards):
		self.card.append(cards)
		print (f'This is the card list on Hand(): {self.card}')  # debug
		show_some(self.card, self.card)                          # debug for show_some()
		
		self.value += values[cards[1]]
		print (f'This is the value of card on Hand(): {self.value}')  #debug
		
		if cards[1] == 'A':
			self.aces += 1
		print (f'Number of Aces on Hand(): {self.aces}')   #debug
		
		return self.value
			
			
	def adjust_for_ace(self):
		self.value = self.value - 10
		print (f'This is the value of card on Hand(): {self.value}')  #debug
		
		return self.value
		


class Chips():
	
	def __init__(self):
		
		while True:
			try:
				self.total = int(input('How much money do you have?'))
				self.bet = 0
			except:
				print ('Come on!')
				continue
			else:
				print (f'You have ${self.total}')
				break
		
	def __str__(self):
		return f'You now have ${self.total}'
		
	def win_bet(self):
		self.total += self.bet
	
	def lose_bet(self):
		self.total += self.bet
		
		

while playing == True:

	suits_pick = suits[random.randrange(len(suits))]
	ranks_pick = ranks[random.randrange(len(ranks))]
	values_pick = values[ranks_pick]
	
	#print (f'suits: {suits_pick}')
	#print (f'ranks: {ranks_pick}')	
	#print (f'values: {values_pick}')
	
	
	# decale the Deck() and shuffle
	a = Deck()
	#print (a)	
	a.shuffle()
	
	#print (a)
	
	
	# deal the card. pop() from the shuffle list
	got_it = a.deal()
	#b = Card(got_it[0], got_it[1])	
	
	# The card at the Card()
	print (Card(got_it[0], got_it[1]))
	
	
	b = Hand()
	hand_value = b.add_card(got_it)
	print (f'The value on hand {hand_value}')

	got_it = a.deal()
	hand_value = b.add_card(got_it)
	print (f'The value on hand {hand_value}')
	
	got_it = a.deal()
	hand_value = b.add_card(got_it)
	print (f'The value on hand {hand_value}')

	hand_value = b.adjust_for_ace()
	print (f'The value on hand {hand_value}')

	
	c = Chips()
	print (c)
	
	take_bet()
	
		
	hit_or_stand(a,b)
	#hit(a,b)
	print (f'playing? {playing}')
	
	
	
	
	
	
	
	x = input ('Play again? Y/N  ')
	if x == "Y" or x == "y":
		playing = True
	else:
		playing = False
				
				
print ('Game Done')


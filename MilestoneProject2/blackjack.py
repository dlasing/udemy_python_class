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
			
	
		

while playing == True:

	suits_pick = suits[random.randrange(len(suits))]
	ranks_pick = ranks[random.randrange(len(ranks))]
	values_pick = values[ranks_pick]
	
	#print (f'suits: {suits_pick}')
	#print (f'ranks: {ranks_pick}')	
	#print (f'values: {values_pick}')
	
	
	a = Deck()
	#print (a)	
	a.shuffle()
	
	#print (a)
	
	got_it = a.deal()
	#b = Card(got_it[0], got_it[1])	
	print (Card(got_it[0], got_it[1]))

	
	#a.deal()
	
	#b = Card(suits_pick, ranks_pick)
	#print (b)

	#mycard = Card(Deck)
	#mycard.printcard()
	
	
	x = input ('Play again? Y/N  ')
	if x == "Y" or x == "y":
		playing = True
	else:
		playing = False
				
				
print ('Game Done')


import random
import time
from colorama import Fore
from colorama import Style


# Declare fixed variable
#suits = ('Hearts', 'Clubs', 'Diamonds', 'Spades')
suits = ('\u2665', '\u2663', '\u2666', '\u2660')
ranks = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10, 'A':11}
playing = True
play_again = True




	
	
def suit_color(suit):
			
	if suit == '\u2665' or suit == '\u2666':
		return Fore.RED
	else:
		return Fore.BLACK



def take_bet(chips):
	
	while True:
		try:
			bet = int(input('Please make the bet.  $'))
		except:
			print ('Ooops. money amount only!')
			continue
		else:
			if bet == 0:
				print (f'You need to put some money in...')
				continue
			if bet > chips:
				print (f'You only have ${chips}. Lower the bet')
				continue
			if bet <= chips:
				print (f'Go Ling, you bet ${bet}.  Good Luck')
				return bet
		

def hit(mydeck,hand):
	# function to hit 
	pop_card = mydeck.deal()
	hand.add_card(pop_card)
	


def hit_or_stand(mydeck, player_hand):
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
				hit(mydeck, player_hand)
				return False
				break
			
			if hit_or_stand == 's':
				playing = False
				print ('You stand')		
				return True	
				break
				
def another_round():
	
	while True:
		try:
			play_again = input ('Play again? [Y]es or [N]o? ')
		except:
			print ('Enter [Y] or [N]o')
			continue
		else:
			if play_again == "Y":
				return True
				break
			if play_again == "N":
				return False
				break
				
						
def show_some (player, dealer, player_chip, player_bet, player_hand_value):
	
	print ('\n'*40)
	print ('DEALER HAND')             
	print ('===========')     		                    
	for item in range(0,len(dealer)):
		
		if item == 0:
			print (f'{suit_color(dealer[item][0])}X X  {Style.RESET_ALL} ')	
		else:
			print (f'{suit_color(dealer[item][0])}{dealer[item][0]} {dealer[item][1]}  {Style.RESET_ALL} ')	
		#print (f'{suit_color(dealer[item][0])}{dealer[item][0]} {dealer[item][1]}  {Style.RESET_ALL} ')	
		#time.sleep(1)

			
			
	print ('\n'*3)	
	print ('GO LING HAND')             
	print ('============')             
	
	for item in range(0,len(player)):
		print (f'{suit_color(player[item][0])}{player[item][0]} {player[item][1]}  {Style.RESET_ALL}')
		#time.sleep(1)
		
	
	print ('\n'*1)
	print (f'Card Value   {player_hand_value}\n')
	print (f'Chip Amount: ${player_chip}')
	print (f'Bet:         ${player_bet}')
		
	
		
	

	
	
	
def show_all (player, dealer, player_chip, player_bet, player_hand_value, dealer_hand_value):
	
	print ('\n'*40)
	print ('DEALER HAND')             
	print ('===========')     		                    
	for item in range(0,len(dealer)):
		
		print (f'{suit_color(dealer[item][0])}{dealer[item][0]} {dealer[item][1]}  {Style.RESET_ALL} ')	
		
	print ('\n'*1)
	print (f'Card Value   {dealer_hand_value}')

			
			
	print ('\n'*3)	
	print ('GO LING HAND')             
	print ('============')             
	
	for item in range(0,len(player)):
		print (f'{suit_color(player[item][0])}{player[item][0]} {player[item][1]}  {Style.RESET_ALL}')
		
	
	print ('\n'*1)
	print (f'Card Value   {player_hand_value}\n')
	print (f'Bet:         ${player_bet}')
	print (f'Chip Amount: ${player_chip}')




def player_busts(player_bet):
	
	player_chip.lose_bet(player_bet)
	print ('Go Ling loose!')
	print (f'You bet ${player_bet}, you now have ${player_chip}')
	

def player_wins(player_bet):
	
	player_chip.win_bet(player_bet)
	print ('Go Ling. You won')
	print (f'Your won ${player_bet}, you now have ${player_chip}')
	
	
def dealer_busts(player_bet):
	
	#Player win the bet when dealer loose
	player_chip.win_bet(player_bet)
	print ('Dealer loose!')
	



def dealer_wins(player_bet):
	
	player_chip.lose_bet(player_bet)
	print ('Dealer Won!')
	
	
def push():

	print ('It is a tie!')
	
	
	

def player_wins(player_bet):
	
	player_chip.win_bet(player_bet)
	print ('Go Ling. You won')
	print (f'Your won ${player_bet}, you now have ${player_chip}')	
	
	

	


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
		#for x in range(0,52):
		#	print (f'{suit_color(self.deck[x][0])}{self.deck[x][0]} {self.deck[x][1]} {Style.RESET_ALL}')



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
		#print (f'This is the card list on Hand(): {self.card}')  # debug
				
		self.value += values[cards[1]]
		#print (f'This is the value of card on Hand(): {self.value}')  #debug
		
		if cards[1] == 'A':
			self.aces += 1
		#print (f'Number of Aces on Hand(): {self.aces}')   #debug
		
		return self.value
					
	def adjust_for_ace(self):
		self.value = self.value - 10
		print (f'This is the value of card on Hand(): {self.value}')  #debug
		
		return self.value
				
				
	def my_hand(self):
		return self.card
		
		
	def hand_value(self):
		return self.value
		
		
		

class Chips():
	
	def __init__(self):
		
		while True:
			try:
				self.total = int(input('How much money do you have? $'))
				self.bet = 0
			except:
				print ('Come on! Go Ling.. ')
				continue
			else:
				print (f'You have ${self.total} chips\n\n\n')
				break
		
	def __str__(self):
		return str(self.total)
		
	def win_bet(self, bet):
		self.bet = bet
		self.total += self.bet
	
	def lose_bet(self, bet):
		self.bet = bet
		self.total -= self.bet
		
	def chips_amt(self):
		return self.total


print ('\n'*40)
print ('THIS IS THE GAME OF BLACKJACK... BIG WINNER!\n\n\n\n')
print ("Go Ling! Let's play!  \n")
player_chip = Chips()


while play_again == True:
	
	# Creat a deck of 52 cards and shuffle
	mydeck = Deck()
	mydeck.shuffle()
	
	print ('\n'*50)
	# Start the game. Ask player how much money does the player has
	#print ("Go Ling! Let's play!  \n")
	#player_chip = Chips()
	
	
	# Player take the bet
	print (f"Go Ling! You have ${player_chip.chips_amt()} chips")
	player_bet = take_bet(player_chip.chips_amt())
	
	# initiate player Hand()
	player_hand = Hand()
	
	# initiate dealer Hand()
	dealer_hand = Hand()
	
	
	# Game Start
	# Player and dealer deal 2 cards
	for item in range (0,2):
		player_card = mydeck.deal()
		dealer_card = mydeck.deal()
		
		player_hand_value = player_hand.add_card(player_card)
		dealer_hand_value = dealer_hand.add_card(dealer_card)
	
	
	show_some(player_hand.my_hand(), dealer_hand.my_hand(), player_chip.chips_amt(), player_bet, player_hand.hand_value())
	# show some cards
	#show_some(player_hand.my_hand(), dealer_hand.my_hand(), player_chip.chips_amt(), player_bet, player_hand_value)
	
	
	while playing == True:
		
		
		
		show_some(player_hand.my_hand(), dealer_hand.my_hand(), player_chip.chips_amt(), player_bet, player_hand.hand_value())
		
		if player_hand.hand_value() == 21:
			player_wins(player_bet)
			break
			
		if dealer_hand.hand_value() == 21:
			dealer_wins(player_bet)
			break
		
		if player_hand.hand_value() > 21 and dealer_hand.hand_value() < 21:
			player_busts(player_bet)
			break
			
		if dealer_hand.hand_value() > 21 and player_hand.hand_value() < 21:
			dealer_busts(player_bet)
			break
			
		if dealer_hand.hand_value() > 21 and player_hand.hand_value() > 21: 
			push()
			break
			
					
		player_is_stand = hit_or_stand(mydeck,player_hand)
	
		# dealer deal 1 card if the value <= 17	
		if player_is_stand == False and dealer_hand.hand_value() <= 17:
			dealer_card = mydeck.deal()
			dealer_hand_value = dealer_hand.add_card(dealer_card)
			
			# Adjust A's value from 10 to 1 if dealer_hand_value >= 19
			if dealer_hand_value >= 19 and dealer_hand.aces > 0:
				print ('Dealer about to adjust A value')
				dealer_hand_value = dealer_hand.adjust_for_ace()
				
			
		# When player is stand.  Dealer continue to deal until hand_value() > 17
		if player_is_stand == True:
			while dealer_hand.hand_value() <= 17:
				dealer_card = mydeck.deal()
				dealer_hand_value = dealer_hand.add_card(dealer_card)
				
				# If dealer_hand_value >19 and dealer_hand.aces > 0
				if dealer_hand_value >= 19 and dealer_hand.aces > 0:
					print ('Dealer about to adjust A value')
					dealer_hand_value = dealer_hand.adjust_for_ace()
				
				show_some(player_hand.my_hand(), dealer_hand.my_hand(), player_chip.chips_amt(), player_bet, player_hand.hand_value())
	
			if player_hand.hand_value() == 21:
				player_wins(player_bet)
				
				
			if dealer_hand.hand_value() == 21:
				dealer_wins(player_bet)
				
			
			if player_hand.hand_value() > 21 and dealer_hand.hand_value() < 21:
				player_busts(player_bet)
				
				
			if dealer_hand.hand_value() > 21 and player_hand.hand_value() < 21:
				dealer_busts(player_bet)
				
				
			if dealer_hand.hand_value() > 21 and player_hand.hand_value() > 21: 
				push()
				
				
			if dealer_hand.hand_value() == player_hand.hand_value():
				push()
			
			if dealer_hand.hand_value() < 21 and player_hand.hand_value() < 21 and dealer_hand.hand_value() > player_hand.hand_value():
				dealer_wins(player_bet)
				
			if dealer_hand.hand_value() < 21 and player_hand.hand_value() < 21 and dealer_hand.hand_value() < player_hand.hand_value():
				player_wins(player_bet)
	
	input('press [enter] to continue')	
	
	show_all(player_hand.my_hand(), dealer_hand.my_hand(), player_chip.chips_amt(), player_bet, player_hand.hand_value(), dealer_hand.hand_value())
	
		
	play_again = another_round()
	
	
	
	
	
	
				
print ('Game Done')


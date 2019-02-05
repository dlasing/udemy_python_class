import random

# Declare fixed variable
suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}
playing = True



while playing == True:
	
	suits_pick = suits[random.randrange(len(suits))]
	ranks_pick = ranks[random.randrange(len(ranks))]
	values_pick = values[ranks_pick]
	
	print (f'suits: {suits_pick}')
	print (f'ranks: {ranks_pick}')	
	print (f'values: {values_pick}')
	
	
	x = input ('Play again? Y/N  ')
	if x == "Y" or x == "y":
		playing = True
	else:
		playing = False
				
				
print ('Game Done')


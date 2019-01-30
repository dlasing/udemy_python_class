import random



def display_board(board):
	print ('\n'*100)
	
	print ('   |   |   \n'   \
	       f' {board[7]} | {board[8]} | {board[9]}   \n'   \
	       '   |   |   \n'   \
	       '-----------\n'   \
	       '   |   |   \n'   \
	       f' {board[4]} | {board[5]} | {board[6]}   \n'   \
	       '   |   |   \n'   \
	       '-----------\n'   \
	       '   |   |   \n'   \
	       f' {board[1]} | {board[2]} | {board[3]}   \n'   \
	       '   |   |   \n')
	



def player_input():	
	player_list = ["?", "?"]
	
	while player_list[0] != 'X' or player_list[0] != "O":
		player_list[0] = input("Player1: Please pick a marker 'X' or 'O' ")
		
		if player_list[0] == "X":
			player_list[1] = "O"
			return player_list
			break
			
		if player_list[0] == "O":
			player_list[1] = "X"
			return player_list
			break
			
			

def place_marker(board, marker, position):	
	# Assign the board list with new position
	board[position] = marker
	return board

		
def win_check(board, mark):	
	# A list to check all possible winning matrix
	check_list = [0,1,2,3,4,5,6,7,8,9,1,4,7,2,5,8,3,6,9,3,5,7,1,5,9]
	counter = 0
	
	for item in range(1,9):
		
		if board[check_list[1+counter]] == board[check_list[2+counter]] == board[check_list[3+counter]] == mark:				
			print (f"Yeah! You just won the game!")
			counter+=3
			return True		
		else:	
			counter+=3
	
	
			
def choose_first():
	player = random.randint(0,1)
	return player			
			

def space_check(board, position):	
		if board[position] == ' ':
			return True
		else:
			return False
			
			
			
def full_board_check(board):
	
	for item in range(1,10):
		if board[item] == " ":
			#Return False if "" found
			return False
	 	
	# Return True if no "" found
	return True				
			
			
			
def player_choice(board):
	position = 0
	
	while position < 1:
		position = int(input ("Please enter your position [1-9]  "))
	
		# If the position is taken
		if position > 9 or space_check(board, position) == False :
			#Reset position
			position = 0
	
	return position
	
				
		
def replay():	
	play_again = ""
	
	while play_again != "N" or play_again != "Y":
		play_again = input ("Do you want to play again? [Y/N]")
		return play_again == "Y"
		
	
	
def ready_to_play():
	yesno = "Yes"
	
	while yesno != "Yes" or yesno != "No":
		yesno = input ('Are you ready to play? Enter Yes or No\n')
		if yesno == "Yes":
			return True
		else:
			return False
			
				
 
	
	
	
	
print ("Welcome to Tic Tac Toe!")	
playagain = True

while playagain == True:
	# Start the Tic Tac Toe game
	marker = player_input()
	print (f'Player 1 is: {marker[0]}')
	print (f'Player 2 is: {marker[1]}\n')	
	
	# Random pick which player will play first
	who_is_first = choose_first()
	print (f'Player {who_is_first+1} will go first')
	
	ready_to_play()
	
	#Reset the board entry
	play_board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
	
	while full_board_check(play_board) == False:
		display_board(play_board)
		# Mark to the board
		play_board[player_choice(play_board)] = marker[who_is_first]
		display_board(play_board)
		
		# Any Winner ? 
		if win_check(play_board, marker[who_is_first]) == True:
			break
		
		# Step to switch player
		if who_is_first == 0:
			who_is_first = 1
		else:
			who_is_first = 0
			
	playagain = replay()
	
	
	
	
	
	
	
	
		

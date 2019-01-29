import random

print ('\n'*100)

def display_board(board):

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
		player_list[0] = input("Please pick a marker 'X' or 'O' ")
		
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
	
	check_list = [0,1,2,3,4,5,6,7,8,9,1,4,7,2,5,8,3,6,9,3,5,7,1,5,9]
	counter = 0
	
	for item in range(1,9):
		
		#print (f'Checking... {check_list[1+counter]}, {check_list[2+counter]}, {check_list[3+counter]}')
		if board[check_list[1+counter]] == board[check_list[2+counter]] == board[check_list[3+counter]] == mark:
			
			
			print (f"Marker: {mark} WON")
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
		if board[item] == "":
			#Return False if "" found
			return False
	 	
	# Return True if no "" found
	return True				
			
			
			
def player_choice(board):
	
	position = input ("Please enter your position [1-9]")
	
	if space_check(board, position) == True:
		return position
		
		
		
def replay():
	
	play_again = ""
	
	while play_again != "N" or play_again != "Y":
		play_again = input ("Do you want to play again? [Y/N]")
		return play_again == "Y"
		
		
		
test_board = ['#','X','O','X','X','X','O','X','O','X']
display_board(test_board)
x = player_input()

#new_board = place_marker(test_board, 'X', 9)
#display_board(new_board)

#win_check(new_board, 'X')

space_check(test_board, 4)

full_board_check(test_board)


print (f'Player 1 is: {x[0]}')
print (f'Player 2 is: {x[1]}')


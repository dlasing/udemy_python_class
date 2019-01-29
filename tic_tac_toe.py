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
	



def play_input():
	player_list = ["?", "?"]
	print(type(player_list))
	
	print (player_list[0])
	
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
			
			
		
		
			

test_board = ['#','X','O','X','O','X','O','X','O','X']
display_board(test_board)
x = play_input()

print (f'Player 1 is: {x[0]}')
print (f'Player 2 is: {x[1]}')


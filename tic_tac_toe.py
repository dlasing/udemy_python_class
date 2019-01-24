#print('\n'*100)

def display_board(board):
	
	bar = [" ", " ", " ", "|", " ", " ", " ", "|", " ", " ", " "]	
	row = '-----------'
		
	for print_row in range (1,4):
		for print_bar in range (1,4):
			
			print (bar[0] + bar[1] + bar[2] + bar[3] +bar[4] + bar[5] + bar[6] + bar[7]+ bar[8] + bar[9] )
						
		if print_row < 3:
			print (row)


display_board ('a')

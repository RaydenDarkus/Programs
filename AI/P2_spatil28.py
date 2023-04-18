# Shreyas Patil
# G01382371
# CS 580: Project 2

import numpy as np
import pygame
import sys
import random
import math
import time

# This is a 6x7 grid with 6 rows and 5 columns
rows = 6
columns = 7

# Define the colors for the game board
TAN = (230, 219, 172)
BEIGE = (238, 220, 154)
MACAROON = (249, 224, 118)
HAZEL_WOOD = (201, 187, 142)
GRANOLA = (214, 184, 90)
OAT = (223, 201, 138)
EGG_NOG = (250, 226, 156)
FAWN = (200, 169, 81)
SUGAR_COOKIE = (243, 234, 175)
SAND = (216, 184, 99)
SEPIA = (227, 183, 120)
LATTE = (231, 194, 120)
OYSTER = (220, 215, 160)
BISCOTTI = (227, 197, 101)
PARMESEAN = (253, 233, 146)
HAZELNUT = (189, 165, 88)

palette = {"TAN":TAN,"BEIGE": BEIGE,"MACAROON": MACAROON,"HAZEL_WOOD": HAZEL_WOOD,"GRANOLA": GRANOLA,"OAT": OAT,"EGG_NOG": EGG_NOG,"FAWN": FAWN,
	   "SUGAR_COOKIE": SUGAR_COOKIE,"SAND": SAND,"SEPIA": SEPIA,"LATTE":LATTE,"OYSTER": OYSTER,"BISCOTTI": BISCOTTI,"PARMESIAN": PARMESEAN,"HAZELNUT": HAZELNUT}

#Main colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (128, 128, 128)

# Player and AI Denotion
PLAYER = 0
AI = 1

#Player piece and AI piece Denotion
EMPTY = 0
PLAYER_PIECE = 1
AI_PIECE = 2

WINDOW_LENGTH = 4

# Create board matrix filled with 0's initially
def create_board():
	board = np.zeros((rows,columns))
	return board

#drop a piece on the board
def drop_piece(board, row, col, piece):
	board[row][col] = piece

#Print the board ie the matrix
def print_board(board):
	print(np.flip(board, 0))

def is_valid_location(board, col):
	return board[rows-1][col] == 0

def get_next_open_row(board, col):
	for r in range(rows):
		if board[r][col] == 0:
			return r
		
#Winning Conditions
def winning_move(board, piece):
	# Check horizontal locations for win
	for c in range(columns-3):
		for r in range(rows):
			if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
				return True

	# Check vertical locations for win
	for c in range(columns):
		for r in range(rows-3):
			if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
				return True

	# Check positively sloped diaganols
	for c in range(columns-3):
		for r in range(rows-3):
			if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
				return True

	# Check negatively sloped diaganols
	for c in range(columns-3):
		for r in range(3, rows):
			if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
				return True
	
	# Check if it forms a square
	# for c in range(columns-1):
	# 	for r in range(rows-1):
	# 		if board[r][c] == piece and board[r][c+1] == piece and board[r+1][c] == piece and board[r+1][c+1] == piece:
	# 			return True

# Evaluate the score		
def evaluate_window(window, piece):
	score = 0
	opp_piece = PLAYER_PIECE
	if piece == PLAYER_PIECE:
		opp_piece = AI_PIECE

	if window.count(piece) == 4:
		score += 100
	elif window.count(piece) == 3 and window.count(EMPTY) == 1:
		score += 5
	elif window.count(piece) == 2 and window.count(EMPTY) == 2:
		score += 2

	if window.count(opp_piece) == 3 and window.count(EMPTY) == 1:
		score -= 4

	return score

def score_position(board, piece):
	score = 0

	## Score center column
	center_array = [int(i) for i in list(board[:, columns//2])]
	center_count = center_array.count(piece)
	score += center_count * 3

	## Score Horizontal
	for r in range(rows):
		row_array = [int(i) for i in list(board[r,:])]
		for c in range(columns-3):
			window = row_array[c:c+WINDOW_LENGTH]
			score += evaluate_window(window, piece)

	## Score Vertical
	for c in range(columns):
		col_array = [int(i) for i in list(board[:,c])]
		for r in range(rows-3):
			window = col_array[r:r+WINDOW_LENGTH]
			score += evaluate_window(window, piece)

	## Score posiive sloped diagonal
	for r in range(rows-3):
		for c in range(columns-3):
			window = [board[r+i][c+i] for i in range(WINDOW_LENGTH)]
			score += evaluate_window(window, piece)

	## Score negative sloped diagonal
	for r in range(rows-3):
		for c in range(columns-3):
			window = [board[r+3-i][c+i] for i in range(WINDOW_LENGTH)]
			score += evaluate_window(window, piece)

	# for r in range(rows-1):
	# 	for c in range(columns-1):
	# 		window = [board[r][c],board[r][c+1],board[r+1][c],board[r][c+1]]
	# 		score += evaluate_window(window, piece)

	return score

# Get the locations which are not filled with pieces			
def get_valid_locations(board):
	valid_locations = []
	for col in range(columns):
		if is_valid_location(board, col):
			valid_locations.append(col)
	return valid_locations		
	
def is_terminal_node(board):
	return winning_move(board, PLAYER_PIECE) or winning_move(board, AI_PIECE) or len(get_valid_locations(board)) == 0

def minimax(board, depth, alpha, beta, maximizingPlayer):
	valid_locations = get_valid_locations(board)
	is_terminal = is_terminal_node(board)
	if depth == 0 or is_terminal:
		if is_terminal:
			if winning_move(board, AI_PIECE):
				return (None, 100000000000000)
			elif winning_move(board, PLAYER_PIECE):
				return (None, -10000000000000)
			else: # Game is over, no more valid moves
				return (None, 0)
		else: # Depth is zero
			return (None, score_position(board, AI_PIECE))
	if maximizingPlayer:
		value = -math.inf
		column = random.choice(valid_locations)
		for col in valid_locations:
			row = get_next_open_row(board, col)
			b_copy = board.copy()
			drop_piece(b_copy, row, col, AI_PIECE)
			new_score = minimax(b_copy, depth-1, alpha, beta, False)[1]
			if new_score > value:
				value = new_score
				column = col
			alpha = max(alpha, value)
			if alpha >= beta:
				break
		return column, value

	else: # Minimizing player
		value = math.inf
		column = random.choice(valid_locations)
		for col in valid_locations:
			row = get_next_open_row(board, col)
			b_copy = board.copy()
			drop_piece(b_copy, row, col, PLAYER_PIECE)
			new_score = minimax(b_copy, depth-1, alpha, beta, True)[1]
			if new_score < value:
				value = new_score
				column = col
			beta = min(beta, value)
			if alpha >= beta:
				break
		return column, value

def get_valid_locations(board):
	valid_locations = []
	for col in range(columns):
		if is_valid_location(board, col):
			valid_locations.append(col)
	return valid_locations

def pick_best_move(board, piece):
	valid_locations = get_valid_locations(board)
	best_score = -10000
	best_col = random.choice(valid_locations)
	for col in valid_locations:
		row = get_next_open_row(board, col)
		temp_board = board.copy()
		drop_piece(temp_board, row, col, piece)
		score = score_position(temp_board, piece)
		if score > best_score:
			best_score = score
			best_col = col

	return best_col


# Draw the board in the screen			
def draw_board(clr,board):
	for c in range(columns):
		for r in range(rows):
			pygame.draw.rect(screen, clr, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
			pygame.draw.circle(screen, GREY, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
	
	for c in range(columns):
		for r in range(rows):		
			if board[r][c] == PLAYER_PIECE:
				pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
			elif board[r][c] == AI_PIECE: 
				pygame.draw.circle(screen, WHITE, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
	pygame.display.update()
	
board = create_board()
#Initialize the game
pygame.init()
#Size of the square
SQUARESIZE = 100
width = columns * SQUARESIZE
height = (rows+1) * SQUARESIZE
size = (width, height)
RADIUS = int(SQUARESIZE/2 - 10)
screen = pygame.display.set_mode(size)

# Set the font of the game
myfont = pygame.font.SysFont("monospace", 32)
font = pygame.font.Font("freesansbold.ttf",32)
clock = pygame.time.Clock()

#Choose your color
def color():
	pygame.display.set_caption("Set color")
	screen.fill(BLACK)
	pygame.draw.rect(screen, BLACK, (width, 0, width, 600))
	font = pygame.font.Font("freesansbold.ttf",20)
	i,j = 200,1

	for key,value in palette.items():
			color_text = "Press "+str(j)+" for "+str(key)
			text = font.render(color_text, True, value)
			text_rect = text.get_rect()
			text_rect.topleft = (200, i)
			i += 20		
			j +=1
			screen.blit(text, text_rect)
	pygame.display.update()

	while True:
		for event in pygame.event.get():
			#Exit the game
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN:
				key=pygame.key.get_pressed()
				if key[pygame.K_7]:
					clr = palette["EGG_NOG"]
				if key[pygame.K_8]:
					clr = palette["FAWN"]
				if key[pygame.K_9]:
					clr = palette["SUGAR_COOKIE"]
				if key[pygame.K_1] and key[pygame.K_0]:
					clr = palette["SAND"]
				if key[pygame.K_1] and key[pygame.K_1]:
					clr = palette["SEPIA"]
				if key[pygame.K_1] and key[pygame.K_2]:
					clr = palette["LATTE"]
				if key[pygame.K_1] and key[pygame.K_3]:
					clr = palette["OYSTER"]
				if key[pygame.K_1] and key[pygame.K_4]:
					clr = palette["BISCOTTI"]
				if key[pygame.K_1] and key[pygame.K_5]:
					clr = palette["PARMESIAN"]
				if key[pygame.K_1] and key[pygame.K_6]:
					clr = palette["HAZELNUT"]
				elif key[pygame.K_1]:
					clr = palette["TAN"]
				elif key[pygame.K_2]:
					clr = palette["BEIGE"]
				elif key[pygame.K_3]:
					clr = palette["MACAROON"]
				elif key[pygame.K_4]:
					clr = palette["HAZEL_WOOD"]
				elif key[pygame.K_5]:
					clr = palette["GRANOLA"]
				elif key[pygame.K_6]:
					clr = palette["OAT"]

				name(clr)
				
# Enter the name. After entering the name, press Enter to go to the next function
def name(clr):
	pygame.display.set_caption("Enter Details")
	screen.fill(BLACK)
	font = pygame.font.Font("freesansbold.ttf",32)
	text = font.render("Enter Name:", True, clr)
	text_rect = text.get_rect()
	text_rect.topleft = (100, 100)
	screen.blit(text, text_rect)
	text_box = pygame.Rect(300,90,100,50)
	active = False
	user_ip = ''
	color = pygame.Color('purple')
	pygame.display.update()
	post = True
	while post:
		pygame.draw.rect(screen, BLACK, pygame.Rect(300, 70, 500, 500))
		if active:
			color = pygame.Color('red')
		else:
			color = pygame.Color('purple')
		pygame.draw.rect(screen,color, text_box,4)
		surf = font.render(user_ip,True,'orange')
		screen.blit(surf, (text_box.x +5 , text_box.y +5))
		text_box.w = max(100, surf.get_width()+10)
		pygame.display.update()
		for event in pygame.event.get():
				#Exit the game
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if event.type == pygame.MOUSEBUTTONDOWN:
					if text_box.collidepoint(event.pos):
						active = True
					else:
						active = False
				if event.type == pygame.KEYDOWN:
					if active:
						if event.key == pygame.K_BACKSPACE:
							user_ip = user_ip[:-1]
						else:
							user_ip += event.unicode
						if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
							# play_game(clr,user_ip[:len(user_ip)-1])
							selection(clr,user_ip[:len(user_ip)-1])
							post = False

def selection(clr, Name):
	turn = 0
	font = pygame.font.Font("freesansbold.ttf",32)
	select_text = "Press 1 for "+Name+" Press 2 for Agent"
	text = font.render(select_text, True, clr)
	text_rect = text.get_rect(center=(width/2, height/2))
	screen.blit(text, text_rect)
	pygame.display.update()
	while True:
		for event in pygame.event.get():
			#Exit the game
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN:
				key = pygame.key.get_pressed()
				if key[pygame.K_1]:
					turn = 0
				if key[pygame.K_2]:
					turn = 1
				deepness(clr, Name, turn)
				break

# Select the depth
def deepness(clr, Name, turn):
	screen.fill(BLACK)
	font = pygame.font.Font("freesansbold.ttf",32)
	text = font.render("Press for depth 1-5: ", True, clr)
	text_rect = text.get_rect(center=(width/2, height/2))
	screen.blit(text, text_rect)
	pygame.display.update()
	while True:
		for event in pygame.event.get():
			#Exit the game
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN:
				key = pygame.key.get_pressed()
				if key[pygame.K_1] or key[pygame.K_KP0]:
					depth = 1
				if key[pygame.K_2] or key[pygame.K_KP0]:
					depth = 2
				if key[pygame.K_3] or key[pygame.K_KP0]:
					depth = 3
				if key[pygame.K_4] or key[pygame.K_KP0]:
					depth = 4
				if key[pygame.K_5] or key[pygame.K_KP0]:
					depth = 5
				play_game(clr,Name,turn, depth)

# Function for calculating number of moves
def number_of_moves(board):
	num = 0
	for r in range(rows):
		for c in range(columns):
			if board[r][c]!=0:
				num +=1
	return num			

# Play the game
def play_game(clr, user_ip, turn, depth):
	game_over = False
	pygame.display.set_caption("Connect 4 Game")
	draw_board(clr,board)
	pygame.display.update()
	start_time = time.time()
	while not game_over:
		# Calculate time elapsed since start
		elapsed_time = int(time.time() - start_time)
		minutes = elapsed_time //60
		seconds = elapsed_time % 60
		# Render timer text
		pygame.draw.rect(screen, GREY, (width - 200, 0, 200, 40))
		text = font.render(f"Time: {minutes:02d}:{seconds:02d}", True, (0, 0, 0))
		text_rect = text.get_rect()
		# Position timer text in top right corner
		text_rect.topright = (width - 10, 10)
		# Draw timer text on screen
		screen.blit(text, text_rect)
		# Update the display
		pygame.display.update()

		for event in pygame.event.get():

			#Exit the game
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

			pygame.draw.rect(screen, GREY, (0,0, width, SQUARESIZE))
			if event.type == pygame.MOUSEMOTION:
				posx = event.pos[0]
				if turn == PLAYER:
					pygame.draw.circle(screen, BLACK, (posx, int(SQUARESIZE/2)), RADIUS)

			pygame.display.update()

			# Ask for player 1 input
			if event.type == pygame.MOUSEBUTTONDOWN:
				pygame.draw.rect(screen, GREY, (0,0, width, SQUARESIZE))

				#print(event.pos)
				# Ask for Player 1 Input
				if turn == PLAYER:
					posx = event.pos[0]
					col = int(math.floor(posx/SQUARESIZE))

					if is_valid_location(board, col):
						
						row = get_next_open_row(board, col)
						drop_piece(board, row, col, 1)

						if winning_move(board, PLAYER_PIECE):
								winner = user_ip + " wins!!"
								label = font.render(winner, 1, BLACK)
								screen.blit(label, (40,10))
								game_over = True

						turn += 1
						turn %= 2
						print_board(board)
						draw_board(clr,board)

			# Ask for player 2 input(AI)
			if turn == AI and not game_over:
				col, minimax_score = minimax(board, depth, -math.inf, math.inf, True)
				if is_valid_location(board, col):
					pygame.time.wait(500)
					row = get_next_open_row(board, col)
					drop_piece(board, row, col, AI_PIECE)

					if winning_move(board, AI_PIECE):
						winner = "Agent wins!!" + user_ip + " loses"
						label = font.render(winner, 1, WHITE)
						screen.blit(label, (40,10))
						game_over = True

					turn += 1
					turn %= 2
					print_board(board)
					draw_board(clr,board)

			# Game Tied
			if len(get_valid_locations(board)) == 0 and game_over:
					winner = "Game Tied"
					label = font.render(winner, 1, WHITE)
					screen.blit(label, (40,10))
					game_over = True
					print_board(board)
					draw_board(clr,board)

		# If game is over wait then display the output
		if game_over:
			minutes = elapsed_time //60
			seconds = elapsed_time % 60
			# Render timer text
			pygame.draw.rect(screen, GREY, (width - 200, 0, 200, 40))
			text = font.render(f"Time: {minutes:02d}:{seconds:02d}", True, (0, 0, 0))
			moves_text = "No of moves: " + str(number_of_moves(board))
			moves_text_ui = font.render(moves_text, True, (0, 0, 0))
			moves_text_ui_rect = moves_text_ui.get_rect()
			text_rect = text.get_rect()
			# Position timer text in top right corner
			text_rect.topright = (width - 10, 10)
			moves_text_ui_rect.topleft = (50,50)
			# Draw timer text on screen
			screen.blit(text, text_rect)
			screen.blit(moves_text_ui, moves_text_ui_rect)
			pygame.display.update()
			print('Elapsed Time:',str(elapsed_time),'No: of moves: ',str(number_of_moves(board)))
			pygame.time.wait(10000)

if __name__=='__main__':
	color()
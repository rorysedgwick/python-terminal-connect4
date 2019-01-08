import sys

def clear():
  print('\n' * 100)

def create_board(board_config):
  board = []
  for i in range(board_config[0]):
    board.append([board_config[2]] * board_config[1])

  return board

def show_board(board):
  for row in board:
    print(' '.join(row))
  print('\n')

def take_turn(player, counter, board, board_tile):

  valid_column = False

  while not valid_column:
    print(player + ': Select a column:')
    col = int(input());
    valid_column = validate_input(board, board_tile, col)

  new_board = add_counter_to_board(board, board_tile, counter, col)
  return new_board

def validate_input(board, board_tile, col):
  if col > len(board[0]):
    print('Pick a column between 0 and ' + str(len(board[0])))
    return False
  elif board[0][col] != board_tile:
    print('This column is already full, pick another')
    return False
  else:
    return True

def add_counter_to_board(board, board_tile, counter, col):
  for i in range(len(board) -1, -1, -1):
    if board[i][col] != board_tile:
      continue
    else:
      board[i][col] = counter
      break
  return board

def four_connected(board, counter):
  connect_four = check_for_connect_four(board, counter)
  return connect_four

def check_for_connect_four(board, counter):
  return check_horizontal(board, counter) or check_vertical(board, counter)

def check_horizontal(board, counter):
  for row in board:
    for col in range(len(row) - 3):
      if row[col] == counter and row[col+1] == counter and row[col+2] == counter and row[col+3] == counter:
        return True
      else:
        continue
  return False

def check_vertical(board, counter):
  for col in range(len(board[0])):
    for row in range(len(board) - 3):
      if board[row][col] == counter and board[row+1][col] == counter and board[row+2][col] == counter and board[row+3][col] == counter:
        return True
      else:
        continue
  return False

def check_diagonal(board, counter):
  pass

def initialize_players():
  print('Player 1: Enter your name:')
  player_1 = input()
  print('Player 1: Enter your playing counter symbol:')
  counter_1 = input()
  print('Player 2: Enter your name:')
  player_2 = input()
  print('Player 2: Enter your playing counter symbol:')
  counter_2 = input()

  return [player_1, player_2, counter_1, counter_2]

def initialize_board():
  print('How many rows should the board have?:')
  rows = int(input())
  print('How many columns should the board have?:')
  cols = int(input())
  print('Enter a single character to use as a board tile:')
  board_tile = input()

  return [rows, cols, board_tile]

def connect_four():
  print('Starting game of Connect Four:', end='\n\n')
  print('Do you want to use the default settings?')
  use_default = input().lower()

  if use_default == 'y' or use_default == 'yes':
    player_config = ['Player 1', 'Player 2', 'O', 'X']
    board_config = [6, 8, '_']
  else:
    player_config = initialize_players()
    board_config = initialize_board()

  clear()
  board = create_board(board_config)
  maximum_moves = board_config[0] * board_config[1]
  board_tile = board_config[2]
  counters = player_config[2:4]

  show_board(board)

  for i in range(maximum_moves):
    if i % 2 == 0:
      player = player_config[0]
      counter = player_config[2]
    else:
      player = player_config[1]
      counter = player_config[3]
    
    new_board = take_turn(player, counter, board, board_tile)
    show_board(new_board)

    if four_connected(new_board, counter):
      print('We have a winner!')
      print('Congratulations {}'.format(player), end='\n')
      sys.exit()

connect_four()

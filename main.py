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

def take_turn(turn_number, board, board_config, player_config):
  if turn_number % 2 == 0:
    player = player_config[0]
    counter = player_config[2]
  else:
    player = player_config[1]
    counter = player_config[3]

  valid_column = False
  board_tile = board_config[2]

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

def four_connected(board, counters):

  connect_four = False
  for counter in counters:
    connect_four = check_for_connect_four(board, counter)

  return connect_four

def check_for_connect_four(board, counter):
  return check_horizontal(board, counter)

def check_horizontal(board, counter):
  for row in board:
    for i in range(len(row) - 4):
      if row[i] == counter and row[i+1] == counter and row[i+2] == counter and row[i+3] == counter:
        return True
      else:
        continue
  return False

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
  counters = player_config[2:4]

  show_board(board)
  turn_number = 0

  while not four_connected(board, counters):
    new_board = take_turn(turn_number, board, board_config, player_config)
    show_board(new_board)
    turn_number += 1

    if four_connected(new_board, counters):
      print('We have a winner!')
      sys.exit()

connect_four()

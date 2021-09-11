import random # for randint() and choice()
import sys # for exit()

# Drawing the Board Data Structure on the Screen
def draw_board(board):
    # This function will prints out the board that it was passed. Return None
    HLINE = '  +---+---+---+---+---+---+---+---+'
    VLINE = '  |   |   |   |   |   |   |   |   |'
    print('    1   2   3   4   5   6   7   8')
    print(HLINE)

    for y in range(8):
        print(VLINE)
        print(y + 1, end=' ')
        for x in range(8):
            print('| {}'.format(board[x][y]), end=' ')
        print('|')
        print(VLINE)
        print(HLINE)
        pass

# Resetting the Game Board
def reset_board(board):
    # Blank out the board it is passed, except for the original starting position
    for x in range(8):
        for y in range(8):
            board[x][y] = ' '

    # Starting pieces
    board[3][3] = 'X'
    board[3][4] = 'O'
    board[4][3] = 'O'
    board[4][4] = 'X'

# Create a New Game Board Data structure
def get_new_board():
    # Create a brand new, blank board data structure
    board = []
    for i in range(8):
        board.append([' '] * 8)

    return board

# Checking if a move is valid
def is_valid_move(board, tile, xstart, ystart):
    # Returns False if the player's move on the space xstart, ystart is invalid
    # If it is a valid move, returns a list of spaces that would become the player's if they make a move
    if board[xstart][ystart] != ' ' or not is_on_board(xstart, ystart):
        return False
    
    board[xstart][ystart] = tile # temporarily set the tile on the board

    if tile == 'X':
        other_tile = 'O'
    else:
        other_tile = 'X'

    tiles_to_flip = []

    for xdirection, ydirection in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
        x, y = xstart, ystart
        x += xdirection # First step in the direction
        y += ydirection # First step in the direction

        if is_on_board(x, y) and board[x][y] == other_tile:
            # There is a pieces belongin to the other player next to our pieces
            x += xdirection
            y += ydirection
            if not is_on_board(x, y):
                continue

            while board[x][y] == other_tile:
                x += xdirection
                y += ydirection
                if not is_on_board(x, y): # break out the while loop then continue for loop
                    break
            if not is_on_board(x, y):
                continue

            if board[x][y] == tile:
                ## There are pieces to flip over. Go in the reverse direction until we reach the original space, noting all the tiles along the way.
                while True:
                    x -= xdirection
                    y -= ydirection
                    if x == xstart and y == ystart:
                        break
                    tiles_to_flip.append([x, y])

    board[xstart][ystart] = ' ' # restore the empty space
    if len(tiles_to_flip) == 0:  #if no tiles was fipped, this is not a valid move
        return False

    return tiles_to_flip

#Checking for Valid coordinates
def is_on_board(x, y):
    return x >= 0 and x <= 7 and y >= 0 and y <= 7

# Getting a List with All Valid Move
def get_board_with_valid_moves(board, tile):
    # Return a new boad with '.' marking the valid moves the given player can make
    dupe_board = get_board_copy(board)

    for x, y in get_valid_moves(dupe_board, tile):
        dupe_board[x][y] = '.'

    return dupe_board

def get_valid_moves(board, tile):
    # Return a list of [x, y] lists of valid moves for the given player on the given board
    valid_moves = []

    for x in range(8):
        for y in range(8):
            if is_valid_move(board, tile, x, y) != False:
                valid_moves.append([x, y])

    return valid_moves

# Getting the Score of the Game Board
def get_score_of_board(board):
    # Determine the score by couting the tiles. Return the dictionary with the key X and O
    x_score = 0
    o_score = 0

    for x in range(8):
        for y in range(8):
            if board[x][y] == 'X':
                x_score += 1
            if board[x][y] == 'O':
                o_score += 1
    
    return {'X':x_score, 'O':o_score}

# Getting the Player's Tile Choice
def enter_player_tile():
    # Let the player type which tile they want to be
    tile = ''

    while tile not in ['x', 'o']:
        tile = input('Do you want to X or O?\n')
    
    if tile == 'x':
        return ('X', 'O')
    else:
        return ('O', 'X')

# Determining Who Goes First
def who_goes_first():
    # Random choose the player who goes first
    if random.randint(0, 1) == 0:
        return 'Player'
    else:
        return 'Computer'

# Asking the Player to Play Again
def play_again():
    # This function return True if player want to play again, otherwise return False
    print('Do you want to play again? (Yes or No)')
    return input().lower().startswith('y')

# Placing Down a Tile on the Game Board
def make_move(board, tile, xstart, ystart):
    # Place the tile on the board at xstart, ystart , and flip any of the opponent's pieces
    tiles_to_flip = is_valid_move(board, tile, xstart, ystart)

    if tiles_to_flip == False:
        return False
    
    board[xstart][ystart] = tile
    for x, y in tiles_to_flip:
        board[x][y] = tile

    return True

# Copying the Board Data Structure
def get_board_copy(board):
    # Make a duplicate of the board list and return duplicate
    dupe_board = get_new_board()

    for x in range(8):
        for y in range(8):
            dupe_board[x][y] = board[x][y]

    return dupe_board

# Determining if a Space is on a Corner
def is_on_corner(x, y):
    # Return True if the position is in one of the four corner
    return (x == 0 and y == 0) or (x == 7 and y == 0) or (x == 0 and y == 7) or (x == 7 and y == 7)

# Getting the Player's Move
def get_player_move(board, player_tile):
    # Let the player type in their move
    # Return the move as [x, y] (or return the string 'Hint' or 'quit')

    DIGITS1TO8 = '1 2 3 4 5 6 7 8'.split()

    while True:
        print('Enter your move, or type quit to end the game, or hints to turn on/off hints.')
        move = input().lower()

        if move == 'quit':
            return 'quit'
        if move == 'hints':
            return 'hints'

        if len(move) == 2 and move[0] in DIGITS1TO8 and move[1] in DIGITS1TO8:
            x = int(move[0]) - 1
            y = int(move[1]) - 1

            if is_valid_move(board, player_tile, x, y) == False:
                continue
            else:
                break
        else:
            print('That is not a valid move. Type the x digit (1-8) and y digit (1-8).')
            print('For example, 81 will be the top-right coner')

    return [x, y]

# Get the Computer's Move
def get_computer_move(board, computer_tile):
    # Giving the board and the computer's tile, determine where to move and return that move as [x, y] list
    possible_move = get_valid_moves(board, computer_tile)

    # Randomize the other of possible move
    random.shuffle(possible_move)

    # Corner moves are the best moves
    for x, y in possible_move:
        if is_on_corner(x, y):
            return [x , y]

    # Get a List of the Best Scoring Moves
    # Go through all the possible moves and remember the best scoring move
    best_score = -1
    for x, y in possible_move:
        dupe_board = get_board_copy(board)
        make_move(dupe_board, computer_tile, x, y)
        score = get_score_of_board(dupe_board)[computer_tile]
        
        if score > best_score:
            best_move = [x, y]
            best_score = score

    return best_move

# Printing the Scores to the Board
def show_point(player_tile, computer_tile):
    # Prints out the current score
    score = get_score_of_board(board)

    print('You have {} points. The computer has {} points.'.format(score[player_tile], score[computer_tile]))

#AI SIM 3 PART
def get_random_move(board, tile):
    # Return a random move
    return random.choice(get_valid_moves(board, tile))

def is_on_side(x, y):
    return x == 0 or x == 7 or y == 0 or y == 7

def get_corner_side_best_move(board, tile):
    # Return a corner move, or a side move, or the best moves
    possible_moves = get_valid_moves(board, tile)

    # Randomize the the other of the possible move list
    random.shuffle(possible_moves)

    # Always go for corner if available
    for x, y in possible_moves:
        if is_on_corner(x, y):
            return [x, y]

    # If there are no cornet, return a side move
    for x, y in possible_moves:
        if is_on_side(x, y):
            return [x, y]

    return get_computer_move(board, tile)

def get_side_best_move(board, tile):
    # Return a corner move, or a side move, or the best moves
    possible_moves = get_valid_moves(board, tile)

    # Randomize the order of the possible moves
    random.shuffle(possible_moves)

    # Return a side move, if availabe
    for x, y in possible_moves:
        if is_on_side(x, y):
            return [x, y]
    
    return get_computer_move(board, tile)

def get_worst_move(board, tile):
    # Return the move that flips the least number of tiles
    possible_moves = get_valid_moves(board, tile)

    # Randomize the order of the possible moves
    random.shuffle(possible_moves)

    # Go through all the possible moves and remember the best scoring moves
    worst_score = 64
    for x, y in possible_moves:
        dupe_board = get_board_copy(board)
        make_move(dupe_board, tile, x, y)
        score = get_score_of_board(dupe_board)[tile]

        if score < worst_score:
            worst_move = [x, y]
            worst_score = score

    return worst_move

def get_corner_worst_move(board, tile):
    # Return the move that flips the least number of tiles
    possible_moves = get_valid_moves(board, tile)

    # Randomize the order of the possible moves
    random.shuffle(possible_moves)

    # Always go for the corner if available
    for x, y in possible_moves:
        if is_on_corner(x, y):
            return [x, y]

    return get_worst_move(board, tile)

# The Start of The Game
print('Welcome to Reversi!!!')

x_wins = 0
o_wins = 0
ties = 0
num_games = int(input('Enter the number of games to run: '))

for game in range(num_games):
    print(f'Game #{game}:', end=' ')
    # Reset the board and the game
    board = get_new_board()
    reset_board(board)

    if who_goes_first() == 'Player':
        turn = 'X'
    else:
        turn = 'O'
    
    while True:
        # Drawing Everything on the Screen
        # Display the final score
        score = get_score_of_board(board)

        if turn == 'X':
            # X's turn
            other_tile = 'O'
            x, y = get_computer_move(board, 'X')
            make_move(board, 'X', x, y)
        else:
            # O's turn
            other_tile = 'X'
            x, y = get_corner_side_best_move(board, 'O')
            make_move(board, 'O', x, y)
        
        if get_valid_moves(board, other_tile) == []:
            break
        else:
            turn = other_tile

    # Display the final score
    score = get_score_of_board(board)

    print('X scored {} points. O scored {} points'.format(score['X'], score['O']))

    if score['X'] > score['O']:
        x_wins += 1
    elif score['X'] < score['O']:
        o_wins += 1
    else:
        ties += 1

num_games = float(num_games)
x_percent = round(((x_wins / num_games) * 100), 2)
o_percent = round(((o_wins / num_games) * 100), 2)
tie_percent = round(((ties / num_games) * 100), 2)

print(f'X win {x_wins} games ({x_percent}%), O win {o_wins} games ({o_percent}%), ties for {ties}  game ({tie_percent}%) of total {int(num_games)} games!')



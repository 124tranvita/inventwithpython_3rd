import random

def draw_board(board):
    #this function prints out the board that it was passed
    #'board' is a list of ten strings representing the board (ignore the index 0)
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])

def input_player_letter():
    #let the player type which the letter they want to be
    #return the set that (player's mark, computer's mark)
    choice = ''
    while choice not in ['x', 'o']:
        choice = input('Do you want to be X or O? ').lower()
    if choice == 'x':
        return ('X', 'O')
    else:
        return ('O', 'X')

def who_go_first():
    #randomly choose the player who go first
    if random.randint(0,1) == 1:
        return 'player'
    else:
        return 'computer'

def play_again():
    #This fuction return True if player want to play again or otherwise it return False
    choice = input('Play again? Y or N ')
    if choice.lower().startswith('y'):
        return True

def make_move(board, letter, move):
    board[move] = letter

def is_winner(board, letter):
    #Given the board and the player's letter, this fuction will return True if player has won
    return (
        (board[7] == board[8] == board[9] == letter) or #across the top
        (board[4] == board[5] == board[6] == letter) or #across the middle
        (board[1] == board[2] == board[3] == letter) or #across the bottom
        (board[1] == board[4] == board[7] == letter) or #down the left side
        (board[2] == board[5] == board[8] == letter) or #down the middle
        (board[3] == board[6] == board[9] == letter) or #down the right side
        (board[1] == board[5] == board[9] == letter) or #diagonal
        (board[3] == board[5] == board[7] == letter) #diagonal
    )

def get_board_copy(board):
    #Make a duplicate of the board and return it duplicates
    copy_board = []
    for i in board:
        copy_board.append(i)
    return copy_board

def is_space_free(board, move):
    #Return True if passed move is free on passed board
    return board[move] == ' '

def get_player_move(board):
    #Let the player type in their move
    move = 0
    while move not in list(range(1,10)) or not is_space_free(board, move):
        try:
            move = int(input('What is your next move? (1 -> 9) '))
        except:
            print('Please enter number only!!!')
        else:
            print('The space unavailable or number out of index (1 - 9)!!!')
    return move

def choose_random_move_from_list(board, moves_list):
    #Returns the valid move on the passed list in the passed board
    #Return None if no valid move
    possible_move = []
    for i in moves_list:
        if is_space_free(board, i):
            possible_move.append(i)
    if len(possible_move) != 0:
        return random.choice(possible_move)
    else:
        return None

def get_computer_move(board, computer_letter):
    #Given the board and the computer's letter, determire where to move and return that move
    if computer_letter == 'X':
        player_letter = 'O'
    else:
        player_letter = 'X'

    #Here is our algorithm for our Tic Toc Toe AI
    #Firs, check if we can win on the next move
    for i in range(1, 10):
        copy_board = get_board_copy(board)
        if is_space_free(copy_board, i):
            make_move(copy_board, computer_letter, i)
            if is_winner(copy_board, computer_letter):
                return i
    #check if player can win on their next move and block them
    for i in range(1, 10):
        copy_board = get_board_copy(board)
        if is_space_free(copy_board, i):
            make_move(copy_board, player_letter, i)
            if is_winner(copy_board, player_letter):
                return i
    #Try to take one of the corners, if they are free
    move = choose_random_move_from_list(board, [1, 3, 7, 9])
    if move != None:
        return move
    #Try to take the center, if it free
    if is_space_free(board, 5):
        return 5
    #Move on one of the sides
    return choose_random_move_from_list(board, [2, 4, 6, 8])

def is_board_full(board):
    #Return True if every space on the board are taken, otherwise return False
    for i in range(1, 10):
        if is_space_free(board, i):
            return False
    return True

while True:
    print('WELCOM TO TIC-TOC-TOE!!!')
    #reset the board
    board = [' '] * 10
    player_letter, computer_letter = input_player_letter()
    turn = who_go_first()
    print(f'The {turn} will go first!!!')
    play_on = True
    
    while play_on:
        if turn == 'player':
            #Player's turn
            draw_board(board)
            move = get_player_move(board)
            make_move(board, player_letter, move)

            if is_winner(board, player_letter):
                draw_board(board)
                print('Hooray! You has won the game!!!')
                play_on = False
            else:
                if is_board_full(board):
                    draw_board(board)
                    print('The game is a tie!!!')
                    break
                else:
                    turn = 'computer'

        else:
            #computer's turn
            move = get_computer_move(board, computer_letter)
            make_move(board, computer_letter, move)

            if is_winner(board, computer_letter):
                draw_board(board)
                print('The computer has beaten you! You lose!!!')
                play_on = False
            else:
                if is_board_full(board):
                    draw_board(board)
                    print('The game is a tie!!!')
                    break
                else:
                    turn = 'player'
    if not play_again():
        break

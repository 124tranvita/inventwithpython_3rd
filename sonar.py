import random
import sys

#drawing the game board
def draw_board(board):
    '''
    Drawing the X-coordinates along the top
    '''
    #Draw the data structure
    #First line +++ + +++++++++ + 9 (hLine + hline(''*9) + str(i)) - (+){3} + (+){9} + str(i)
    h_line = '   '
    for i in range(1, 6):
        h_line += (' ' * 9) + str(i)
    print(h_line)
    #Second line +++ + 123456....4950
    print('  ' + ('0123456789' * 6))
    print()
    #Third line 
    '''
    Drawing the Rows of the ocean
    '''
    for i in range(15):
        if i < 10:
            extra_space = ' '
        else:
            extra_space = ''
        print(f'{extra_space}{i} {get_row(board, i)} {i}')
    '''
    Drawing the X-coordinates along the bottom
    '''
    #Print the number across the bottom (which is reverse with the top)
    print()
    print('   ' + ('0123456789' * 6))
    print(h_line)

#Getting the state of a row in the ocean
def get_row(board, row):
    #Return the string from the board data structure at a certain row
    board_row = ''
    for i in range(60):
        board_row += board[i][row]
    
    return board_row

#Creating a new game board
def get_new_board():
    #Create a new [60x15] board structure
    board = []
    for x in range(60): #The main list is the list of 60 lists
        board.append([])
        for y in range(15): #Each list in the main list have 15-single characters string
            #Use different characters for the ocean to make it more readable
            if random.randint(0, 1) == 0:
                board[x].append('~')
            else:
                board[x].append('`')

    return board

#Creating a random treasure chest
def get_random_chests(num_chests):
    #Create a list chest data structure (two-item lists of x, y in coordinates)
    chests = []
    for i in range(num_chests):
        chests.append([random.randint(0, 59), random.randint(0, 14)])
    
    return chests

#Determining if the move is Valid
def is_valid_move(x, y):
    #Return True if coordinates is in the board. Otherwise return False
    return x >= 0 and x <= 59 and y >= 0 and y <= 14

#Placing a move on the Board
def make_move(board, chests, x, y):
    '''
    Change the board data structure with a sonar device character. Remove treasure chests
    from the chests list as they are found. Return False if this is an invalid move.
    Otherwise, return the string of the result of this move.
    '''
    if not is_valid_move(x, y):
        return False
    
    smallest_distance = 100 #any chest will be closer than 100
    for cx, cy in chests:
        if abs(cx - x) > abs(cy - y):
            distance = abs(cx -x)
        else:
            distance = abs(cy - y)
            
        if distance < smallest_distance: #we want the closest treaseure
            smallest_distance = distance
        
    if smallest_distance == 0:
        #x,y is direct on the treasure chest
        chests.remove([x, y])
        return 'You have found a suken treasure chest!!!'
    else:
        if smallest_distance < 10:
            board[x][y] = str(smallest_distance)
            return 'Treasure detected at a distance of {} from the sonar device.'.format(smallest_distance)
        else:
            board[x][y] = '0'
            return 'Sonar did not detect anything. All treasure chests out of range!!!'

#Getting the player move
def enter_player_move():
    #let the player type in their move. Return the a two-item list of int x and y coordinates
    print('Where do you want to drop the next sonar device? (0-59) (0-14) (or type quit to exit)')
    while True:
        move = input()
        if move.lower() == 'quit':
            print('Thanks for playing!!!')
            sys.exit()
            
        move = move.split()
        if len(move) == 2 and move[0].isdigit() and move[1].isdigit() and is_valid_move(int(move[0]), int(move[1])):
            return [int(move[0]), int(move[1])]
        print('Enter a number from 0 to 59, a space, then a number from 0 to 14.')            

#Asking player to play again
def play_again():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')
                    
#Printing the game instructions for player
def show_instrutions():
    print('''Instructions:
    You are the captain of the Simon, a treasure-hunting ship. Your current
    mission is to find the three sunken treasure chests that are lurking in the part
    of the ocean you are in and collect them.

    To play, enter the coordinates of the point in the ocean you wish to drop
    a sonar device. The sonar can find out how far away the closest chest is to
    it.

    For example, the d below marks where the device was dropped, and the 2's represent distances of 2 away from the device.
    The 4's represent distances of 4 away from the device. 

    444444444
    4       4
    4 22222 4
    4 2 2 2 4
    4 2 d 2 4
    4 2 2 2 4
    4 22222 4
    4       4
    444444444

    Press enter to continue...''')
    input()
    print('''For example, here is a treasure chest (the c) located a
    distance of 2 away from the sonar device (the d):

    22222
    c   2
    2 d 2
    2   2
    22222

    The point where the device was dropped will be marked with a 2.

    The treasure chests don’t move around. Sonar devices can detect treasure
    chests up to a distance of 9. If all chests are out of range, the point
    will be marked with O

    If a device is directly dropped on a treasure chest, you have discovered
    the location of the chest, and it will be collected. The sonar device will
    remain there.

    When you collect a chest, all sonar devices will update to locate the next
    closest sunken treasure chest.
    Press enter to continue...''')
    input()
    print()
                    
#The start of the game
print('S O N A R')
print()
print('Would you like to view instructions? (yes or no)')
if input().lower().startswith('y'):
    show_instrutions()

while True:
    #game setup
    sonar_devices = 16
    board = get_new_board()
    chests = get_random_chests(3)
    draw_board(board)
    previous_move = []

    # displaying the game status for the player
    while sonar_devices > 0:
        # Start of a turn
        # show sonar devices, chests status
        if sonar_devices > 1: extra_s_sonar = 's'
        else: extra_s_sonar = ''
        if len(chests) > 1: extra_s_chest = 's'
        else: extra_s_chest = ''
        print(f'You have {sonar_devices} sonar device{extra_s_sonar} left. {len(chests)} treasure chest{extra_s_chest} remain.')
        print(f'Test {chests}')
        #Getting the player move
        x, y = enter_player_move()
        previous_move.append([x, y]) # we must track all moves so that sonar device an updated
        move_result = make_move(board, chests, x, y)
        if move_result == False:
            continue
        #Finding a sukan treasure chests
        else:
            if move_result == 'You have found a suken treasure chest!!!':
                # update all the sonar devices currently on map
                for x, y in previous_move:
                    make_move(board, chests, x, y)
            draw_board(board)
            print(move_result)

            # check if the player has won
            if len(chests) == 0:
                print('You have found all the sunken treasure chests! Congratulations and good game!')
                break
            sonar_devices -= 1

    # check if the player has lost
    if sonar_devices == 0:
        print('We\'ve run out of sonar devices! Now we have to turn the ship around and head')
        print('for home with treasure chests still out there! Game over.')
        print(' The remaining chests were here:')
        for x, y in chests:
            print(' %s, %s' % (x, y))
     
    #ask player play again
    if not play_again():
        sys.exit()

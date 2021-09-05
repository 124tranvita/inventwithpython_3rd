import random

def get_secret_number(num_digits):
    #Return a string that is num_digits long, make up of unique random digits
    number = list(range(10))
    random.shuffle(number)
    
    secret_number = ''
    for i in range(num_digits):
        secret_number += str(number[i])
    
    return secret_number

def get_clues(guess, secret_num):
    #Return a string with the pico, fermi, bagels clues to the user
    if guess == secret_num:
        return 'You got it!!!'

    clue = []
    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
            clue.append('Fermi')
        elif guess[i] in secret_num:
            clue.append('Pico')
    
    if len(clue) == 0:
        return 'Bagels'

    clue.sort()

    return ' '.join(clue)

def is_only_digits(num):
    #Return True if num is a string made up only digits. Otherwise return False
    if num == '':
        return False

    for i in num:
        if i not in '1 2 3 4 5 6 7 8 9 0'.split():
            return False
    
    return True

def play_again():
    #This fuction return True if player want to play again or otherwise it return False
    choice = input('Play again? Y or N ')
    if choice.lower().startswith('y'):
        return True


NUMDIGITS = 3
MAXGUESS = 10

print('I am thinking of a {}-digit number. Try to guess what it is.'.format(NUMDIGITS))
print('Here are some clues:')
print('When I say:    That means:')
print(' Pico           One digit is correct but in the wrong position.')
print(' Fermi          One digit is correct and in the right position.')
print(' Bagels         No digit is correct.')

while True:
    secret_num = get_secret_number(NUMDIGITS)

    print('I have thought up a number. You have {} guesses to get it.'.format(MAXGUESS))

    num_guesses = 1

    while num_guesses <= MAXGUESS:
        #getting player guess
        guess = ''
        while len(guess) != NUMDIGITS or not is_only_digits(guess):
            print('Guess #{}: '.format(num_guesses))
            guess = input()

        #getting the player's clues for player's guess
        clue = get_clues(guess, secret_num)
        print(clue)
        num_guesses += 1

        #checking if the player won or lost!
        if guess == secret_num:
            break
        if num_guesses > MAXGUESS:
            print('You ran out of guesses. The answer is {}'.format(secret_num))
        
    #ask player to play again
    if not play_again():
        break

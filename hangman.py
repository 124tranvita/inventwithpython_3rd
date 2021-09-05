import random

HANGMANPICS = ['''
    +---+
    |   |
        |
        |
        |
        |
=========''',
'''
    +---+
    |   |
    o   |
        |
        |
        |
=========''',
'''
    +---+
    |   |
    o   |
    |   |
        |
        |
=========''',
'''
    +---+
    |   |
    o   |
   /|   |
        |
        |
=========''',
'''
    +---+
    |   |
    o   |
   /|\  |
        |
        |
=========''',
'''
    +---+
    |   |
    o   |
   /|\  |
   /    |
        |
=========''',
'''
    +---+
    |   |
    o   |
   /|\  |
   / \  |
        |
=========''']

words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()

#get secret word
def get_secret_word(words):
    return words[random.randint(0, len(words) - 1)]

#print the game board
def display_game_board(secret_word, missed_letter, correct_letter):
    #set the blank string
    blank = '_' * len(secret_word)

    #print the hangman pics
    print(HANGMANPICS[len(missed_letter)])

    #print all missed letter
    print('Missed letter: {}'.format(missed_letter))

    #put correct letter into blank string and print the current blank string
    if correct_letter != '':
        for i in range(len(secret_word)):
            if secret_word[i] in correct_letter:
                blank = blank[:i] + secret_word[i] + blank[i + 1:]
    print(blank)

#ask player to guess the letter
def player_guess():
    while True:
        choice = input('Guess letter: ').lower()

        if len(choice) != 1:
            print('Please enter only one letter at time!!!')
        elif choice not in'abcdefghijklmnopqrstuvwxyz':
            print('Please enter alphabet letter only!!!')
        else:
            break
    return choice

while True:
    #init value
    correct_letter = ''
    missed_letter = ''
    #come up with a secret word
    secret_word = get_secret_word(words)
    play_on = True

    #begin game
    while play_on:
        
        #show the board and blank to player
        display_game_board(secret_word, missed_letter, correct_letter)

        #ask player to guess letter
        guess_letter = player_guess()
        
        #if guessed letter is in secret word
        while guess_letter in secret_word:
            #if guessed letter is in serect word but already guess
            if guess_letter in correct_letter:
                print('You have already guessed that letter. Choose again.')
                break
            else:
                correct_letter += guess_letter
                break
        #if guessed letter is not in secret word
        else:
            missed_letter += guess_letter

        #if player has guessed all letter and win
        found_all_letters = True
        for letter in secret_word:
            if letter not in correct_letter:
                found_all_letters = False
         
        if found_all_letters:
            print('Yes! The secret word is "{}"! You have won!'.format(secret_word))
            play_on = False
            break

        #if player has run out of body part and lose
        if len(missed_letter) == len(HANGMANPICS) - 1:
            print(HANGMANPICS[len(missed_letter)])
            print('You lose!!! The Secret Word is "{}"'.format(secret_word))
            play_on = False
            break

    #ask user to play again
    choice = input('Play again? Y or N ')
    if choice.lower().startswith('y'):
        continue
    else:
        print('Thank for playing game!!!')
        break

    
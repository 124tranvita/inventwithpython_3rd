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
=========''',
'''
    +---+
    |   |
   [o   |
   /|\  |
   / \  |
        |
=========''',
'''
    +---+
    |   |
   [o]  |
   /|\  |
   / \  |
        |
=========''']

words = {'Colors':'red orange yellow green blue indigo violet white black brown'.split(),
'Shapes':'square triangle rectangle circle ellipse rhombus trapezoid chevron pentagon hexagon septagon octagon'.split(),
'Fruits':'apple orange lemon lime pear watermelon grape grapefruit cherry banana cantaloupe mango strawberry tomato'.split(),
'Animals':'bat bear beaver cat cougar crab deer dog donkey duck eagle fish frog goat leech lion lizard monkey moose mouse otter owl panda python rabbit rat shark sheep skunk squid tiger turkey turtle weasel whale wolf wombat zebra'.split()}
#get secret word
def get_secret_word(words):
    #select random key in words dictionary
    word_key = random.choice(list(words.keys()))
    #select random word in word key set
    word_index = random.choice(words[word_key])
    #return the set of key and word
    return (word_key, word_index)

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
    #come up with the secret word
    secret_set, secret_word = get_secret_word(words)
    play_on = True

    #begin game
    while play_on:
        #show the board and blank to player
        display_game_board(secret_word, missed_letter, correct_letter)

        print('The secret word is in the set: {}'.format(secret_set))
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
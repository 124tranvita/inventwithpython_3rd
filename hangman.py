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

#come up with a secret word
def get_secret_word(words):
    return words[random.randint(0, len(words)- 1)]

#show the board and the blank to the player
def show_game_board(hangmanpics, missed_letter, correct_letter, secret_word):
    #init the blank string base on len of secret word
    blank = '_' * len(secret_word)

    #print the hangman part pic
    print(hangmanpics[len(missed_letter)])

    #print missed guess
    print('Missed letter: {}'.format(missed_letter))

    #put correct letter into blank
    if correct_letter != '':
        for i in range(len(secret_word)):
            if secret_word[i] in correct_letter:
                blank = blank[:i] + secret_word[i] + blank[i+1:]

    #return the guess letter string
    print(blank)

#ask player guess
def player_guess():
    while True:
        player_guess = input('Guess letter: ').lower()

        if len(player_guess) > 1:
            print('Please enter one letter only!!!')
        else:
            break
    return player_guess.lower()

#check if letter is in secret word
def check_letter(guess_letter, secret_word):
    if guess_letter in secret_word:
        return True

#check winner
def found_all_word(correct_letter, secret_word):
    for i in range(len(secret_word)):
        if secret_word[i] not in correct_letter:
            return False
    else:
        return True


#Play game
while True:
    #come up with a secret word
    secret_word = get_secret_word(words)

    #init missed guess and correct guess
    missed_letter = ''
    correct_letter = ''

    play_on = True
    while play_on:
        #show the board and blank to player
        show_game_board(HANGMANPICS, missed_letter, correct_letter, secret_word)

        if found_all_word(correct_letter, secret_word):
            print('Yes! The secret word is "{}"! You have won!'.format(secret_word))
            play_on = False
            break
        elif len(missed_letter) == 6:
            print('You lose!!! The Secret Word is "{}"'.format(secret_word))
            play_on = False
            break

        #ask player to guess a letter
        while True:
            guess = player_guess()

            if guess in correct_letter:
                print('You have already guessed that letter. Choose again.')
            elif check_letter(guess, secret_word):
                correct_letter += guess
                break
            else:
                missed_letter += guess
                break
        
    #ask player if they want to play again or not
    choice = input('Play again? Y or N')
    if choice[0].lower() == 'y':
        continue
    else:
        print('Thank for playing game!!!')
        break
    
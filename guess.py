import random

while True:
    #welcom
    print('WELCOM TO GUESS NUMBER GAME!!!')
    print('You have 10 tries to guess the correct random number between 1 and 100!!!')
    
    #initialize random number between 1 and 100
    rand_num = random.randint(1, 100)
    
    #ask player name
    player_name = input('Hello! What us your name?: ')
    print('Well, {}, I am thinking of number between 1 and 100'.format(player_name))

    #set the get time
    guess_times = 0

    while guess_times < 10:
        #ask user to guess the random number
        try:
            guess_num = int(input('Take guess: '))
        except:
            print('Please input number only!!!')
            continue

        #check if guess number
        if guess_num == rand_num:
            print('Good job {}! You have guessed my number in {} guesses'.format(player_name, guess_times))
            break
        elif guess_num <= rand_num:
            print('Your guess is too slow!!!')
        else:
            print('Your guess is too high!!!')

        #print the guess times that use have used 
        guess_times += 1   
        print('\nYou have guessed {} times!!!'.format(guess_times)) 
        
    else:
        print('\nNope. My number I was thinking of is {}'.format(rand_num))
        
    #ask user to continue or not if they game over   
    choice = input('Are you want to play again? Y or N')

    if choice[0].lower() == 'y':
        guess_times = 0
        continue
    else:
        print("Thank you for playing!!!")
        break
    

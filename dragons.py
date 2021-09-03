import random
import time

#display the intro of the game
def displayIntro():
    print('You are in a land full of dragons. In front of you,')
    print('you see two caves. In one cave, the dragon is friendly')
    print('and will share his treasure with you. The other dragon')
    print('is greedy and hungry, and will eat you on sight.')
    print()

#ask player to choose what cave will be go into
def chooseCave():
    choice = 0
    while choice not in [1, 2]:
        try:
            choice = int(input('which cave will you go into? (1 or 2) '))
        except:
            print('Character not accepted!!!')
        else:
            print('Please select only 1 or 2!!!')

    return choice

#check the dragon in this cave is friendly or not by random.randint()
def checkCave(chosenCave):
    print('You approach the cave...')
    time.sleep(2) 
    print('It is dark and spooky...')
    time.sleep(2) 
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    time.sleep(2) 

    friendlyDragon = random.randint(1,2)

    if chosenCave == friendlyDragon:
        print('Gives you his treasure!')
    else:
        print('Gobbles you down in one bite')

while True:
    displayIntro()

    caveNumber = chooseCave()

    checkCave(caveNumber)

    #ask player if they want to play again or not
    choice = input('Play again? Y or N')
    if choice[0].lower() == 'y':
        continue
    else:
        print('Thank for playing game!!!')
        break
    


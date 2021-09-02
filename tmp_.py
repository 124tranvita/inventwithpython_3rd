print('Your have used all you guess!!!')
choice = input('Are you want to play again? Y or N')

if choice[0].lower() == 'y':
    print("Y!!!")
elif choice[0].lower() == 'n':
    print("N!!!")
else:
    print("Please enter only Y or N!!!")

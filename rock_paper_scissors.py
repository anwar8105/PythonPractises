# Attempt to implement of rock, paper and scissors game

from random import choice
from sys import exit


def getInput():
    def ai_Choice():
        rps = ['rock', 'paper', 'scissors']
        return choice(rps)

    # Tracking game status
    user_winning = 0
    ai_winning = 0
    ties = 0

    gameOn = True

    while gameOn:
        try:
            # lowering every character user has typed and striping trailing spaces
            user_choice = input('Enter your choice r for rock, p for paper or s for scissors : ').lower().strip()
        except KeyboardInterrupt:  # if keyboard interrupted, display game status and exit
            print('Game Status')
            print(f"\n{'+' * 25}")
            print(f"User Winning(s) : {user_winning}\nAi Winnings(s) : {ai_winning}\nTie(s) : {ties}")
            print(f"{'+' * 25}\n")
            exit()
        else:
            if not user_choice in ['r', 'p', 's', 'q', 'quit']:
                print('numbers, special characters and other character aren\'t allowed')
                continue  # prevents going below code execution and starts again

            ai_choice = ai_Choice()
            if user_choice == 'q' or user_choice == 'quit':
                print('Game Status')
                print(f"\n{'+' * 25}")
                print(f"User Winning(s) : {user_winning}\nAi Winnings(s) : {ai_winning}\nTie(s) : {ties}")
                print(f"{'+' * 25}\n")
                exit()

            # replacing intials with full names
            if user_choice == 'r':
                user_choice = 'rock'
            elif user_choice == 'p':
                user_choice = 'paper'
            elif user_choice == 's':
                user_choice = 'scissors'

            # check winnings, losses and ties
            if user_choice == ai_choice:
                ties += 1
                print('Tied!!!')
            elif (user_choice == 'rock' and ai_choice == 'scissors') or (user_choice == 'scissors' and ai_choice == 'paper') or (user_choice == 'paper' and ai_choice == 'rock'):
                user_winning += 1
                print('User Won!!!')
            else:
                ai_winning += 1
                print('Ai Won!!!')


print('Welcome to Rock, Paper and Scissors Game')
print('Have Fun with AI player\n')
print('Enter \'q\', \'quit\' or \'CTRL-C\' anytime if you want to quit\n')
getInput()

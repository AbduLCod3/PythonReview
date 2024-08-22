import sys
import random
from enum import Enum 
print("")


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS =  3

play_again = True

while play_again:

    # print(RPS(2))
    # print(RPS.ROCK)
    # print(RPS['ROCK'])
    # print(RPS.ROCK.value)
    # sys.exit

    print("")
    player_choice = input('Enter... \n1 for Rock, \n2 for Paper, or \n3 for Scissors: \n\n')
    player = int(player_choice)

    if player < 1 or player > 3:
        sys.exit('Please Enter 1, 2, or 3.')

    computer_choice = random.choice("123");
    computer = int(computer_choice)
    print("")
    print("You Chose " + str(RPS(player)).replace('RPS.',"") + ".\n")
    print("Python Chose " + str(RPS(computer)).replace('RPS.', "") + ".\n")
    print("")


    if player == 1 and computer == 3:
        print("🎉 You Win!")
    elif player == 2 and computer == 1:
        print("🎉 You Win!")
    elif player == 3 and computer == 2:
        print("🎉 You Win!")
    elif player == computer:
        print("😎 Tie Game!")
    else:
        print("🐍 Python Wins!")

    play_again = input('\nWant To Play Again?\nY for Yes or \nQ to Quit \n\n')

    if play_again.lower() =="y":
        continue
    else:
        print("\n🎉🎉🎉🎉🎉")
        print('Thanks for playing!\n')
        play_again = False

sys.exit("Bye! 👋👋\n\n")








print("")

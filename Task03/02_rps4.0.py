import sys
import random
from enum import Enum 

# Global variables
game_count = 0

print("")

def play_rps():

    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS =  3

    # play_again = True

    # while play_again:

    # print(RPS(2))
    # print(RPS.ROCK)
    # print(RPS['ROCK'])
    # print(RPS.ROCK.value)
    # sys.exit

    print("")
    player_choice = input('Enter... \n1 for Rock, \n2 for Paper, or \n3 for Scissors: \n\n')
    # Let's check if the player enter the correct value 
    if player_choice not in ['1', '2', '3']:
        # Handle it by priting the following message and restarting the game
        print('You must enter 1, 2, or 3.\n')
        return play_rps
    
    player = int(player_choice)

    # if player < 1 or player > 3:
    #     sys.exit('Please Enter 1, 2, or 3.')

    computer_choice = random.choice("123");
    computer = int(computer_choice)
    print("")
    print("You Chose " + str(RPS(player)).replace('RPS.',"") + ".\n")
    print("Python Chose " + str(RPS(computer)).replace('RPS.', "") + ".\n")
    print("")

    def decide_winner(player, computer):

        if player == 1 and computer == 3:
            return "🎉 You Win!"
        elif player == 2 and computer == 1:
            return "🎉 You Win!"
        elif player == 3 and computer == 2:
            return "🎉 You Win!"
        elif player == computer:
            return "😎 Tie Game!"
        else:
            return "🐍 Python Wins!"

    game_result = decide_winner(player, computer)

    print(game_result)
    global game_count
    game_count += 1

    print("\nGame Count: " + str(game_count) )

    print("Want To Play Again")

    while True:
        play_again = input('\nY for Yes or \nQ to Quit \n\n')
        if play_again.lower() not in ['y', 'q']:
            continue
        else:
            break

    if play_again.lower() == 'y':
        return play_rps()
    else:
        
        print("\n🎉🎉🎉🎉🎉")
        print('Thanks for playing!\n')
        sys.exit("Bye! 👋👋\n\n")




play_rps()







print("")

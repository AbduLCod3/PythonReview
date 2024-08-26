import sys
import random
from enum import Enum 


def rps():

    # Global variables
    game_count = 0
    player_wins = 0
    python_wins = 0 

    print("")

    def play_rps():
        nonlocal player_wins
        nonlocal python_wins

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
        ## Use F-strings to format better the following commented codes
        # print("You Chose " + str(RPS(player)).replace('RPS.',"") + ".\n")
        # print("Python Chose " + str(RPS(computer)).replace('RPS.', "") + ".\n")
        print(f"You Chose {str(RPS(player)).replace('RPS.',"").title()}.\n")
        print(f"Python Chose {str(RPS(computer)).replace('RPS.', "").title()}.\n")
        print("")

        def decide_winner(player, computer):
            nonlocal player_wins
            nonlocal python_wins

            if player == 1 and computer == 3:
                player_wins += 1
                return "🎉 You Win!"
            elif player == 2 and computer == 1:
                player_wins += 1
                return "🎉 You Win!"
            elif player == 3 and computer == 2:
                player_wins += 1
                return "🎉 You Win!"
            elif player == computer:
                return "😎 Tie Game!"
            else:
                python_wins += 1
                return "🐍 Python Wins!"

        game_result = decide_winner(player, computer)

        print(game_result)
        nonlocal game_count
        game_count += 1

        ## Use F-strings to format better the following commented codes
        # print("\nGame Count: " + str(game_count) )
        # print("\nPlayer Wins: " + str(player_wins) )
        # print("\nPython Wins: " + str(python_wins) )
        print(f"\nGame Count: {str(game_count)}")
        print(f"\nPlayer Wins {str(player_wins)}")
        print(f"\nPython Wins: {str(python_wins)}")

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

    return play_rps




rock_paper_scissors = rps()

if __name__ == "__main__":
    rock_paper_scissors()





print("")

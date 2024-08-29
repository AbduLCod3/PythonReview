import sys
import random
from enum import Enum 


def rps(name='PlayerOne'):

    # Global variables
    game_count = 0
    player_wins = 0
    python_wins = 0 

    print("")

    def play_rps():
        nonlocal name
        nonlocal player_wins
        nonlocal python_wins

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS =  3

        player_choice = input(
            f'Please enter [1 for Rock], [2 for Paper], or [3 for Scissors]. \n\nYour Choice: ')
        # Let's check if the player enter the correct value 
        if player_choice not in ['1', '2', '3']:
            # Handle it by priting the following message and restarting the game
            print(f'{name}, please enter 1, 2, or 3.\n')
            return play_rps()
        
        player = int(player_choice)

        # if player < 1 or player > 3:
        #     sys.exit('Please Enter 1, 2, or 3.')

        computer_choice = random.choice("123");
        computer = int(computer_choice)
        print("")
        ## Use F-strings to format better the following commented codes
        # print("You Chose " + str(RPS(player)).replace('RPS.',"") + ".\n")
        # print("Python Chose " + str(RPS(computer)).replace('RPS.', "") + ".\n")
        print(f"{name} Chose {str(RPS(player)).replace('RPS.',"").title()}.\n")
        print(f"Python Chose {str(RPS(computer)).replace('RPS.', "").title()}.\n")
        print("")

        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins
            nonlocal python_wins

            if player == 1 and computer == 3:
                player_wins += 1
                return f"{name}🎉 You Win!"
            elif player == 2 and computer == 1:
                player_wins += 1
                return f"{name}🎉 You Win!"
            elif player == 3 and computer == 2:
                player_wins += 1
                return f"{name}🎉 You Win!"
            elif player == computer:
                return "😎 Tie Game!"
            else:
                python_wins += 1
                return f"🐍 Python Wins!\n Sorry, {name} ..😢"

        game_result = decide_winner(player, computer)

        print(game_result)
        nonlocal game_count
        game_count += 1

        ## Use F-strings to format better the following commented codes
        # print("\nGame Count: " + str(game_count) )
        # print("\nPlayer Wins: " + str(player_wins) )
        # print("\nPython Wins: " + str(python_wins) )
        print(f"\nGame Count: {game_count}")
        print(f"{name}'s Wins: {player_wins}")
        print(f"Python Wins: {python_wins}\n")

        print(f"Want To Play Again, {name}?\n")

        while True:
            play_again = input('Y for Yes,  or  Q to Quit \n\nYour Decision: ')
            if play_again.lower() not in ['y', 'q']:
                print("\n")
                continue
            else:
                break

        if play_again.lower() == 'y':
            return play_rps()
        else:
            print("")
            # print("\n🎉🎉🎉🎉🎉")
            print('Thanks for playing!\n')
            if __name__ == "__main__":
                sys.exit(f"Bye {name}! 👋👋\n\n")
            else:
                return

    return play_rps



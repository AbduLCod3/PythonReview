import sys
import random


def guess_number(name='PlayerOne'):
    # Global variables
    game_count = 0
    player_wins = 0
    
    def play_guess_number():
        nonlocal name
        nonlocal player_wins

        # Get User's Guess
        user_guess = input(f'\nGuess Which Number I am thinking: 1, 2, or 3:\n')
        # Check if user input is valid (is it one (1, 2, or 3))
        # If user input is not correct
        if user_guess not in ['1', '2', '3']:
            # Restart the game, and ask the user to input the correct choices
            print(f'{name}, Please Enter 1, 2, or 3:\n')
            return play_guess_number()
        
        # Annotate user input with int data type
        player_guess = int(user_guess)
        print(f'{name}, You Chose the Number {user_guess}')

        def guess_result(player_guess):
            nonlocal name
            nonlocal player_wins
          
            # Generate random # and annotated with int data type
            random_num = int(random.choice('123'))

            # Check if player guessed the number correctly
            if player_guess == random_num:
                # Add to player wins
                player_wins += 1
                return f'And I, {name}, was thinking about the same number {random_num}\n{name}, You Win!! 🏆'
            else:
                return f'And I, {name}, was thinking about the number {random_num}\nSorry, {name}, Better Luck Next Time. 😉' 
            
        game_result = guess_result(player_guess)
        print(game_result)
        nonlocal game_count
        game_count +=1

        print('\n')
        print(f"*****  GAME STATS!  *****") 
        print(f"*  Game Count: {game_count}        *")
        print(f"*  {name}'s Wins: {player_wins}      *")
        print(f"*  {name}'s Winning Rate: {(player_wins/game_count)*100 : .2f}% * ")
        print(f"*****  END OF GAME STATS!  *****") 
        print('\n')

        # Ask if user wants to play again
        print(f"Want To Play Again, {name}?")

        while True:
            play_again = input('Y for Yes,  or  Q to Quit \n\nYour Decision: ')
            if play_again.lower() not in ['y', 'q']:
                print("\n")
                continue
            else:
                break


        if play_again.lower() == 'y':
            return play_guess_number()
        else:
            print("")
            # print("\n🎉🎉🎉🎉🎉")
            print('Thanks for playing!\n')
            if __name__ == "__main__":
                sys.exit(f"Bye {name}! 👋👋\n\n")
            else:
                return
            
    return play_guess_number()





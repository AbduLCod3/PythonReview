import sys
import guessMyNumber
import RPSv6

def play_arcade(name='PlayerOne'):
    welcome_back = False

    while True:
        if welcome_back ==  True:
            print(f"\n{name}, welcome back to the Arcade menu.\n")
        # Ask User Which game he wants to play 
        
        user_choice = input(f'Please choose a game: \n1 = Rock Paper Scicssors. \n2 = Guess My Number. \n\nOr Press "X" to exit the Arcade.\n\nYour Game Choice: ')

        # Check if user input is valid (is it 1, 2, or x)
        # If user input is not correct
        if user_choice not in ['1', '2', 'x']:
            # Restart the game, and ask the user to input the correct choices
            print(f'{name}, Please Enter 1, 2, or x:\n')
            return play_arcade(name)
        
        welcome_back = True


        if user_choice == '1':
            print(f'\nHi {name}, You Chose to Play the Game: Rock, Paper, Scicssors.')
            rock_paper_scissors = RPSv6.rps(name)
            rock_paper_scissors()
        
        elif user_choice == '2':
            print(f'\nHi {name}, You Chose to Play the Game: Guess My Number.')
            guess_number_game = guessMyNumber.guess_number(name)
            guess_number_game()
        else:
            print("")
            # print("\n🎉🎉🎉🎉🎉")
            print('You Chose Not To Play.\n')
            sys.exit(f"Bye {name}! 👋👋\n\n")



if __name__ == "__main__":
    # Command line option and argumnet parsing library
    import argparse


    parser = argparse.ArgumentParser(
        description='Provides a personalize game experience agreenment'
        )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person playing the game."
    )
   

    args = parser.parse_args()

    print(f'\n🕹🕹🕹   Hi {args.name}, Welcome to the Arcade! 🕹🕹🕹:\n')
    
    play_arcade(args.name)
   



    
    
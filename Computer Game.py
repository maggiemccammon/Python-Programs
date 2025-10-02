# Function of program is to execute a one-player dice game agaist the computer where both player and
#   computer start with 50 points. Whoever has the most amount of points when the game ends is the winner.
## Whenever the dice is rolled for both player and computer the higher number wins and that number is
##  then subtracted from the losers total amount.

import random

# Global constants used in the program.
DICE_MIN_NUM = 1
DICE_MAX_NUM = 6
START_SCORE = 50
MIN_ROUNDS = 1
MAX_ROUNDS = 10

# Defines the main program(function).
def main():
    # Stating when the main greeting is displayed.
    display_greeting()

    #//*** 
    #//*** This while-loop controls how many games are played.
    #//*** Formulate the while-loop condition to play any number of games at the player’s discretion.
    #//***
    #//*** Hint: You will write code that is placed at the end of function play_game that asks the
    #//***    player if they would like to play another game after a game finishes. The player's
    #//***    response will be the return value of the call to function play_game and will be used
    #//***    in this while-loop condition.
    #//***

    # While-loop simulates how many rounds are within a game, and allows for multiple to be played.
    play_again = True
    while (play_again):
        rounds = int(input(f'\nEnter the number of rounds in the game. ({MIN_ROUNDS}-{MAX_ROUNDS}): ').strip())
        
        #//*** 
        #//*** Prompt the player for the number of rounds to be played in the current game, and
        #//***    store in a variable as an integer. Use the CONSTANTS provided in the prompt text.
        #//***
        #//*** See Sample Runs in Canvas for verbiage.
        #//*** 
        play_again = play_game(rounds)
        
        #//*** 
        #//*** Call function play_game passing the number of rounds as an argument and assign
        #//***    the return value of the call to play_game to a variable as a Boolean.
        #//***         
        #//*** Hint: This Boolean variable will be used to control the termination/continuation
        #//***    of the while-loop.
        #//*** 


    return

# Defining what the main greeting being displayed will say.
def display_greeting():

    print("\nThis is a game of chance where the player and the computer")
    print("\teach roll a single die one time per round.")
    print("\nThe one with the lower number shown on their dice loses")
    print("\tthe number shown on the other's dice.")
    print("\nIf the numbers shown on each dice are the same,")
    print("\tno points are lost by either the player or the computer.")
    print("\nThe goal is to lose the fewest number of points possible")
    print("\tbefore the game ends.")

    return

#//*** 
#//*** Modify the function definition header to receive the number of rounds as a parameter.
#//***

# Defines what will be included in the game and taking into account the amount of rounds being played.
def play_game(rounds):

    #//*** 
    #//*** Initialize a variable for the player’s start score.
    #//***
    #//*** Do not hard-code the start score. Use the CONSTANT provided.
    #//*** 
    player_score = START_SCORE

    #//*** 
    #//*** Initialize a variable for the computer’s start score.
    #//***
    #//*** Do not hard-code the start score. Use the CONSTANT provided.
    #//*** 
    computer_score = START_SCORE

    #//*** 
    #//*** This while-loop controls how many rounds are played in the current game.
    #//*** Formulate the while-loop condition to play the number of rounds.
    #//***
    #//*** Hint: The number of rounds to play is the value stored in the parameter
    #//***    variable passed into this function.
    #//***
    #//*** Hint: You will need a counter variable in this condition.
    #//***
    
    round_num = 1
    
    # While-loop dictates what is displayed during a game and for how many rounds it will be displayed.
    while (round_num <= rounds):

        #//*** 
        #//*** Display the number of the round.
        #//***
        #//*** See Sample Runs in Canvas for verbiage.
        #//*** 
        print(f'\nRound #{round_num}')

        #//*** 
        #//*** Using an input statement, pause the game with a message for the player
        #//***    to roll the dice.
        #//***
        #//*** See Sample Runs in Canvas for verbiage.
        #//*** 
        input('\n\tPress the enter key to roll the player\'s dice.')

        #//*** 
        #//*** Roll the dice for the player by using the randint function to generate
        #//***    a random number from 1 to 6 and store in a variable as an integer.
        #//***
        #//*** Do not hard-code the upper or lower bounds. Use the CONSTANTs provided.
        #//*** 
        player_roll = random.randint(DICE_MIN_NUM, DICE_MAX_NUM)

        #//*** 
        #//*** Display the number on the dice for the player.
        #//***
        #//*** See Sample Runs in Canvas for verbiage.
        #//*** 
        print(f'\n\tThe player rolls a {player_roll}.')
        
        #//*** 
        #//*** Using an input statement, pause the game with a message for the computer
        #//***    to roll the dice.
        #//***
        #//*** See Sample Runs in Canvas for verbiage.
        #//*** 
        input('\n\tPress the enter key to roll the computer\'s dice.')

        #//*** 
        #//*** Roll the dice for the computer by using the randint function to generate
        #//***    a random number from 1 to 6 and store in a variable as an integer.
        #//***
        #//*** Do not hard-code the upper or lower bounds. Use the CONSTANTs provided.
        #//*** 
        computer_roll = random.randint(DICE_MIN_NUM, DICE_MAX_NUM)

        #//*** 
        #//*** Display the number on the dice for the computer.
        #//***
        #//*** See Sample Runs in Canvas for verbiage.
        #//*** 
        print(f'\n\tThe computer rolls a {computer_roll}.')

        #//*** 
        #//*** Use an if-elif-else structure to determine the outcome of the round.
        #//*** Based upon the outcome of the round:
        #//***    1) Update either the player's score or the computer's score.
        #//***    2) Display who lost or if it was a tie.
        #//***
        #//*** See Sample Runs in Canvas for verbiage.
        #//***

        # If-elif-else structure determines how many points are taken off of the losers score, if any.
        if (player_roll < computer_roll):
            player_score -= computer_roll
            print(f'\n\tThe player loses {computer_roll} point(s).')
        elif (player_roll > computer_roll):
            computer_score -= player_roll
            print(f'\n\tThe computer loses {player_roll} point(s).')
        else:
            print('\n\tIt\'s a tie! No points lost.')

        #//*** 
        #//*** Display the player's current score.
        #//***
        #//*** See Sample Runs in Canvas for verbiage.
        #//*** 
        print(f'\n\tThe player currently has a score of {player_score} point(s).')

        #//*** 
        #//*** Display the computer's current score.
        #//***
        #//*** See Sample Runs in Canvas for verbiage.
        #//*** 
        print(f'\tThe computer currently has a score of {computer_score} point(s).')

        #//*** 
        #//*** Don't forget to increment your counter variable.
        #//***
        round_num += 1

    #//*** 
    #//*** Use an if-elif-else structure to determine the outcome of the game.
    #//*** Based upon the outcome of the game, display who won or if it was a tie.
    #//***
    #//*** See Sample Runs in Canvas for verbiage.
    #//***

    # If-elif-else structure determines highest score and displays winner, if any.
    print(f'\nAfter {rounds} round(s), ', end="")
    if (player_score < computer_score):
        print('the player wins!')
    elif (player_score > computer_score):
        print('the computer wins!')
    else:
        print('It\'s a tie')

    #//*** 
    #//*** Display the final score for the player.
    #//***
    #//*** See Sample Runs in Canvas for verbiage.
    #//***
    print(f'\n\tThe player\'s final score is {player_score} point(s).')
    
    #//*** 
    #//*** Display the final score for the computer.
    #//***
    #//*** See Sample Runs in Canvas for verbiage.
    #//***
    print(f'\tThe computer\'s final score is {computer_score} point(s).')

    #//***
    #//*** Prompt the player if they would like to play another game, and store in a
    #//***    variable as a string character. The user will enter "Y" or "y" to play
    #//***    another game, or "N" or "n" to end the program.
    #//***
    #//*** See Sample Runs in Canvas for verbiage.
    #//***
    play_again_input = input('\nWould you like to play another game? (Y/y or N/n): ').strip().lower()

    #//***
    #//*** Use an if-else structure to determine if another game is to be played.
    #//*** The test of the user's response must be case-insensitive. Meaning, they
    #//***    can enter "Y" or "y" for another game to begin, or "N" or "n" to end
    #//***    the program.
    #//*** 
    #//*** Based upon the player's response, set a Boolean variable to either
    #//***    True or False.
    #//***

    # If-else structure determines if the player would like to play again.
    if (play_again_input == 'y' or play_again_input == 'Y'):
        play_again = True
    else:
        play_again = False

    #//***
    #//*** Use this return statement to pass back the value of the "play another game"
    #//***    Boolean variable.
    #//***
    return play_again

# Displays entire program based on defined main from the top. 
main()

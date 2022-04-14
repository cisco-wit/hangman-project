def drawHangman(missedLetters, correctLetters, secretWord):
    """Draw the current state of the hangman, along with the missed and correctly-guessed letters of the secret word."""
    
    # Show the incorrectly guessed letters:


    # Display the blanks for the secret word (one blank per letter):

    
    # Replace blanks with correctly guessed letters:
    
    
    # Show the secret word with spaces in between each letter:

    return



def getPlayerGuess(alreadyGuessed):
    """Returns the letter the player entered. This function makes sure the player entered a single letter they haven't guessed before."""
    # Keep asking until the player enters a valid letter.
    print('Guess a letter.')


def main():
    print('Hangman, by Al Sweigart al@inventwithpython.com')
    
    # Setup variables for a new game:



    # Check if the player has won:




    # The player has guessed incorrectly:




    # Check if player has guessed too many times and lost. (The # "- 1" is because we don't count the empty gallows in
    # HANGMAN_PICS.)



# If this program was run (instead of imported), run the game: 
if __name__ == '__main__':
	try: 
	    main()
	except KeyboardInterrupt:
	    sys.exit() # When Ctrl-C is pressed, end the program.

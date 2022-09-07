#!/usr/bin/python3

## libraries
from libs import *

## global variable
FILE_PATH = "database/words_database.txt"
HIDDEN_WORD = None 
HIDDEN_PROGRESS = None
AMMOUNT_GUESS = 10 # You can change this to your licking
WRONG_CHAR = []
ROUND_RIGHT_CHAR = None

if __name__ == "__main__":
    info_header()
    
    HIDDEN_WORD = choose_random_words(FILE_PATH).lower() # make hidden_word lower
   
    HIDDEN_PROGRESS = create_hidden_word_progress(HIDDEN_WORD)
    try:
        for i in range(AMMOUNT_GUESS + 1):
            show_game_stat( AMMOUNT_GUESS - i, WRONG_CHAR)

            show_hidden_progress(ROUND_RIGHT_CHAR ,HIDDEN_WORD, HIDDEN_PROGRESS)
        
            if (AMMOUNT_GUESS - i ) == 0:
                print("\n\t[ATTENTION] You have 1 guess left, use it wisely".upper())

            user_input = get_user_guess()

            if user_input[0] == 'char':
                check_char = parse_guess_letter(user_input, HIDDEN_WORD, WRONG_CHAR)

                if check_char[0] == 'right_char':
                    ROUND_RIGHT_CHAR = check_char[1][1]
        
            if user_input[0] == 'word':
                word_to_check = parse_guess_words(user_input, HIDDEN_WORD)
            
                if word_to_check == 'good_word':
                    good_word() # replace by something else
                    show_hidden_word(HIDDEN_WORD) 
                    exit()

                if word_to_check == 'wrong_word':
                    if not ((AMMOUNT_GUESS - i) == 0):
                        bad_word()

        no_guess_left(HIDDEN_WORD)
    
    except:
        fatal()


# 
from random import randint as random_nb

#

def info_header():
    print("Version: 0.1\nWelcome to hangman (the terminal version)\nHere are the rule\n[+] You have 5 chances to get the hidden word right\n[+] You can either guess a entire word or a single character\n\t\t-=-=-=-=-= Good Luck =-=-=-=-=-\n\n");

def fatal():
    print("\n[FATAL] a fatal error occur.\tThe program will close shortly")
    exit()

def choose_random_words(FILE_PATH):
    with open(FILE_PATH, 'r') as file:
        words_list = file.readlines()
        return words_list[ random_nb(0, len(words_list)) ]
    return

def show_game_stat(guess_left, list_wrong_letter):
    print(f"\nYou have {guess_left} guesses left\t\tWrong letter: {list_wrong_letter}")
    return

# to implement
def create_hidden_word_progress(hidden_word):
    return [ f"{item} " for item in range(len(hidden_word) - 1) ]

def show_hidden_progress(right_char, hidden_word, hidden_progress):
    for index in range(len(hidden_word)):
        if [ *hidden_word][index] == right_char:
            hidden_progress[index] = right_char

    print(f"Here you progress: { ''.join(hidden_progress) }")
    return hidden_progress




def get_user_guess():
    user_guess = input("\n[+] Enter your guess =>  ")
    if len(user_guess) == 1:
        # enter a character
        return ('char', user_guess.lower()) # all the answer are lowercase
    else:
        return ('word', user_guess.strip().lower()) # change this # all the answer are lowercase
        # enter a words

# might need to change it
def parse_guess_letter(user_guess, hidden_word, list_wrong_letter):
    if user_guess[1] not in hidden_word:
        list_wrong_letter.append( user_guess[1] )
        print(f"[B] The letter {user_guess[1]} is not in the hidden words")
        return ('wrong_char')
    
    else:
        print(f"[G] The letter {user_guess[1]} is in the hidden words")
        return ('right_char', user_guess)

    return

## <-- focus attention here

def parse_guess_words(user_guess, hidden_word):
    # variable used
    guess = user_guess[1].strip()
    hidden = hidden_word.strip()

    if guess == hidden: # change this
        return ('good_word')
    
    if guess != hidden:
        return ('wrong_word')


def debug_guess_words(user_guess, hidden_word):
    print("\n\n-=-=-=-=-= Begining debug mode =-=-=-=-=-=")
    
    print("[+] the expression is: hidden_word != user_guess[1] \n\n")

    print(f"[+] the user enter: { user_guess[1] }")
    print(f"[+] the datatype of the user is: { type(user_guess[1]) }\n")
    print(f"[+] the hidden_word was: { hidden_word}")
    print(f"[+] the hidden_word datatype was: { type(hidden_word) }\n")
    
    print(f"[+] bool value of hidden_word == user_guess: { hidden_word.strip() == user_guess[1].strip()}")
    
    print("-=-=-=-=-= End of debug mode =-=-=-=-=-=-\n\n")

## 

def no_guess_left(hidden_word):
    print(f"\n\n\t=-=-=-=-=- You have no guesses left, the hidden word was: {hidden_word.strip().upper()} -=-=-=-=-=")

def bad_word():
    print("\n\n\t\t=-=-=-=-=- Darn it, this isn't the good word -=-=-=-=-=")

def good_word():
    print("\n\n\t\t=-=-=-=-=- Congratulation you found the hidden word -=-=-=-=-=")

def show_hidden_word(hidden_word):
    print(f"\n\n\t\t=-=-=-=-=- The hidden word was { hidden_word.upper().strip() } -=-=-=-=-=")

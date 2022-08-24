# 
from random import randint as random_nb

#

def info_header():
    print("Version: 0.1\nWelcome to hangmane (the terminal version)\nHere are the rule\n[+] You have 5 chances to get the hidden word right\n[+] You can either guess a entire word or a single character\n\n\t\t-=-=-=-=-= Good Luck =-=-=-=-=-");

def choose_random_words(FILE_PATH):
    with open(FILE_PATH, 'r') as file:
        words_list = file.readlines()
        return words_list[ random_nb(0, len(words_list)) ]
    return

def show_game_stat(guess_left, list_wrong_letter):
    print(f"You have {guess_left} guesses left\t\tWrong letter: {list_wrong_letter}")
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
    user_guess = input("\nenter your guess =>  ")
    if len(user_guess) == 1:
        # enter a character
        return ('char', user_guess.lower()) # all the answer are lowercase
    else:
        return ('word', user_guess.lower()) # all the answer are lowercase
        # enter a words

# might need to change it
def parse_guess_letter(user_guess, hidden_word, list_wrong_letter):
    if user_guess[1] not in hidden_word:
        list_wrong_letter.append( user_guess[1] )
        print(f"The letter {user_guess[1]} is not in the hidden words")
        return ('wrong_char')
    
    else:
        print(f"The letter {user_guess[1]} is in the hidden words")
        return ('right_char', user_guess)

    return

def parse_guess_words(user_guess, hidden_word):
    if user_guess[1] == hidden_word:
        return True
    
    if user_guess[1] != hidden_word:
        print(f"{ hidden_word } isn't the word, try again")
        return ('wrong_word')

def no_guess_left():
    print("\n\n\t\t=-=-=-=-=- Darn it, you failed you have no guesses left -=-=-=-=-=")

def good_word():
    print("\n\n\t\t=-=-=-=-=- Congratulation you found the hidden word -=-=-=-=-=")

# 
from random import randint as random_nb

#
FILE_PATH = "/home/reader/hangman/src/database/words_database.txt" 

def choose_random_words():
    with open(FILE_PATH, 'r') as file:
        words_list = file.readlines()
        return words_list[ random_nb(0, len(words_list)) ]
    return

def show_game_stat(guess_left, list_wrong_letter):
    print(f"You have [{guess_left}]\t\tWrong letter: {list_wrong_letter}")
    return

# to implement
def create_hidden_word_progress(hidden_word):
    return [ " _ " for item in hidden_word ]

def show_hidden_progress(right_char, hidden_word, hidden_progress):
    for index in range(len(hidden_word)):
        if [ *hidden_word][index] == right_char:
            hidden_progress[index] = right_char
    print( hidden_progress )
    return hidden_progress


def get_user_guess():
    user_guess = input("Enter guess>> ")
    if len(user_guess) == 1:
        # enter a character
        return ('char', user_guess)
    else:
        return ('word', user_guess)
        # enter a words

# might need to change it
def wrong_letter(user_guess, hidden_word, list_wrong_letter):
    if user_guess(1) not in hidden_word:
        list_wrong_letter.append( user_guess(1) )

    return

def wrong_words(user_guess, hidden_word):
    if user_guess == hidden_word:
        return True

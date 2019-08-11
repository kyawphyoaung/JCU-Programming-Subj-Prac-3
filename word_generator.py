"""
CP1404/CP5632 - Practical
Random word generator - based on format of words

Another way to get just consonants would be to use string.ascii_lowercase
(all letters) and remove the vowels.
"""
import random
import sys

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
ALPHABET = "abcdefghijklmnpqrstuvwxyz"
SPECIAL = "#%*"
MENU = """Word Generator V2.0 by Kyaw Phyo Aung
Option 1 : Auto Generate (A)
Option 2 : Manual Input Word Format (M)
Option 3 : Generate with Speical Letters (S)
           Only with % # *
Quit : (Q)
"""
def main():
    option = ask_user()
    while option != "q":
        if option == "a":
            auto()
            print("\n")
        elif option == "m":
            manual()
            print("\n")
        elif option == "s":
            wildcard()
            print("\n")
        print(MENU)
        option = input(">>>")
    print("Thank You!")
    sys.exit()

def ask_user():
    print("\n",MENU)
    user_option = input(">>> ")
    option = user_option.lower()
    return option

def is_valid_format():
    user_format = input("Enter the word format: ")
    word_format = user_format.lower()
    valid = False
    while valid == False:
        if 'c' in word_format or 'v'in word_format:
            valid = True
        else:
            valid = False
            user_format = input("Enter the word format: ")
            word_format = user_format.lower()
    return user_format, valid

def valid_for_special():
    user_format = input("Enter the word format: ")
    word_format = user_format.lower()
    valid = False
    while valid == False:
        if ALPHABET in word_format or SPECIAL in word_format:
            valid = True
        else:
            valid = False
            user_format = input("Enter the word format: ")
            word_format = user_format.lower()
    return user_format, valid

def auto():
    word_format = "ccvcvvc"
    word = ""
    for kind in word_format:
        if kind == "c":
            word += random.choice(CONSONANTS)
        else:
            word += random.choice(VOWELS)
    print(word)

def manual():
    # user_format mean word format from user
    # validating user input
    word_format, valid = is_valid_format()
    if valid == True:
        word = ""
        for kind in word_format:
            if kind == "c":
                word += random.choice(CONSONANTS)
            else:
                word += random.choice(VOWELS)
        print(word)
    else:
        print("Something is Wrong!")

def wildcard():
    # user_format mean word format from user
    # validating user input
    word_format, valid = valid_for_special()
    if valid == True:
        word = ""
        for kind in word_format:
            if kind == "%":
                word += random.choice(CONSONANTS)
            elif kind == "#":
                word += random.choice(VOWELS)
            elif kind == "*":
                word += random.choice(ALPHABET)
            elif kind in ALPHABET:
                word += kind
            else:
                print("Invalid Input")
        print(word)
    else:
        print("Something Wrong!")

main()
"""
CP1404/CP5632 - Practical
Random word generator - based on format of words

Another way to get just consonants would be to use string.ascii_lowercase
(all letters) and remove the vowels.
"""
import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
ALPHABET = "abcdefghijclmnpqrstuvwxyz"

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
    user_format = input("Enter the word format :")
    # validating user input
    lowerword = user_format.lower()
    word = ""
    for kind in lowerword:
        if kind == "c":
            word += random.choice(CONSONANTS)
        else:
            word += random.choice(VOWELS)
    print(word)

def wildcard():
    # user_format mean word format from user
    user_format = input("Enter the word format with special:")
    # validating user input
    lowerword = user_format.lower()
    word = ""
    for kind in lowerword:
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

# auto()
# manual()
wildcard()
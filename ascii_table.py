# ASCII Table
import sys

LOWER_VALUE = 33
UPPER_VALUE = 127
MENU = """ASCII Table Software V2.0 by Kyaw Phyo Aung
Option 1: Character to Number  (C)
Option 2: Number to Character  (N)
Option 3: Customize Columns    (S)
Option 4: Customize Rows       (F)
Quit : (Q)
"""
def main():
    global LOWER_VALUE, UPPER_VALUE
    option = ask_user()
    while option != "q":
        if option == "c":
            chgord()
            option = ask_user()
        elif option == "n":
            chgchr()
            option = ask_user()
        elif option == "s":
            column()
            option = ask_user()
        elif option == "f":
            customize()
            option = ask_user()
        else:
            print("Invalid Input")
            option = ask_user()
    print("Thank You!")
    sys.exit()


def ask_user():
    print("\n",MENU)
    user_option = input(">>> ")
    option = user_option.lower()
    return option


def get_number(lower, upper):
    usernum = input("Enter a number between {} and {}:".format(lower, upper))
    valid = False
    usernum = is_number(usernum, valid, lower, upper)
    while usernum < lower or usernum > upper:
        print("Enter a valid number")
        usernum = input("Enter a number between {} and {}:".format(lower, upper))
        usernum = is_number(usernum, valid, lower, upper)
    return usernum


def is_number(usernum, valid, lower, upper):
    if usernum.isdigit():
        valid = True
        usernum = int(usernum)
    while valid == False:
        print("Enter a valid number")
        usernum = input("Enter a number between {} and {}:".format(lower, upper))
        if usernum.isdigit():
            valid = True
            usernum = int(usernum)
    return usernum


# character to number
def chgord():
    # Request a character from user
    userchar = input("Enter a character:")
    # change from character to UTF-8 integer using ord() funtion
    print("The ASCII code for {} is {}".format(userchar,ord(userchar)))

# number to character
def chgchr():
    # Request a integer from user
    # if user input number is between 33 and 127 , ask again and again
    usernum = get_number(LOWER_VALUE, UPPER_VALUE)

    # change from integer to UTF-8 character using chr() function
    print("The character for {} is {}".format(usernum, chr(usernum)))

# all row, customize column
def column():
    columns = int(input("How many cols :"))
    curr = 0
    for i in range(LOWER_VALUE,UPPER_VALUE+1):
        curr += 1
        print("{:3d} {:1s}".format(i,chr(i)),end='|')
        if curr == columns:
            print()
            curr = 0
        i+=1

# customize row
def customize():
    rows = int(input("How many rows :"))
    for j in range(LOWER_VALUE,rows+34):
        print("{:3d} {:1s}".format(j,chr(j)))
        j+=1

main()
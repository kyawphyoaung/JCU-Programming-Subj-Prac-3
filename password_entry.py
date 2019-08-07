"""
Name : Kyaw Phyo Aung
JCU ID : 13822414
"""
MINIMUM_LENGTH = 6
PASSWORD = "Pythonista"
length_count = 0
user_pwd = input("Enter the password: " )

if len(user_pwd) >= MINIMUM_LENGTH :
    if user_pwd == PASSWORD :
        print("Your enterd password is :")
        while length_count <= len(user_pwd):
            print("*",end="")
            length_count += 1
        print("\n Correct!")
    else:
        print("Wrong!")
else:
    print("Minimum password length is 6")

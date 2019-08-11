"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!

score = ""
result = ""

def main():
    global score, result
    score = ask_user()
    result = mark_scheme(score)
    print(result)

def ask_user():
    global score
    score = float(input("Enter score: "))
    return score


def mark_scheme(score):
    global result
    if score < 0:
        result = "Invalid score"
    else:
        if score > 100:
            result = "Invalid score"
        if score > 50:
            result = "Passable"
        if score > 90:
            result = "Excellent"
        if score < 50:
            result = "Bad"
    return result

main()



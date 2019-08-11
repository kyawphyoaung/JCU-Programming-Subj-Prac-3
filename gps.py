"""
GPS (Gopher Population Simulator) V1.0
    by Kyaw Phyo Aung
    JCU ID: 13822414
"""
import random

WELCOME = """Welcome to the Gopher Population Simulator!
V1.0 by Kyaw Phyo Aung
"""
INT_POPU = 1000

def main():
    year = 1
    now_popu = INT_POPU
    print(WELCOME)
    print("Starting Population {}".format(INT_POPU))
    print("Year {}".format(year))
    prediction(now_popu, year)


def prediction(now_popu, year):
    while year < 10:
        year += 1
        ten_percent = now_popu * 0.1
        twenty_percent = now_popu * 0.2
        five_percent = now_popu * 0.05
        twentyfive_percent = now_popu * 0.25

        numofborn = random.randrange(int(ten_percent), int(twenty_percent))
        now_popu += numofborn

        numofdie = random.randrange(int(five_percent), int(twentyfive_percent))
        now_popu -= numofdie
        print("\n")
        print("{} gophers were born. {} died".format(numofborn, numofdie))
        print("Population: {}".format(now_popu))
        print("Year {}".format(year))


main()
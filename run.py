import time
import sys


class Player:
    """
    Store player name and pick ups
    """
    def __init__(self, name, griff, lucky_dice):
        self.name = name
        self.griff = griff
        self.lucky_dice = lucky_dice


def slow_print(text):
    """
    Slower print for speech
    """
    for c in text:
        print(c, end='')
        sys.stdout.flush()
        time.sleep(0.1)


def new_game():
    """
    Starts the game
    """
    print("Start new game?")
    answer = input("[yes/no]\n")
    if answer.lower() == "yes":
        print("Great! Let us begin!")
        name = input("Please enter your name:\n")
        global p1
        p1 = Player(name, False, False)
        act1()
    elif answer.lower() == "no":
        print("Shame. Maybe another time. Good bye.")
    else:
        print("Please enter either yes or no")
        new_game()


def act1():
    """
    The first act of the game
    """
    print("Leaving the safety of your home, your journey begins")
    print("You enter a dark forest, struggling to see the path before you")
    print("Suddenly, a voice cries out from the dark")
    slow_print(f"..is that.. ..is that you {p1.name}?\n")
    answer = input("Do you answer the voice? [yes/no]\n")
    if answer.lower() == "yes":
        print("You answer the voice and get nothing but silence in return")
    elif answer.lower() == "no":
        print("You ignore the voice and keep walking")
        print("Suddenly the air grows cold and your body frozen in place.")
    else:
        print("Please enter either yes or no")
        act1()


# run game
new_game()
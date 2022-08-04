class Player:
    """
    Store player name and pick ups
    """
    def __init__(self, name, griff, lucky_dice):
        self.name = name
        self.griff = griff
        self.lucky_dice = lucky_dice


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
    elif answer.lower() == "no":
        print("Shame. Maybe another time. Good bye.")
    else:
        print("Please enter either yes or no")
        new_game()


new_game()
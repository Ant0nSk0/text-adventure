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


def death():
    """
    Game over message.
    """
    print()
    print(f"This journey ends here. Better luck next time, {p1.name}\n")
    new_game()


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
    print()
    print("Leaving the safety of your home, your journey begins.")
    print("You enter a dark forest, struggling to see the path before you.")
    print("Suddenly, a voice cries out from the dark.")
    slow_print(f"..is that.. ..is that you {p1.name}?\n")
    answer = input("Do you answer the voice? [yes/no]\n")
    if answer.lower() == "yes":
        print("You answer the voice and get nothing but silence in return.")
        print("A dark figure appears in the distance.")
        answer2 = input("Do you approach the figure? [yes/no]\n")
        if answer2.lower() == "yes":
            print("You approach the figure.")
            print("There is something familiar about it.")
            print("The figure reaches out its hand to give you something.")
            answer3 = input("Do you accept the gift? [yes/no]\n")
            if answer3.lower() == "yes":
                print("You accept the gift.")
                print("It appears to be a medallion of sort")
                print("Might be valuable. Or magic. Seems important.")
                print("Something about the item has you enchanted")
                print("and you start to lose touch with reality..")
                act2()
            elif answer3.lower() == "no":
                print("You refuse the gift, clearly upsetting the figure")
                slow_print("..You were supposed to be the one..\n"
                           "..you were supposed to save me..\n")
                print("The figure disappears as you feel a terrible chill")
                print("Slowly all life fades away")
                death()
            else:
                print("You hesitate and utter something incoherent.")
                print("The figure lost all hope and left you to die")
                death()
        elif answer2.lower() == "no":
            print("You decide to turn around and go the other way")
            print("Trying to outrun the evils of the forest,"
                  " you trip and fall")
            print("It's too late.. ")
            death()
        else:
            print("You seem confused.")
            print("The figure shakes its head and leaves you for dead")
            death()
    elif answer.lower() == "no":
        print("You ignore the voice and keep walking.")
        print("Suddenly the air grows cold and your body frozen in place.")
        death()
    else:
        print("Please enter either yes or no")
        act1()


def act2():
    """
    The second act of the game
    """
    print()
    print("You wake up all of a sudden with a gasp. It's no longer dark.")
    print("Confused about what just happened, you look around you")
    print("and wonder where to go and what to do next\n")
    print("Do you want to go deeper into the forest or head to town?")
    answer = input("[forest/town]\n")
    if answer.lower() == "forest":
        print("You decide to go deeper into the forest")
        print("It quickly gets dark again and you start to lose clarity")
        print("Your mind runs away from you and all turns black")
        act2()
    elif answer.lower() == "town":
        print("you go to town")
    else:
        print("Not possible. Try again")
        act2()


# run game
new_game()
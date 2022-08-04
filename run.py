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
        print("You head towards the town")
        print("The town before you is in very bad shape.")
        print("You decide to try and find some locals")
        print("Where do you want to go?")
        answer2 = input("[tavern/market]\n")
        if answer2.lower() == "tavern":
            print()
            print("You find an old tavern, with a few locals in it\n")
            time.sleep(0.5)
            print("The air reeks of smoke and booze, sweat and despair.")
            print("The barkeep glares at you as the room fills with silence\n")
            time.sleep(1)
            slow_print("...and you are?\n")
            print("he says, placing a bottle of rum upon the bar")
            print()
            time.sleep(1)
            print("[a]: Tell the barkeep your name and ask for information")
            print("[b]: Say nothing. Grab the bottle. Pay and go sit down.")
            answer3 = input("How do you answer?\n")
            if answer3.lower() == "a":
                print()
                slow_print(f"...{p1.name}, huh? Lookin' for information hm?\n")
                slow_print("...heh Well that'll cost ya..\n")
                answer4 = input("Pay the barkeeper?\n [yes/no]\n")
                if answer4.lower() == "yes":
                    print()
                    slow_print("..heh heh cheers. now, have a drink.\n")
                    slow_print("..Then go 'round back, ask for Griff\n")
                    p1.griff = True
                elif answer4.lower() == "no":
                    print()
                    slow_print("..Cheap are we?\n")
                    time.sleep(1.5)
                    print("BOYS!")
                    print("Suddenly a wooden plank connects to "
                          "the back of your skull")
                    print("Everything turns black")
                    death()
                else:
                    print()
                    print("Somehow you insulted the barkeep")
                    print("Before you know it, a whistle and a swing")
                    print("Bat to the back and everything turns black")
                    death()
            elif answer3.lower() == "b":
                print()
                print("You go sit down, having a drink, looking around")
                print("You keep scanning the room with your eyes")
                print("You notice strange noises from a beyond a back door")
                print("But before you can get up and investigate,")
                print(" a stranger takes a seat across from you.")
            else:
                print()
                print("Somehow you insulted the barkeep")
                print("Before you know it, a whistle and a swing")
                print("A bat to the back and everything turns black")
                death()

        elif answer2.lower == "market":
            print()
            print("you went to the market\n")
            time.sleep(0.5)
            print("Theres not much people around. It's very silent")
            print("Almost too silent...")
            print("Before you know it you get ambushed by a group of bandits")
            print("This does not end well...")
            death()
        else:
            print("You have trouble making a decent decision\n")
            time.sleep(0.5)
            print("Staying idle in this town is a very bad idea")
            print("Before you know it, bandits ambush you. You have no chance")
            death()
    else:
        print("Not possible. Try again")
        act2()


# run game
new_game()
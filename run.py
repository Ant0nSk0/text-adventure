"""
Text Adventure Game
"""
import time
import sys
import random
from colorama import init, Fore


init(autoreset=True)


class Player:
    """
    Store player name and pick ups
    """
    def __init__(self, name, griff, lucky_dice):
        self.name = name
        self.griff = griff
        self.lucky_dice = lucky_dice


p1 = Player('', False, False)


def slow_print(text):
    """
    Slower print for speech
    """
    for char in text:
        print(char, end='')
        sys.stdout.flush()
        time.sleep(0.1)


def death():
    """
    Game over message.
    """
    print()
    print(Fore.RED + "  --GAME OVER--\n")
    print(f"This journey ends here. Better luck next time, {p1.name}\n")
    new_game()


def new_game():
    """
    Starts the game
    """
    print(Fore.GREEN + "Start new game?")
    answer = input("[yes/no]\n")
    if answer.lower() == "yes":
        print("\n"*24)
        print("Great! Let us begin!")
        p1.name = input("Please enter your name:\n")
        p1.griff = False
        p1.lucky_dice = False
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
    print()
    answer = input("Do you answer the voice? [yes/no]\n")
    if answer.lower() == "yes":
        print()
        print("You answer the voice and get nothing but silence in return.")
        print("A dark figure appears in the distance.")
        answer2 = input("Do you approach the figure? [yes/no]\n")
        if answer2.lower() == "yes":
            print()
            print("You approach the figure.")
            print("There is something familiar about it.")
            print("The figure reaches out its hand to give you something.")
            answer3 = input("Do you accept the gift? [yes/no]\n")
            if answer3.lower() == "yes":
                print()
                print("You accept the gift.\n")
                time.sleep(1)
                print("It appears to be a medallion of sort")
                print("Might be valuable. Or magic. Seems important.")
                print("Something about the item has you enchanted")
                print("and you start to lose touch with reality..")
                time.sleep(2)
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
        print()
        print("You head towards the town")
        print("The town before you is in very bad shape.")
        print("You decide to try and find some locals")
        print("Where do you want to go?")
        answer2 = input("[tavern/market]\n")
        if answer2.lower() == "tavern":
            print()
            print("You find an old tavern, with a few locals in it\n")
            time.sleep(1)
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
                    act3()
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
                act2b()
            else:
                print()
                print("Somehow you insulted the barkeep")
                print("Before you know it, a whistle and a swing")
                print("A bat to the back and everything turns black")
                death()

        elif answer2.lower() == "market":
            print()
            print("you went to the market\n")
            time.sleep(1)
            print("Theres not much people around. It's very silent")
            print("Almost too silent...")
            print("Before you know it you get ambushed by a group of bandits")
            print("This does not end well...")
            death()
        else:
            print("You have trouble making a decent decision\n")
            time.sleep(1)
            print("Staying idle in this town is a very bad idea")
            print("Before you know it, bandits ambush you. You have no chance")
            death()
    else:
        print("Not possible. Try again")
        act2()


def act2b():
    """
    Alternative path from act2 to act3
    Gives the player a dice rolling minigame
    """
    print()
    print("The strange man takes out a pair of dice, asking to play")
    play_dice = input("Would you like to play som dice?[yes/no]\n")
    if play_dice.lower() == "yes":
        play = True
        while play:
            die1 = random.randrange(1, 7)
            die2 = random.randrange(1, 7)
            print("Let's play, highest number wins.\n")
            print("Stranger:")
            print(f"  +---+\n"
                  f"  | {die2} |\n"
                  f"  +---+")
            print()
            print(f"{p1.name}:")
            print(f"  +---+\n"
                  f"  | {die1} |\n"
                  f"  +---+")
            print()
            if die1 > die2:
                print(f"{p1.name} wins")
            elif die2 > die1:
                print("Stranger wins")
            else:
                print("It's a draw")
            print()
            play_dice = input('Play again? [yes/no]\n')
            if play_dice.lower() == "no":
                play = False
                print("You decide that's enough for now so you stand up")
                print("The stranger smiles and says:")
                print()
                slow_print(f"..Very well {p1.name}..")
                slow_print(" I trust you have more important things to do\n")
                slow_print(
                    "..You should take this with you\n")
                slow_print(
                    "..You never know when you'll need some extra luck\n")
                print()
                print(
                    "After accepting the dice, you decide to go out the back")
                time.sleep(1.5)
                p1.lucky_dice = True
                act3()
    else:
        print("You decide you don't have time for this.")
        print("Ignoring the stranger you leave via the back door")
        time.sleep(1.5)
        act3()


def act3():
    """
    The third act of the game
    """
    print()
    time.sleep(1.5)
    print("As you go out back, you see a short little creature")
    print("Green skin, long nose, long ears. Cursing like a sailor")
    print("You reckon it's a goblin\n")
    time.sleep(2)
    print("The goblin seems to be going through some bags and boxes")
    print("Frantically digging through it's contents\n")
    time.sleep(2)
    if p1.griff:
        print("[griff]: Ask if the goblin is called Griff or if he knows him")
    elif not p1.griff:
        print("[ask]: 'Is everything in order here?'")
    print("[fight]: This creature seem to be up to no good, I must fight!")
    answer = input("How will you approach the creature?\n")
    if answer.lower() == "griff":
        print()
        print("The goblin jumps up, startled by hearing his name")
        time.sleep(1)
        slow_print("..oh yes yes, Griff is my name.\n")
        slow_print("..But that's not for you to know now, who told you?\n")
        slow_print("..oh I bet it was that ol' bastard behind the bar\n")
        slow_print("..He keeps selling me out.\n")
        time.sleep(1.5)
        print()
        print("..And I won't see half of the coin he took, I bloody know it\n")
        time.sleep(2)
        slow_print(".. oh well..\n")
        slow_print("..Half of something is still better than all of nothing\n")
        slow_print("..Now what do you want?\n")
        print()
        print("[a]: Ask about the medallion")
        print("[b]: Ask about the forest")
        answer2 = input("What do you ask Griff?\n")
        if answer2.lower() == "a":
            print()
            print("You pull out the medallion to show him\n")
            print("..ARE YOU MAD? DO YOU HAVE A DEATHWISH? PUT IT AWAY")
            slow_print("..quickly now, follow me.. we'll talk in private\n")
            time.sleep(2)
            act4()
        elif answer2.lower() == "b":
            print()
            print("You ask about the forest and tell Griff about the figure")
            print("The goblin scratches his head, and looks around nervously")
            slow_print("..We can't talk here, come, follow me.\n")
            time.sleep(2)
            act4()
        else:
            print()
            print("While trying to speak your mind, bandits approached")
            print("Griff managed to escape. You however....")
            death()
    elif answer.lower() == "ask":
        print()
        print("The goblin shakes his head\n")
        slow_print("..Nothing is in order in this land..\n")
        slow_print("..Look, I got a business here..\n")
        slow_print("..You need something?..\n")
        slow_print("..I sell trinkets, 'magic' items etc etc you get it\n")
        print("..I'm short on time. Hurry up now.\n")
        print("[a]: Ask for information")
        print("[b]: Ask for magic items")
        answer3 = input("What do you need?\n")
        if answer3 == "a":
            print()
            print("You tell about what you experienced in the forest")
            print("You ask if he knows anything about it")
            print("He introduces himself as Griff and says:\n")
            slow_print("..Follow me, we must talk in private\n")
            act4()
        elif answer3 == "b":
            print()
            print("You ask about magic items and attempt to buy some")
            print("The goblin sees your coin and smirks, handing over an item")
            print("It is a very odd stone, glowing slightly\n")
            time.sleep(2)
            print("Suddenly the stone explodes into a sharp mist")
            print("Rendering you paralysed, the goblin loot all your coin")
            print("He even takes the medallion. Nothing you can do now\n")
            slow_print("..sorry pal..\n")
            death()
        else:
            print()
            print("The goblin grows impatient and throws a stone at your head")
            print("He then proceeds to loot all your coin and belongings")
            slow_print("..sorry pal..")
            death()
    elif answer.lower() == "fight":
        print()
        time.sleep(1)
        print("You prepare yourself to fight the creature, charging forward")
        print("The goblin however turns around faster than you can blink")
        print("A dagger comes flying and hits you right between the eyes")
        death()
    else:
        print("Not an option Try again")
        act3()


def act4():
    """
    Fourth act of the game
    """
    print()
    time.sleep(1)
    print("You follow Griff into a hidden passage below a crypt")
    print("Far below ground you reach a large room")
    time.sleep(1)
    print("You proceed to tell him everything about what happened")
    print("Griff thinks deeply for a bit, then responds:\n")
    slow_print("..The medallion connects you to that spirit\n")
    print()
    print("..hm.. The way i see it, you have two options\n")
    time.sleep(2)
    slow_print("..Either you perform the ritual, at a risk\n")
    slow_print("..Or you give it to me. I'll sell it off\n")
    slow_print("..Just transfer some magic stuff. Easy. I'll make good coin\n")
    print()
    print("What will you do?")
    answer = input("[a]: Perform the ritual. [b]: give medallion to Griff\n")
    if answer.lower() == "a":
        print()
        print("You decide to perform the ritual")
        print("Griff nods and starts to gather some supplies")
        slow_print("..Back into the forest we go.. \n")
        slow_print("..The medallion won't protect you once we start..\n")
        finale()
    elif answer.lower() == "b":
        print()
        print("You decide to hand it over to Griff for him to sell.")
        print("This has been enough adventuring for you.")
        time.sleep(2)
        print("You decide to go home and forget about the whole thing")
        time.sleep(2)
        print("You can't even remember why you left to begin with\n")
        print("...Was there a princess to be saved? Coin to be had?")
        print("Evil to be banished? No matter. \n")
        print("Not your problem anymore. Go home and rest")
        time.sleep(2)
        the_end()
    else:
        print()
        act4()


def the_end():
    """
    The End message
    """
    print()
    time.sleep(2)
    print(f"This story has come to an end. Well done {p1.name}!")
    print("However, there's more to this story. Other paths to take.")
    print("Feel free to play again, and see how it ends next time\n")
    print()
    print(Fore.YELLOW + "                     #########################")
    print(Fore.YELLOW + "                     # Thank you for playing #")
    print(Fore.YELLOW + "                     #########################")
    time.sleep(4)
    new_game()


def finale():
    """
    Final Act of the game
    """
    print()
    time.sleep(2)
    print("You enter the forest once again to prepare the ritual")
    print("Griff starts to draw a circle on the ground")
    print("Chanting some spell, that suddenly changes tone..")
    print("Into a conversation in a dead language..\n")
    time.sleep(2)
    print("Griff turns to you and start to speak:")
    slow_print("..sooo, this is going to sound silly, but..\n")
    slow_print("..in order to free our spirit, and now us, I guess..\n")
    slow_print("..you have to play a game against the dark spirit here.\n")
    slow_print("..That's his terms, I guess he's lonely or something..\n")
    print("..anyway. simple stuff..")
    slow_print("..Roll the die and hope not to, you know, die..\n")
    print()
    time.sleep(2)
    print("The dark spirit rolls first. He rolls a 5.")
    if p1.lucky_dice:
        print("You remembered the lucky die the stranger gave you")
        print("Use the lucky dice? [luck]")
    elif p1.griff:
        print("Griff offers you his dice, it's just plain normal")
        print("Use Griffs die? [griff]")
    print("The dark spirit provides a die as well [spirit]")
    answer = input("Which die will you use?\n")
    if answer.lower() == "luck":
        print()
        print("You throw the lucky die the stranger gave you")
        print("  +---+\n"
              "  | 6 |\n"
              "  +---+")
        print()
        print("It seems you rolled a six, beating the dark spirit")
        print("The dark spirit gets upset, but honors his deal")
        print("You and the freed spirits flee the forest\n")
        time.sleep(2)
        print("That's enough adventure for now")
        print("The dark spirit still haunts the forest")
        print("But no one enters without a good lucky die\n")
        the_end()
    elif answer.lower() == "griff":
        print()
        die1 = random.randrange(1, 7)
        print("you throw the die that Griff gave you")
        print(f"  +---+\n"
              f"  | {die1} |\n"
              f"  +---+\n")
        print(f"You rolled {die1}")
        while die1 == 5:
            die1 = random.randrange(1, 7)
            print("We'll roll again")
            print("Spirit got 5 again")
            print()
            print(f"  +---+\n"
                  f"  | {die1} |\n"
                  f"  +---+\n")
            print(f"you rolled {die1}")
        if die1 < 5:
            print("The dark spirit smiles and everything turns black")
            death()
        elif die1 == 6:
            print("It seems you rolled a six, beating the dark spirit")
            print("The dark spirit gets upset, but honors his deal")
            print("You and the freed spirits flee the forest\n")
            time.sleep(2)
            print("That's enough adventure for now")
            print("The dark spirit still haunts the forest")
            print("But no one enters without a good lucky die\n")
            the_end()
    elif answer.lower() == "spirit":
        print()
        print("You throw the die that the spirit gave you")
        print("  +---+\n"
              "  | 1 |\n"
              "  +---+\n")
        slow_print("oh my.. This isn't good..\n")
        print("The dark spirit smiles and everything turns black")
        death()


# Intro + Run Game
print(Fore.YELLOW +
      "                ##############################################\n"
      "                #                                            #\n"
      "                #          WELCOME TO THE ADVENTURE          #\n"
      "                #                                            #\n"
      "                ##############################################")
print()
time.sleep(2)
print("\n")
print("We find ourselves in dangerous times, evil spirits haunt the forest,")
print("People have gone missing, poverty and crime is everywhere")
print("Death lurks around every corner.\n")
print("In search for a lost loved one, for coin or to put an end to this evil")
print("Our hero (that's you!) starts their journey towards death or glory\n")
slow_print("                             --- GOOD LUCK! ---\n")
print()
new_game()

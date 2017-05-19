# Coded by Domo4862
# This short fighting fantasy is made by Stuart Lloyd
# Reference from (https://docs.google.com/file/d/0Bw3nCQKxLG5_ZjRlNmRjYjQtMjEwNy00M2EzLTg4ZjItZjM5MDcxMzFlMTdj/view)
# Slight modifications to the text have been made for implementation in python

from random import randint

# Player Stats
SKL = 0
STA = 0
LCK = 0

# Event Modifiers
altar = 0  # para 3 altar blessing
apprentice = 0  # para 4 attack while distracted
wolf = 0  # para 13 sneak on wolf
penalty = 1  # para 19 drowsiness
shock = 0  # para 22 (If you are unlucky with magic eye)


def main():
    # Introduction
    print("Welcome to Forest of Chaos")
    print("")
    print("INTRODUCTION")
    print("In this adventure, you are an apprentice to the Grand Wizard of Yore in the forest near Salamonis.")
    print("Someone has stolen his familiar and he has tasked you to stop the thief and recover the familiar.")
    print("")

    print("Enter '1' to roll for stats")
    while True:
        x = input()
        if x == '1':
            break

    # Die Rolling
    print("")
    print("Rolling dice for stats:")
    roll()
    print("SKILL =", SKL)
    print("STAMINA =", STA)
    print("LUCK =", LCK)
    print("")
    print("You have your staff to use in combat and you are dressed in your wizard's robes.")
    print("")
    print("Enter '1' to Start")
    while True:
        x = input()
        if x == '1':
            break

    # Begin Adventure
    print("")
    print("Background")
    print("Its not easy being the apprentice to the Grand Wizard of Yore.")
    print("It took you a month to learn the Elvish etiquette and hand signals to stop the native half elves killing")
    print("you on sight. You then had to learn seven different languages and how to play the harp, piano and flute.")
    print("Apparently, this was to make sure your hands could do the precise wind in the bag before you actually had")
    print("to learn a spell. But once all that was done, you had to perform seemingly ludicrous task, though. Feed a")
    print("cow to a tree. Make a hand print in the ground that last for a week. Eat nothing but orange food for a")
    print("month. The list goes on. Apparently, these are the tasks that one who wants to attain true enlightenment")
    print("must go through, but they just infuriated you. This happened for years. Until this morning, when your")
    print("master approached you with a task you understand. My familiar has been kidnapped! I can sense it in this")
    print("wood, but it is moving out fast. It is with another sorcerer, an apprentice to Balthus Dire. You need to")
    print("find him and free him. The Grand Wizard's familiar is a crow with an acerbic wit. You immediately grab your")
    print("staff and head out into the wood to find the crow.")
    print("")
    print("Enter '1' to begin your adventure")
    while True:
        x = input()
        if x == '1':
            break
    start()


# Chapter functions
def start():
    print("")
    print("You come to a fork in the path. Would you:")
    print("1. Go left")
    print("2. Go right")
    print("3. Mediate on psychic residues to see if anything went by (Using magic has its risks")
    print("4. Expand your sight and see whats down each path")
    while True:
        x = input()
        if x == "1":
            twenty()
        elif x == "2":
            fifteen()
        elif x == "3":
            five()
        elif x == "4":
            thirteen()


def two():
    global STA
    print("")
    print("Somehow, the mage can still see you and a bolt of fire shoots out of his hands and hits you.")
    print("Lose 6 Stamina Points.")
    STA -= 6
    if STA < 0:
        lose()
    print("How will you counter attack him? Would you:")
    print("1. Use fireball")
    print("2. Befuddle him")
    while True:
        x = input()
        if x == "1":
            nineteen()
        elif x == "2":
            four()


def three():
    global altar
    print("")
    print("The bear stares at you as you approach the altar, but makes no move to attack you.")
    print("When you touch it, a feeling of warmth and energy flows through you.")
    print("For the remainder of the adventure, if you have to test your luck in a NON COMBAT situation,")
    print("you will AUTOMATICALLY BE LUCKY and will NOT HAVE TO deduct a luck point.")
    altar += 1
    print("1. Continue through the forest.")
    while True:
        x = input()
        if x == "1":
            seventeen()


def four():
    global apprentice
    print("")
    print("You cast the spell. The apprentice is mumbling but immediately stops, distracted by a bird.")
    print("When you fight him, you will AUTOMATICALLY WIN THE FIRST attack round.")
    apprentice += 1
    print("1. You rush up to him and take him by surprise.")
    while True:
        x = input()
        if x == "1":
            twentyone()


def five():
    print("")
    print("You relax and close your eyes.")
    print("After awhile of breathing, slowly, you start to see colours and shapes through your third eye.")
    print("You see a faint aura leading LEFT. It is a recent psychic trail but it is weak and may not have")
    print("been made by something very intelligent.")
    print("Would you:")
    print("1. Go left")
    print("2. Go right")
    while True:
        x = input()
        if x == "1":
            twenty()
        elif x == "2":
            fifteen()


def six():
    global LCK
    print("")
    print("The apprentice breaks off from combat and pulls a vial out from the sleeves of his robes.")
    print("He uncorks it and flings it into your face. You are engulfed in a strange gas.")
    print("1. Test your luck")
    while True:
        x = input()
        if x == "1":
            if altar == 1:
                print("You received the altar's blessing.")
                ten()
            else:
                y = randint(1, 12)
                print(LCK)
                print(y)
                if y > LCK:
                    print("You are unlucky")
                    LCK -= 1
                    fourteen()
                else:
                    print("You are lucky")
                    LCK -= 1
                    ten()


def seven():
    print("")
    print("You free the crow from the cage who thanks you. You then mumble the words of the levitation spell on")
    print("the apprentice. His unconscious body rises to your waist height and you push him back to your master")
    print("who is sitting in his favourite clearing, reading a book. He thanks you for returning his familiar and")
    print("then performs some telepathy on the apprentice to discern his secrets. Balthus Dire is apparently going")
    print("to invade the Vale of Willow soon. Just then, a half elf bursts into the clearing. 'Master, master...'")
    print("he begins. 'Balthus Dire is going to invade soon?' Asks the Grand Wizard, matter of factly.")
    print("'Yes. How did you know?' Asks the half elf, amazed. The Grand Wizard does not reply, but just looks at you.")
    print("He knows exactly what you want to do, so you run off immediately to pack...")
    win()


def eight():
    print("")
    print("You speak the words of the spell and put your hands on the tree.")
    print("You then hear a loud and ancient voice in your head.")
    print("'Human!, What brings you here?'")
    print("You explain that you are seeking the Grand Wizards familiar.")
    print("'I may help you, flesh one'. Says the tree.")
    print("'But I am old and need life. Can you give up some of your life for me?")
    print("Would you:")
    print("1. Agree to give some life")
    print("2. Leave the tree and continue")
    while True:
        x = input()
        if x == "1":
            twentyfive()
        elif x == "2":
            twentythree()


def nine():
    global LCK
    print("")
    print("As a wizard of the forest, you are bound to protect it.")
    print("Slaying a creature that was not hostile to you is in violation of your oath.")
    print("You lose 1 luck point.")
    LCK -= 1
    print("1. Leave the area")
    while True:
        x = input()
        if x == "1":
            seventeen()


def ten():
    print("")
    print("You close your mouth and hold your breath, avoiding taking a gulp of gas.")
    print("You jump out of the cloud and strike the apprentice in the head.")
    print("He crumples to the ground, unconscious.")
    print("1. Free the crow")
    while True:
        x = input()
        if x == "1":
            seven()


def eleven():
    print("")
    print("You wave your hands in the shapes that counter the apprentices and you manage to stop it.")
    print("A small flame shoots out of his finger and falls to the ground with a splutter.")
    print("How will you attack him:")
    print("1. Use fireball")
    print("2. Befuddle him")
    while True:
        x = input()
        if x == "1":
            nineteen()
        elif x == "2":
            four()


def twelve():
    print("")
    print("You babble a spell that allows you to understand the language of animals.")
    print("'Hello.' You said to the bear.")
    print("'Greetings, friend of the forest.' Replied the bear. The bear is not hostile, so you continue.")
    print("'Did you perchance see a wizard carrying a bird? It is a familiar he has kidnapped'")
    print("'I did; he passed this way only an hour ago. He stopped at the altar to cast a spell of protection on")
    print("himself. He told the bird that he would now be IMMUNE TO ANY FIREBALLS his rivals would attack him with.'")
    print("You thank the bear. It also advises you to touch the altar as it bestows a blessing to all who use magic.")
    print("1. Touch the altar")
    while True:
        x = input()
        if x == "1":
            three()


def thirteen():
    global LCK
    global wolf
    global shock
    print("")
    print("You sit on the ground and close your eyes. You speak the words of your spell")
    print("Then you can see yourself in the clearing. You can see in all directions.")
    print("You can move your magical eye on the right path and eventually come to a clearing with an altar.")
    print("This is as far as you can go and so you move your eye back to the clearing and then along the left path.")
    print("You go a hundred meters down there and see a wolf sniffing around.")
    print("You look at it for a couple of seconds, but then the wolf looks up with a start.")
    print("It has sensed your magic eye.")
    print("1. Test your luck")
    while True:
        x = input()
        if x == "1":
            y = randint(1, 12)
            print("Your luck = ", LCK)
            print("Dice = ", y)
            if y > LCK:
                print("You are unlucky")
                shock += 1
                twentytwo()
            else:
                print("You are lucky")
                wolf += 1
                break
    LCK -= 1
    print("Your new luck = ", LCK)
    print("")
    print("The wolf loses interest and goes back sniffing around in the undergrowth.")
    print("Which way would you go?")
    print("1. Left fork (Fight the wolf but you automatically win the first attack round due to surprise.)")
    print("2. Right fork (towards the altar).")
    while True:
        x = input()
        if x == "1":
            twenty()
        elif x == "2":
            fifteen()


def fourteen():
    print("")
    print("You can't avoid taking a lungful of gas and start to feel an overwhelming sense of drowsiness. You collapse")
    print("on the floor and fall asleep. When you awake, there is no sign of the apprentice or the familiar.")
    print("")
    lose()


def fifteen():
    print("")
    print("You walk along the path for about fifteen minutes before you come to a clearing. The clearing has an altar")
    print("made of pure white marble. However, there is a large brown bear staring at you in the clearing.")
    print("Would you:")
    print("1. Approach the altar despite the bear")
    print("2. Attack the bear")
    print("3. Use magic to sense danger")
    print("4. Use magic to talk to bear")
    print("5. Go back the path and take the left path instead")
    while True:
        x = input()
        if x == "1":
            three()
        elif x == "2":
            twentyfour()
        elif x == "3":
            eighteen()
        elif x == "4":
            twelve()
        elif x == "5":
            twenty()


def sixteen():
    print("")
    print("You fall asleep. When you awake, the apprentice has long gone.")
    print("")
    lose()


def seventeen():
    print("")
    print("After another 10 minutes of walking, you come to a clearing with a large tree.")
    print("Its leaves are looking a bit brown and its branches are drooping.")
    print("You have a spell which allows you to talk to plants and this ancient tree may have much wisdom.")
    print("Would you:")
    print("1. Use magic to speak to the tree")
    print("2. Continue through the forest")
    while True:
        x = input()
        if x == "1":
            eight()
        elif x == "2":
            twentythree()


def eighteen():
    print("")
    print("You sense that the bear is no threat and that there are no traps.")
    print("1. You approach the altar.")
    while True:
        x = input()
        if x == "1":
            three()


def nineteen():
    print("")
    print("The fireball flies towards him and engulfs him. However, the flames do not harm him and he laughs.")
    print("The flames go out and he starts to chant in a low tone while swaying.")
    print("He is trying to put you to sleep")
    print("1. Test your luck")
    while True:
        x = input()
        if x == "1":
            y = randint(1, 12)
            print("Your luck = ", LCK)
            print("Dice = ", y)
            if y > LCK:
                print("You are unlucky")
                sixteen()
            else:
                print("You are lucky")
                print("You manage to stay awake but you are drowsy.")
                print("Reduce attack strength by 1 in your combat with apprentice.")
                twentyone()


def twenty():
    print("")
    print("You start to walk down the path and then see a large grey wolf sniffing around.")
    print("It stops and then looks at you. With a growl, it charges at you, bearing its teeth")
    print("")
    print("FIGHT")
    print("")
    combat('Wolf')


def twentyone():
    print("")
    print("The wizard draws a curved knife, ready to fight you.")
    combat('Apprentice')


def twentytwo():
    print("")
    print("You see the wolf growl and then see it bound down the path in your direction. You panic and")
    print("start to bring your consciousness back into your body. You open your eyes to see the wolf")
    print("standing in the clearing growling. You must fight it.")
    combat('Wolf')


def twentythree():
    print("")
    print("After fifteen minutes, you find the apprentice with the bird. He is WEARING GLASSES. He sees")
    print("you and starts mumbling a spell of attack.")
    print("Would you:")
    print("1. Try to dispel it")
    print("2. Make yourself invisible")
    while True:
        x = input()
        if x == '1':
            eleven()
        elif x == '2':
            two()


def twentyfour():
    print("")
    print("As you raise your staff, the bear rises up on its hind legs and beats its chest with its claws.")
    print("Then it charges at you. This will be a difficult fight.")
    combat('Bear')


def twentyfive():
    global STA
    print("")
    print("Pain runs through your arms and a feeling of fatigue comes over you")
    print("You lose 4 stamina points.")
    STA -= 4
    print("Your Stamina = ", STA)
    if STA < 0:
        lose()
    print("The tree's branches start to look more sturdy. It speaks to you again. 'Thank you flesh one.")
    print("The man you are seeking did come this way. He stopped here to put on a PAIR of GLASSES. I heard him")
    print("talking to himself; saying that they let him see INVISIBLE THINGS.' You thank the tree and leave.")
    print("1. Proceed onwards")
    while True:
        x = input()
        if x == '1':
            twentythree()


def roll():
    global SKL
    global STA
    global LCK

    # Roll for Skill
    a = randint(1, 6)
    if a < 3:
        SKL = 6
    elif 2 < a < 5:
        SKL = 7
    elif a > 4:
        SKL = 8

    # Roll for Stamina
    b = randint(1, 6)
    STA = b + 9

    # Roll for Luck
    c = randint(1, 6)
    if c < 3:
        LCK = 10
    elif 2 < c < 5:
        LCK = 11
    elif c > 4:
        LCK = 12


def combat(n):
    global SKL
    global LCK
    global STA
    global wolf
    global shock
    eSTA = 0
    eSKL = 0

    if n == 'Wolf':
        eSTA += 6
        eSKL += 5
    elif n == 'Bear':
        eSTA += 8
        eSKL += 7
    elif n == 'Apprentice':
        eSTA += 10
        eSKL += 6

    if n == 'Wolf' and wolf == 1:
        eSTA -= 2
        print("Preemptive strike. Wolf Stamina is now ", eSTA)

    while eSTA > 0 and STA > 0:
        print("")
        print("{} Stamina = {}".format(n, eSTA))
        print("Your Stamina = ", STA)
        print("Your Luck = ", LCK)
        print("Enter '1' to roll dice")
        x = input()
        if x == "1":
            p = randint(1, 12) + SKL
            w = randint(1, 12) + eSTA
            # Win duel
            if p > w:
                eSTA -= 2
                print("You won the duel")
                if LCK != 0:
                    print("Do you want to try your luck?")
                    print("1. Yes")
                    print("2. No")
                    while True:
                        y = input()
                        if y == '1':
                            r = randint(1, 12)
                            if LCK > r:
                                print("You are lucky. You dealt 4 damage.")
                                eSTA -= 2
                            else:
                                print("You are unlucky. You merely scratched him for 1 damage.")
                                eSTA += 1
                            LCK -= 1
                            break
                        elif y == '2':
                            print("You dealt 2 damage")
                            break
                else:
                    print("You dealt 2 damage")
            # Lose Duel
            elif w > p:
                STA -= 2
                print("You lost the duel")
                if LCK != 0:
                    print("Do you want to try your luck?")
                    print("1. Yes")
                    print("2. No")
                    while True:
                        y = input()
                        if y == '1':
                            r = randint(1, 12)
                            if LCK > r:
                                print("You are lucky. You only receive 1 damage.")
                                STA += 1
                            else:
                                print("You are unlucky. You receive 3 damage")
                                STA -= 1
                            LCK -= 1
                            break
                        elif y == '2':
                            print("You receive 2 damage")
                            break
                else:
                    print("You receive 2 damage")
            elif p == w:
                print("Draw")
        if n == 'Apprentice' and eSTA <= 4:
            break
    if STA < 0:
        print("")
        print("You have been defeated")
        print("")
        lose()

    # Relocate back to chapter after winning
    if n == 'Apprentice' and eSTA <= 4:
        six()
    else:
        print("")
        print("The {} is defeated. Congratulations".format(n))
        if n == 'Bear':
            nine()
        elif n == 'Wolf':
            if shock == 1:
                print("Which path would you choose?")
                print("1. Left path")
                print("2. Right path")
                while True:
                    x = input()
                    if x == '1':
                        seventeen()
                    elif x == '2':
                        fifteen()
            elif shock == 0:
                seventeen()


def win():
    print("")
    print("                                            THE END")
    print("                                      THANKS FOR PLAYING")
    print("")
    print("                                     Enter '1' to end game")
    while True:
        x = input()
        if x == '1':
            exit()


def lose():
    print("THE END")
    print("THANKS FOR PLAYING")
    print("Enter '1' to end game.")
    while True:
        x = input()
        if x == '1':
            exit()

if __name__ == "__main__":
    main()
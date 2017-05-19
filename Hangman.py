# Coded by Domo4862
# A simple Hangman game with 1 player and 2 player mode
# Guess the word or the man gets hanged

from easygui import enterbox
from random import randint

# Global variables
miss = 0  # Counts number of letters missed
guess = []  # Contain the word converted to underscores
letters = []  # Contain letters player has chosen
check = []  # Contain the actual word

# Hangman ASCII art array
pic = [
"""
 #----#
 |    |
      |
      |
      |
      |
==========
""",
"""
 #----#
 |    |
 0    |
      |
      |
      |
==========
""",
"""
 #----#
 |    |
 0    |
 |    |
      |
      |
==========
""",
"""
 #----#
 |    |
 0    |
/|    |
      |
      |
==========
""",
"""
 #----#
 |    |
 0    |
/|\   |
      |
      |
==========
""",
"""
 #----#
 |    |
 0    |
/|\   |
/     |
      |
==========
""",
"""
 #----#
 |    |
 0    |
/|\   |
/ \   |
      |
==========
"""
]


def main():
    global letters
    global check
    global guess
    global miss

    # Welcoming message
    print("Welcome to Hangman.")
    print("You need to guess the word as per displayed on the screen.")
    print("You only have 6 miss before the man is hanged.")
    print("")
    print("How many players? (Enter '1' or '2' players)")
    play = input()

    # Change guess from string to array of chars
    if play == '1':
        print("Choosing word from very tiny database :3")
        words = ["club", "position", "account", "suspect", "uninterested", "lighten", "last", "van", "tasty", "rural",
                 "moan", "nasty", "aware", "base", "delay", "spring", "silent", "cloudy", "immense", "hellish", "screw",
                 "conscious", "hesitant", "parched", "wash", "madly", "birthday", "wasteful", "lying", "quarrelsome",
                 "concern", "friend", "mountainous", "untidy", "comfortable", "work", "embarrass", "playground",
                 "wealth", "questionable", "grin", "complex", "dull", "dinner", "language", "well-off", "long", "noisy",
                 "surprise", "lucky"]
        length = len(words)
        y = words[randint(0, (length - 1))]
        for i in y:
            check += i
    elif play == '2':

        y = enterbox('Input word for friend to guess: ')
        for i in y:
            check += i

    # Convert array of chars to array of blanks
    for i in check:
        guess += '_'

    # Checking mechanism
    while True:
        print("")
        print(pic[miss])
        print(guess)
        print("Previously chose:", letters)
        print("Input:")
        inp = input()

        # Check duplicate entry
        if inp in letters:
            print("Letter already chosen.")
            miss -= 1
        else:
            letters += inp

        # Check entry for correct guess
        if inp in check:
            counter = 0
            pos = []
            for i in check:
                if i == inp:
                    pos.append(counter)
                counter += 1
            for i in pos:
                guess[i] = inp
        else:
            miss += 1

        # Win condition
        if check == guess:
            print("")
            print("Success")
            print("The word is:", y)
            break

        # Lose condition
        if miss == 6:
            print("")
            print(pic[miss])
            print("You hung the man to death.")
            break

if __name__ == "__main__":
    main()

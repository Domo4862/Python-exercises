# Coded by Domo4862
# Random number generation
# Accepts input for highest number limit

from random import randint

limit = 0


# Prompt for highest limit of number generation
def main():
    global limit
    print("Insert highest limit for number generation")
    limit += int(input())
    generate()


# Define number generation
def generate():
    print("")
    print("Rolled:", randint(1, limit))
    print('Would you like to reroll?')
    print('Inputs are "y" or "n"')
    # Check input
    while True:
        x = input()
        if x != 'n' and x != 'y':
            print('Inputs are "y" or "n"')
        elif x == 'y':
            generate()
        elif x == 'n':
            break

if __name__ == "__main__":
    main()
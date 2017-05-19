# Coded by Domo 4862
# Guess my Number game
# Guess any number from 1 to 100 and receive tips if the number is higher or lower

from random import randint

def main():
    # Initialise number to guess
    guess = randint(1, 100)
    print('What\'s my number? (1-100)')

    # Counter for number of guess
    count = 0

# Check input
    while (True):
        x = int(input())
        count += 1
        if x < guess:
            print('Go higher!')
        elif x > guess:
            print('Go lower!')
        elif x == guess:
            print('You found me!')
            print("Guess Count:", count)
            break

if __name__ == '__main__':
    main()
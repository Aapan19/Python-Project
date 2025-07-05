from random import randint

while True:
    ask = input('Are you want to roll the dice?(y/n): ').lower()
    if ask == 'y':
        dice1 = randint(1,6)
        dice2 = randint(1,6)
        print()
        print(dice1,dice2)
        print()
    elif ask == 'n':
        print()
        print('Thank you for playing')
        break
    else:
        print()
        print('Invalid input! Enter a vlaid input')
        print()
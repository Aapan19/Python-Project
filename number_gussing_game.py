from random import randint

random_numb = randint(1,100)

while True:
    try:
        guess = int(input('Make a guess between 1 to 100:(0 to quit): '))

        if guess == 0:
            print()
            print('Thanks for playing')
            print('Quiting.......')
            break
        elif guess < random_numb:
            print()
            print('Too loww!: ')
            print()
        elif guess > random_numb:
            print()
            print('Too high!: ')
            print()
        else:
            print()
            print('Hurrey! You\'ve won')
            print()

    except ValueError:
        print('Invalid input, Enter a valid number within 1 to 100')

    
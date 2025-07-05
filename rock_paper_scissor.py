from random import choice

options = ('r', 'p', 's')
emojis = {
    'r': '🪨',
    's': '✂️',
    'p': '📃'}
while True:
    user_choice = input('Rock, Paper or Scissor(r,p,s): ').lower()
    if user_choice not in options:
        print('Invalid input! ')
        continue

    computer_choice = choice(options)

    print(f'You chose {emojis[user_choice]}')
    print(f'Computer choice {emojis[computer_choice]}') 

    if user_choice == computer_choice:
        print('Ties!')
    elif (
        (user_choice == 'r' and computer_choice == 's') or
        (user_choice == 's' and computer_choice == 'p') or
        (user_choice == 'p' and computer_choice == 'r')):
        print('You win! ')
    else:
        print('You loss!')

    continue_again = input('Play again?(y/n): ')
    if continue_again == 'n':
        print('Thanks for playing...')
        print('Quiting..........')
        break
class test:
    def __init__(self):
        pass
    
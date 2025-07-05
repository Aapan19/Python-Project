from random import choice

ROCK = 'r'
PAPER = 'p'
SCISSOR = 's'
emojis ={ROCK: '🪨', SCISSOR: '✂️', PAPER: '📃'}
options = tuple(emojis.keys())

def get_user_choice():
    while True:
        user_choice = input('Rock, Paper or Scissor(r,p,s): ').lower()
        if user_choice in options:
            return user_choice
        else: 
            print('Invalid input! ')

def display_choices(user_choice, computer_choice):
    print(f'You chose {emojis[user_choice]}')
    print(f'Computer choice {emojis[computer_choice]}') 

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print('Ties!')
    elif (
        (user_choice == ROCK and computer_choice == SCISSOR) or
        (user_choice == SCISSOR and computer_choice == PAPER) or
        (user_choice == PAPER and computer_choice == ROCK)):
        print('You win! ')
    else:
        print('You loss!')

def play_game():
    while True:
        user_choice = get_user_choice()
        computer_choice = choice(options)

        display_choices(user_choice, computer_choice)

        determine_winner(user_choice, computer_choice)

        continue_again = input('Play again?(y/n): ')
        if continue_again == 'n':
            print('Thanks for playing...')
            print('Quiting..........')
            break

play_game()
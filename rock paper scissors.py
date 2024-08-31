import random

def play_game():
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)

    user_choice = input('Enter your choice (rock, paper, scissors): ')
    while user_choice not in choices:
        user_choice = input('Invalid choice. Enter again (rock, paper, scissors): ')

    print(f'\nComputer chose: {computer_choice}')
    print(f'You chose: {user_choice}\n')

    if user_choice == computer_choice:
        print(f'Both players selected {user_choice}. It\'s a draw !')
    elif user_choice == 'rock':
        if computer_choice == 'scissors':
            print('Rock smashes scissors! You win!')
        else:
            print('Paper covers rock! You lose.')
    elif user_choice == 'paper':
        if computer_choice == 'rock':
            print('Paper covers rock! You win!')
        else:
            print('Scissors cuts paper! You lose.')
    elif user_choice == 'scissors':
        if computer_choice == 'paper':
            print('Scissors cuts paper! You win!')
        else:
            print('Rock smashes scissors! You lose.')

play_game()

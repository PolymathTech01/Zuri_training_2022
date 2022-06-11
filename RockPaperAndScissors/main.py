

from random import choice

choices = ['R', 'P', 'S']

cpu_choice = choice(choices).upper()
print('this is cpu choice', cpu_choice)

player_choice = input(
    "Please input either:\nR for scissors\nP for paper\nS for scissors\n").upper()
print(player_choice)


def game_choice_interpretation(choice):
    if choice == 'R':
        choice_interpretation = 'Rock'
    elif choice == 'P':
        choice_interpretation = 'Paper'
    elif choice == 'S':
        choice_interpretation = 'Scissors'
    else:
        choice_interpretation = 'Invalid option pls try again'

    return choice_interpretation


while True:
    player_interpretation = game_choice_interpretation(player_choice)
    print("player choice is: ", player_interpretation)
    cpu_interpretation = game_choice_interpretation(cpu_choice)
    print('computer choice is: ', cpu_interpretation)
    choices_dict = {'player': player_interpretation, 'cpu': cpu_interpretation}
    player = True
    if player_interpretation != cpu_interpretation and player:

        if player_interpretation == 'Scissors':
            if cpu_interpretation == 'Paper':
                print("player wins")
            elif cpu_interpretation == 'Rock':
                print('computer wins')
        elif cpu_interpretation == 'Scissors':
            if player_interpretation == 'paper':
                print('computer wins')
            elif player_interpretation == 'Rock':
                print('player wins')
        elif player_interpretation == 'Paper':
            if cpu_interpretation == 'Rock':
                print('player wins')
            elif cpu_interpretation == 'Scissors':
                print('computer winssssssssss')
        elif cpu_interpretation == 'Paper':
            if player_interpretation == 'Rock':
                print('computer wins')
            elif player_interpretation == 'Scissors':
                print('player wins')
        player = False
        break
    else:
        print('it is a tie!, you will have to play again')
        player_interpretation = game_choice_interpretation(player_choice)
        print("player choice is: ", player_interpretation)
        cpu_interpretation = game_choice_interpretation(cpu_choice)
        print('computer choice is: ', cpu_interpretation)
        choices_dict = {'player': player_interpretation,
                        'cpu': cpu_interpretation}
        player = True
        break

#    scripts.py


# import the utils module
import utils

print('Starting the Rock Paper Scissors game!')
player_name = input('Please enter your name: ')

print('Pick a hand: (0: Rock, 1: Paper, 2: Scissors)')
player_hand = int(input('Please enter a number (0-2): '))

# Call the validate function of utils module
if utils.validate(player_hand):
    computer_hand = 1
    
    # Call the print_hand function of utils module
    utils.print_hand(player_hand, player_name)
    utils.print_hand(computer_hand, 'Computer')
    
    # Call the judge function of utils module
    result = utils.judge(player_hand, computer_hand)
    print('Result: ' + result)
else:
    print('Please enter a valid number')

    
    
#    utils.py



def validate(hand):
    if hand < 0 or hand > 2:
        return False
    return True

def print_hand(hand, name='Guest'):
    hands = ['Rock', 'Paper', 'Scissors']
    print(name + ' picked: ' + hands[hand])

def judge(player, computer):
    if player == computer:
        return 'Draw'
    elif player == 0 and computer == 1:
        return 'Lose'
    elif player == 1 and computer == 2:
        return 'Lose'
    elif player == 2 and computer == 0:
        return 'Lose'
    else:
        return 'Win'

      
      

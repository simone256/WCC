import random
#                                        J   Q   K   A
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

random.shuffle(cards)

#print(cards) # To see the list after being shuffled

# Round 1
player_card1 = cards.pop()
computer_card1 = cards.pop()
#print(cards) # To see the list after two cards have been popped off.
print('Player card: ' + str(player_card1))
print('Computer card:  ' + str(computer_card1))

# Round 2
decision = raw_input('\nIf you want to stay type `s`, if you want to hit type `h`: ')

if decision == 'h':
    player_card2 = cards.pop()
else:
    player_card2 = 0

computer_card2 = cards.pop()

print('Player cards: ' + str(player_card1) + ', ' + str(player_card2))
print('Computer cards: ' + str(computer_card1) + ', ' + str(computer_card2))

# Round 3
decision = raw_input('\nIf you want to stay type `s`, if you want to hit type `h`: ')

if decision == 'h':
    player_card3 = cards.pop()
else:
    player_card3 = 0

computer_score = computer_card1 + computer_card2

if computer_score < 16:
    computer_card3 = cards.pop()
else:
    computer_card3 = 0

print('Player cards: ' + str(player_card1) + ', ' + str(player_card2) + ', ' + str(player_card3))
print('Computer cards: ' + str(computer_card1) + ', ' + str(computer_card2) + ', ' + str(computer_card3))

#Results

print('\nGame over!')

final_player_score = player_card1 + player_card2 + player_card3
final_computer_score = computer_card1 + computer_card2 + computer_card3

if final_player_score > 21 and final_computer_score > 21:
    print('Tie - both player and computer busted')
elif final_player_score == final_computer_score:
    print('Tie')
elif final_computer_score > 21:
        print('Player won! Computer busted.')
elif final_player_score > 21:
    print('Computer won! Player busted.')
elif final_player_score > final_computer_score:
    print('Player won! Closest to 21.')
else:
    print('Computer won! Closest to 21.')

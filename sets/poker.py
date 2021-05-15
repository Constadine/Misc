from random import seed
from random import randrange
from datetime import datetime


seed(datetime.now())


kind = {'heart', 'diamond', 'club', 'spades'}
number = {'ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'jack', 'queen', 'king'}

deck = set()

deck = {(k, n) for k in kind for n in number}


p1 = set()
p2 = set()

deck_list = list(deck)


def draw_card(player):
    draw = randrange(0, len(deck_list))
    player.add(deck_list.pop(draw))


for _ in range(5):
    draw_card(p1)
    draw_card(p2)


def aces(player):
    cnt = 0
    for card in player:
        if card[1] == 'ace':
            cnt += 1
    if cnt == 4:
        print(f'Player has 4 of aces!')


aces(p1)
aces(p2)


def kenta(player):
    hand_numbers = []
    for card in player:
        if card[1] == 'ace':
            hand_numbers.append(1)
        elif card[1] == 'jack':
            hand_numbers.append(11)
        elif card[1] == 'queen':
            hand_numbers.append(12)
        elif card[1] == 'king':
            hand_numbers.append(13)
        else:
            hand_numbers.append(card[1])

    hand_numbers.sort()
    for pos in range(4):
        if hand_numbers[pos] != hand_numbers[pos+1] - 1:
            break
    else:
        print("Player has kenta!")


print('player1:' + str(p1))
print('player2:' + str(p2))


kenta(p1)
kenta(p2)

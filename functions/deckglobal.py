from random import seed
from random import randrange
from datetime import datetime


def player1_pick():
    player1.add(deck.pop())


def player2_pick():
    player2.add(deck.pop())


def play():
    print("START")
    for _ in range(len(deck)):
        if randrange(2) == 0:
            player1_pick()
        else:
            player2_pick()
    print(f"Player 1: {len(player1)}")
    print(f"Player 2: {len(player2)}")
    if len(player1) > len(player2):
        print("Player1 wins")
    elif len(player1) == len(player2):
        print("Draw")
    else:
        print("Player2 wins")


seed(datetime.now())


kind = {'heart', 'diamond', 'club', 'spades'}
number = {'ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'jack', 'queen', 'king'}


deck = {(k, n) for k in kind for n in number}
print(deck)
player1 = set()
player2 = set()

play()

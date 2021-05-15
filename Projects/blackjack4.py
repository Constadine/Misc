from random import seed
from random import randrange
from datetime import datetime


kind = {'heart', 'diamond', 'club', 'spades'}
number = {'ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'jack', 'queen', 'king'}

deck = set()

deck = {(k, n) for k in kind for n in number}
deck_list = list(deck)


# functions
def hand_value(hand):
    s = 0
    for card in hand:
        if card[1]


def main():
    seed(datetime.now())


# main
main()

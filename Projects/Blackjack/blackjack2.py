from random import seed
from random import randrange
from datetime import datetime

seed(datetime.now())


kind = {'heart', 'diamond', 'club', 'spades'}
number = {'ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'jack', 'queen', 'king'}

deck = set()

deck = {(k, n) for k in kind for n in number}
deck_list = list(deck)


human = []
computer = []


def draw_card(player):
    draw = randrange(0, len(deck_list))
    player.append(deck_list.pop(draw))
    print(human)


def starting_hand(player):
    for _ in range(2):
        draw_card(player)


def hand_value(player):
    card = player[len(player) - 1]
    if card[1] == 'ace':
        while True:
            try:
                ace_choice = int(input("Got an ace, 1 or 11?: "))
                break
            except:
                print("Wrong input. Choices 1 or 11")
        return ace_choice
    elif card[1] == 'jack' or card[1] == 'queen' or card[1] == 'king':
        return 10
    else:
        return card[1]


def main():
    human_count = 0
    starting_hand(human)
    if 'ace' in human and human_count < 12:
        while True:
            try:
                ace_choice = int(input("Got an ace, 1 or 11?: "))
                break
            except:
                print("Wrong input. Choices 1 or 11")
        human_count += ace_choice
    elif 'ace' in human and human_count >= 12:
        human_count += 1

    print(f"Hand: {human}")
    print(f"You're at {human_count}. Continue?")


main()

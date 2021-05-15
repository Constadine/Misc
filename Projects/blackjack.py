from random import seed
from random import randrange
from datetime import datetime


kind = {'heart', 'diamond', 'club', 'spades'}
number = {'ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'jack', 'queen', 'king'}

deck = set()

deck = {(k, n) for k in kind for n in number}


computer = set()


def draw_card(player):
    player.add(deck.pop())


def starting_hand(player):
    for _ in range(2):
        draw_card(player)


def hand_value(player):
    cnt = 0
    ace = False
    for card in player:
        n = card[1]
        if n == 'ace':
            cnt += 1
            ace = True
        elif n == 'jack' or n == 'queen' or n == 'king':
            cnt += 10
        else:
            cnt += n
    if ace:
        if cnt + 10 <= 21:
            cnt += 10

    return cnt


def main():
    seed(datetime.now())

    human = set()

    starting_hand(human)
    print(f"Hand: {human}")
    while not input(f"You're at: {hand_value(human)}. Continue? (y/n): ") == "n":
        human_final = 0
        draw_card(human)
        if hand_value(human) == 21:
            print("21! You win!")
            human_final = hand_value(human)
            print(human)
            break
        elif hand_value(human) > 21:
            print(f"You're at ({hand_value(human)}). You lost!")
            print(human)
            break
        print(human)
    else:
        human_final = hand_value(human)
        print(f"Hand: {human}")
        print(f"Final cnt: {human_final}")

    # starting_hand(computer)


main()

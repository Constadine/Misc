from random import seed
from random import randrange
from datetime import datetime

seed(datetime.now())


kind = {'heart', 'diamond', 'club', 'spades'}
number = {'ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'jack', 'queen', 'king'}

deck = set()

deck = {(k, n) for k in kind for n in number}
deck_list = list(deck)


human_hand = []
computer_hand = []


def draw_card(player):
    draw = randrange(0, len(deck_list))
    player.append(deck_list.pop(draw))
    print(human_hand)


def check_ace_cheat(player):
    if hand_value(player) == 11:
        return True


def hand_value(player):
    cnt = 0
    card = player[len(player) - 1]
    if card[1] == 'ace':
        while True:
            try:
                ace_choice = int(input("Got an ace, 1 or 11?: "))
                if ace_choice == 1:
                    cnt += 1
                    break
                elif ace_choice == 11:
                    cnt += 11

                    break
                else:
                    print("Choose 1 or 11")
            except:
                print("Wrong input. Choices 1 or 11")
    elif card[1] == 'jack' or card[1] == 'queen' or card[1] == 'king':
        cnt += 10
    else:
        cnt += card[1]
    return cnt


def main():
    human_count = 0
    ace_cheat = False
    for _ in range(2):
        draw_card(human_hand)
        human_count += hand_value(human_hand)
        if hand_value(human_hand) == 11:
            ace_cheat = True

    while human_count < 22:
        if input(f"You're at: {human_count}. Continue? (y/n): ").lower() == "n":
            break
        else:
            if hand_value(human_hand) == 11:
                ace_cheat = True
            if human_count < 21:
                draw_card(human_hand)
                human_count += hand_value(human_hand)
            elif human_count == 21:
                print("Wow, 21! You won!")
                break
            if human_count > 21:
                print(f"You're at {human_count}. You lost!")
                break
            elif (human_count > 21) and ('ace' in human_hand) and not ace_cheat:
                human_count -= 10
                print(f"You turned your ace from 11 to 1")
                draw_card(human_hand)
                human_count += hand_value(human_hand)
    else:
        print(f"Human hand: {human_hand}")
        print(f"Human stopped at {human_count}")


main()

kind = {'heart', 'diamond', 'club', 'spades'}
number = {'ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'jack', 'queen', 'king'}

deck = set()
deck = {(k, n) for k in kind for n in number}

# functions


def hand_value(hand):
    cnt = 0
    ace = False
    for card in hand:
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


def player(hand):
    for _ in range(2):
        hand.add(deck.pop())

    while True:
        print(hand)
        print(f"You're at {hand_value(hand)}")
        choice = input("H-Hit or S-Stand: ").lower()
        if choice == "h":
            hand.add(deck.pop())
            value = hand_value(hand)
            if value >= 21:
                return value
        elif choice == "s":
            return hand_value(hand)


def computer(value_player, hand):
    for _ in range(2):
        hand.add(deck.pop())

    while True:
        value = hand_value(hand)

        if value >= 21:
            return value
        elif value >= value_player:
            return value
        else:
            hand.add(deck.pop())


# main


def main():
    rounds = 0
    player_score = 0
    computer_score = 0
    while True:

        player_hand = set()

        player_value = player(player_hand)

        print(f"{player_hand} with value {player_value}")
        if player_value == 21:
            print("21! Player won!")
            player_score += 1
        elif player_value > 21:
            print("You lost.")
            computer_score += 1
        else:
            print("Computer plays")
            computer_hand = set()
            computer_value = computer(player_value, computer_hand)
            print(computer_hand)
            if computer_value > 21:
                print("Computer is over 21. Player wins")
                player_score += 1
            else:
                print(f"Computer wins with {computer_value}")
                computer_score += 1
        rounds += 1
        print(f"""
        Round: {rounds} | Score:
        ======================================================
                | Player: {player_score}       Computer: {computer_score}
        """)
        if input("Play another round? (y/n): ") == "n":
            print("Thanks for playing!")
            break


# gia na kanei ananeosi to deck prepei na ginei olo to programma me lists.
main()

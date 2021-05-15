import random
import time


def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True


def play():
    user = input("'r' for rock, 'p' for paper, 's' for scissors. Choose: ")

    computer = random.choice(['r', 'p', 's'])

    print("Computer is choosing...")
    time.sleep(1.5)

    if computer == 'r':
        print(f'..and chose ROCK.')
    elif computer == 'p':
        print(f'..and chose PAPER.')
    else:
        print(f'..and chose SCISSORS.')

    time.sleep(0.5)

    if user == computer:
        return "It's a tie"
    elif is_win(user, computer):
        return "You won!"

    return 'You lost..'


def main():
    while True:
        print(play())


if __name__ == '__main__':
    main()

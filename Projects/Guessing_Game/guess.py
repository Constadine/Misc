import random


def guess(x):
    random_number = random.randint(1, x)
    guess = int(input(f'Guess a number between 1 and {x}: '))
    while guess != random_number:
        if guess < random_number:
            guess = int(input(f'Sorry, you guessed too low. Guess again: '))
        else:
            guess = int(input(f'Sorry, you guessed too high. Guess again: '))

    print('Good job!')


# Computer Guessing

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(
            (f'Was {guess} too high (H), too low (L) or correct (C): ')).lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print('Yay, boiii. Found it.')


computer_guess(20)

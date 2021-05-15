import random

hidden = []
state = []

N = 12

found = 0
tries = 0
best_score = 1000
active = True


# ohh
exclude = []
for card in range(N):
    x = random.randint(1, N/2)
    while x in exclude:
        x = random.randint(1, N/2)
    hidden.append(x)
    if hidden.count(x) == 2:
        exclude.append(x)
# YEAHHHHH!

for i in range(N):
    state.append('closed')

while active:
    tries += 1
    # read 1st position
    first_position = int(
        input(f'Give first position (1-{N}) and closed: ')) - 1
    while (first_position < 0 or first_position > N) or state[first_position] == 'open':
        print('Error!')
        first_position = int(
            input(f'Give first position (1-{N}) and closed: ')) - 1
        # read 2nd position
    second_position = int(
        input(f'Give second position (1-{N}) and closed: ')) - 1
    while (second_position < 0 or second_position > N) or state[second_position] == 'open' or second_position == first_position:
        print('Error!')
        second_position = int(
            input(f'Give second position (1-{N}) and closed: ')) - 1
    # change state: both temp_open
    state[first_position] = "temp_open"
    state[second_position] = "temp_open"

    # print currect state
    print('')

    for position in range(N):
        if state[position] == 'closed':
            print("_", end='')
        elif state[position] == 'open':
            print(hidden[position], end='')
        else:
            print(hidden[position], end='')

    print('')

    # check if same open, else closed
    if hidden[first_position] == hidden[second_position]:
        state[first_position] = 'open'
        state[second_position] = 'open'
        print("Success")
        found += 2
        if found == N:
            replay = input(
                f'Bravo. Game finished after {tries} tries! If you want to continue press "Y" or else "N": ').lower()
            if replay == 'n':
                active = False
            else:
                if tries < best_score:
                    best_score = tries
                print(f'Best score is {best_score}')
                state = ['closed', 'closed', 'closed', 'closed',
                         'closed', 'closed', 'closed', 'closed']
                found = 0
                tries = 0

    else:
        state[first_position] = 'closed'
        state[second_position] = 'closed'
        print("Failure")

    # print currect state
    print('')

    for position in range(N):
        if state[position] == 'closed':
            print("_", end='')
        elif state[position] == 'open':
            print(hidden[position], end='')
        else:
            print(hidden[position], end='')

    print('')

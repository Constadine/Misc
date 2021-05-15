import random

dices = {}

for i in range(6):
    dices[i+1] = 0

N = 1000

for rolls in range(N):
    roll = random.randint(1, 6)
    dices[roll] += 1


for i in range(6):
    print(f'{str(i+1)}: {str(dices[i+1]/N)}')

# 1η περίπτωση
my_list = []
for number in range(3):
    my_list.append(number)

# γίνεται : 

my_list = [number for number in range(3)]

# ===================

# 2η περίπτωση
my_list = []
for number in range(10):
    if number % 2 == 0:
        my_list.append(number)

# γίνεται : 

my_list = [number for number in range(10) if number%2 == 0]

# ===================

# 3η περίπτωση

my_list = []
for number in range(10):
    if number % 2 == 0:
        my_list.append(number)
    else:
        my_list.append(number/2)

# γίνεται : 

my_list = [number if number%2 == 0 else number/2 for number in range(10)]
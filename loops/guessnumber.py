secret_Number = 5
max_tries = 5

ans = int(input("Guess the secret number: "))
tries = 1
while ans != secret_Number:
    print(f"You have {max_tries-tries} lives left.")
    if ans < secret_Number:
        ans = int(input("Guessed too low. Try again: "))
    else:
        ans = int(input("Guessed too high. Try again: "))
    tries +=1 
    if tries == max_tries:
        replay = input("Out of lives. If you want to try again press 'Y', to quit 'N': ")
        if replay == "Y":
            tries = 0
            continue
        elif replay =="N":    
            break
else: 
    print("Good job!")

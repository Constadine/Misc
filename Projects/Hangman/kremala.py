import random

words = [
    "wash",
    "invite",
    "apology",
    "displace",
    "assessment",
    "colorful",
    "employee",
    "slippery",
    "rescue",
    "reality",
    "sustain",
    "liberal",
    "crackpot",
    "sympathetic",
    "disco"
]


hidden_word = words[random.randint(0, len(words) - 1)]

# δεν χρειαζοταν να τα περασω σε λιστα. ετρεχα for char in hidden_word... FAIL
letters = list(hidden_word)
guessed_letters = []
state = ["closed" for i in range(len(letters))]
max_tries = 5


while len(letters) != len(guessed_letters):
    for position in range(len(letters)):
        if state[position] == "closed":
            print("_", end="")
        elif state[position] == "open":
            print(letters[position], end="")
    guess = (input("\nGive a letter: ")).lower()
    while (not guess.isalpha()) or (len(guess) > 1):
        guess = (input("\nOnly one LETTER please: ")).lower()

    if guess in guessed_letters:
        print("You have already guessed this letter. Try again")
    elif guess in letters:
        guessed_letters.append(guess)
        state[letters.index(guess)] = "open"
        rep = letters.count(guess)
        print(f'"{guess}" exists {rep} times')
        if rep > 1:
            for i in range(rep - 1):
                guessed_letters.append(guess)
            for i in range(0, len(letters)):
                if guess == letters[i]:
                    state[i] = "open"
    else:
        max_tries -= 1
        if max_tries == 0:
            print("You are dead.")
            break
        else:
            print(f"Try again. You have {max_tries} more lives.")


else:
    print(f'\nYour word was "{hidden_word}". Good job!')

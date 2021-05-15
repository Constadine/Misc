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

letters = list(hidden_word)
letters_dic = {}
for i in range(len(letters) - 1):
    letters_dic[i] = letters[i]
print(letters_dic)

# for key, value in letters_dic.items():
while True:
    guess = input("Guess a letter: ")
    x = 0
    for key in letters_dic.keys():
        if letters_dic[key].count(guess):
            x += 1
            print(x)

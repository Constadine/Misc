import random
import time

choices = ["rock", "scissors", "paper"]
score = {
    "player": 0,
    "computer": 0
}

round_history = {}


def result():
    if player_input == "rock":
        if computer_random == "rock":
            return "Tie"
        elif computer_random == "paper":
            return "Computer won this round."
        else:
            return "Player won this round."
    elif player_input == "paper":
        if computer_random == "paper":
            return "Tie"
        elif computer_random == "scissors":
            return "Computer won this round."
        else:
            return "Player won this round."
    else:
        if computer_random == "paper":
            return "Player won this round."
        elif computer_random == "scissors":
            return "Tie"
        else:
            return "Computer won this round."


rounds = 0
while score["player"] < 3 and score["computer"] < 3:
    rounds += 1
    print("Round:" + str(rounds))
    computer_random = choices[random.randint(0, 2)]
    player_input = input("Choose: ")
    while player_input not in choices:
        print("Wrong input. Choices: rock, scissors, paper")
        player_input = input("Choose: ")
    print(f"Computer: {computer_random}")
    time.sleep(0.5)
    print(result())
    if result() == "Player won this round.":
        score["player"] += 1
    elif result() == "Computer won this round.":
        score["computer"] += 1

    round_history[f"Round {rounds}"] = f'Player: {player_input}, Computer: {computer_random}, Score: {score["player"]} - {score["computer"]}'
    print(score)
    print("==============================")
else:
    if score["player"] == 3:
        print("Gave over. Player won!")
    else:
        print("Gave over. Computer won!")
print(round_history)

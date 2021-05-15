import random
from random import seed
from datetime import datetime


# score
player1_score = [["ones", 0, "open"], ["twos", 0, "open"], ["threes", 0, "open"],
                 ["fours", 0, "open"], ["fives", 0, "open"], ["sixes", 0, "open"]]
player2_score = [["ones", 0, "open"], ["twos", 0, "open"], ["threes", 0, "open"],
                 ["fours", 0, "open"], ["fives", 0, "open"], ["sixes", 0, "open"]]


def roll_dices(dice_kept):
    dices_on_board = [random.randint(1, 6) for _ in range(dice_kept)]

    return sorted(dices_on_board)


def select_points(dices_on_board, player_hand, player_score):
    print(player_hand, dices_on_board)
    while True:
        while True:
            score_choice = input("What sum do you want to keep? (1-6): ")
            if not score_choice.isdigit():
                print("Press a number 1-6!")
            else:
                score_choice = int(score_choice)
                break
        if score_choice < 0 or score_choice > 6 or player_score[score_choice - 1][2] == "closed":
            print("Choose between 1-6 and a number you haven't already chosen!")
        elif (score_choice not in player_hand) and (score_choice not in dices_on_board):
            zero_points_choice = input(
                f"Do you want to give a zero on {score_choice}? y/n: ")
            while not zero_points_choice.isalpha():
                zero_points_choice = input("Please answer with a y or n")
            if zero_points_choice.lower() == "y":
                player_score[score_choice - 1][2] = "closed"
                break
            elif zero_points_choice.lower() == "n":
                pass
        else:
            for i in range(0, 6):
                if (score_choice - 1) == i:
                    player_score[i][1] += (score_choice*(player_hand.count(score_choice) +
                                                         dices_on_board.count(score_choice)))
                    player_score[i][2] = "closed"
            break


def manage_player_hand(player_hand, player_score):

    for roll in range(3):
        dice_kept = 5 - len(player_hand)
        dices_on_board = roll_dices(dice_kept)
        while True:
            print(f"Board: {dices_on_board}")
            print(f"Hand: {player_hand}")

            pick_discard_dice = input(
                '"p" - pick, "d" - discard, "f" - finished: ')
            if pick_discard_dice.isalpha():

                if pick_discard_dice == "p":

                    while dices_on_board:
                        print(f"Board: {dices_on_board}")
                        print(f"Your hand: {player_hand}")

                        choose_dice = input(
                            f"From 1 - {len(dices_on_board)} choose the dice you want to pick: ('f' - finished): ")
                        if choose_dice == "f":
                            break
                        else:
                            if not choose_dice.isdigit() or int(choose_dice) > len(dices_on_board) or int(choose_dice) < 0:
                                print("Wrong input")
                            else:
                                temp = dices_on_board.pop(int(choose_dice) - 1)
                                player_hand.append(temp)
                    else:
                        print("There are no dices on dices_on_board")
                elif pick_discard_dice == "d":
                    while player_hand:
                        print(f"Your hand: {player_hand}")
                        choose_dice = (input(
                            f"From 1 -{len(player_hand)} choose the dice you want to discard: ('f' - finished): "))

                        if choose_dice == "f":
                            break
                        else:
                            if not choose_dice.isdigit() or int(choose_dice) > len(player_hand) or int(choose_dice) < 0:
                                print("Wrong input!")
                            else:
                                temp = player_hand.pop(int(choose_dice) - 1)
                                dices_on_board.append(temp)
                    else:
                        print("No dices on hand")
                elif pick_discard_dice == "f":
                    break
                else:
                    print("Wrong input!")
            else:
                print("Wrong input")
        select_points(dices_on_board, player_hand, player_score)
        return player_hand


def print_final_score():
    player1_total_score = 0
    player2_total_score = 0
    for i in range(6):
        player1_total_score += player1_score[i][1]
        player2_total_score += player2_score[i][1]
    print(f"Player 1: {player1_total_score} - Player 2: {player2_total_score}")
    if player1_total_score > player2_total_score:
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")


def print_scores():
    print(f"Player 1 score: {player1_score}")
    print(f"Player 2 score: {player2_score}")

def main():
    seed(datetime.now())

    for i in range(6):

      # player1 plays
        p1 = []
        print("-"*15)
        print("Player 1 plays!")

        manage_player_hand(p1, player1_score)
        print_scores()

        # player2 plays
        p2 = []
        print("-"*15)
        print("Player 2 plays!")

        manage_player_hand(p2, player2_score)
        print_scores()

    print_final_score()


main()

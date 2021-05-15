from random import randrange

from character import Character


class Arena:
    def __init__(self, team_A, team_B):
        self.team_A = team_A
        self.team_B = team_B

    def print_state(self):
        print("TEAM A")
        for character in self.team_A:
            character.print()
        print("-"*15)
        print("TEAM B")
        for character in self.team_B:
            character.print()
        print("-"*15)

    def play(self):
        time = -1

        while True:
            time += 1
            print("=" * 20)
            print("Time = " + str(time))
            print("=" * 20)
            self.print_state()

            chars_to_play = []
            for character in self.team_A:
                if character.delay == 0:
                    chars_to_play.append(('A', character))
            for character in self.team_B:
                if character.delay == 0:
                    chars_to_play.append(('B', character))

            for character in chars_to_play:
                attacking = character[1]
                if character[0] == 'A':
                    defending = self.team_B[randrange(len(self.team_B))]
                else:
                    defending = self.team_A[randrange(len(self.team_A))]

                damage = attacking.attack()
                defending.health -= damage
                print(
                    f"{attacking.character_name} dealt {damage} to {defending.character_name}")

            for pos in range(len(self.team_A)-1, -1, -1):
                if self.team_A[pos].is_dead():
                    print(f"{self.team_A[pos].character_name} is dead!")
                    self.team_A.pop(pos)
            for pos in range(len(self.team_B)-1, -1, -1):
                if self.team_B[pos].is_dead():
                    print(f"{self.team_B[pos].character_name} is dead!")
                    self.team_B.pop(pos)

            if len(self.team_A) == 0:
                print("Team B won!")
                break
            elif len(self.team_B) == 0:
                print("Team A won!")
                break

            for character in self.team_A:
                character.end_round()
            for character in self.team_B:
                character.end_round()

            input("Press Enter to Continue")

import random
import time

class Die:
    def __init__(self, sides):
        self.sides = sides
        self.value = self.roll()

    def roll(self):
        self.value = random.randint(1, self.sides)
        return self.value

    def get_value(self):
        return self.value

def reroll(Dice, *reroll_indices):
    if len(reroll_indices) == 0:
        print("No dice rerolled")
    else:
        for index in reroll_indices:
            if 1 <= index <= 3:
                Dice[index - 1].roll()
            else:
                print(f"Invalid input: {index}")

def main():
    try:
        while True:
            print("Welcome to the dice game!")

            Dice = [Die(6), Die(6), Die(6)]
            for die in Dice:
                print(f"Die roll: {die.get_value()}")
            total_before = Dice[0].get_value() + Dice[1].get_value() + Dice[2].get_value()
            print(f"Total: {total_before}")

            while True:
                try:
                    reroll_input = input("Enter the dice you would like rerolled (1-3) as a comma-separated list, or leave blank: ")
                    if reroll_input == "":
                        reroll_indices = []
                    else:
                        reroll_indices = [int(x) for x in reroll_input.split(',')]
                    break
                except ValueError:
                    print("Invalid input")

            reroll(Dice, *reroll_indices)
            for die in Dice:
                print(f"Die roll: {die.get_value()}")
            total_after = Dice[0].get_value() + Dice[1].get_value() + Dice[2].get_value()
            print(f"Final Total: {total_after}")

            if total_after > total_before:
                print("You win!")
            elif total_after == total_before:
                print("Draw!")
            else:
                print("You lose!")
            time.sleep(5)
    except KeyboardInterrupt:
        print("\nGoodbye!")
    
if __name__ == "__main__":
    main()

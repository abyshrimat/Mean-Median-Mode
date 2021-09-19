import random

number = random.randint(1,9)

chances = 0

while chances < 5:

    guess = input("enter your Guess")

    if guess == number:
        print("congratulation YOU WON!!!!")
        break

        chances = chances + 1

    if not chances < 5:
        print("you Lose the number Is: ", number)
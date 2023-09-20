import random
import art

numbers_list = list(range(1, 101))
chosen_number = random.choice(numbers_list)
chances = 10


def welcome():
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
# print(f"Pssst, the correct number is {chosen_number}")


def choose_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "hard":
        return chances - 5
    else:
        return chances


welcome()
chances = choose_difficulty()
game_over = False

while chances > 0 and not game_over:
    print(f"You have {chances} attempts remaining to guess the number.")
    user_number = int(input("Make a guess: "))
    chances -= 1
    if user_number > chosen_number and user_number < 101:
        print("Too high.")
        if chances > 0:
            print("Guess again.")
    elif user_number < chosen_number and user_number > 0:
        print("Too low.")
        if chances > 0:
            print("Guess again.")
    elif user_number == chosen_number:
        print(f"You got it. The answer was {chosen_number}.")
        game_over = True
    elif user_number > 100 or user_number < 0:
        print("Stick to numbers between 1 and 100.")


if chances == 0:
    print("You've run out of guesses, you lose.")


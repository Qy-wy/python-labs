import random

def guess_the_number():
    number = random.randint(1, 100)
    guesses = 0
    guess = 0
    while guess != number:
        guesses += 1
        guess = int(input("Guess the number: "))
        if guess < number:
            print("Too low")
        elif guess > number:
            print("Too high")
        else:
            print(f"You guessed it in {guesses} guesses")

guess_the_number()
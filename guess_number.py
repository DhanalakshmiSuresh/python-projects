import random

number = random.randint(1, 20)
attempts = 0

print("Guess a number between 1 and 20")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print(f"🎉 Correct! You guessed it in {attempts} attempts.")
        break
import random

def number_guesser():
    number = random.randint(1, 10)
    tries = 0

    while True:
        try:
            guess = int(input("Guess a number between 1 and 10: "))
            tries += 1

            if guess < number:
                print("Too low!")
            elif guess > number:
                print("Too high!")
            else:
                print(f"Correct! You guessed it in {tries} tries.")
                break
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    number_guesser()

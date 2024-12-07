import random

def guess_the_number():
    random_number = random.randint(1,100)
    print("A number is chosen. Try to guess it.")
    while True:

        try:
            guess = int(input("Guess the number between 1 and 100: "))

            if guess > 100:
                print("Please enter a number <= 100")
                continue
            if guess < 1:
                print("Please enter a number >= 1")
                continue

            if guess > random_number:
                if guess-random_number >= 10:
                    print("Your guess is TOO HIGH!")
                else:
                    print("Close. But still HIGH!")
            elif guess < random_number:
                if random_number-guess >= 10:
                    print("Your guess is TOO LOW!")
                else:
                    print("Close. But still LOW!")
            else:
                print("Congrats! You guessed the number!")
                break

        except ValueError:
            print("Error! Please enter a valid number!")

            
guess_the_number()
import random

def Guess_num():
    secret_num = random.randint(1,100)
    num_guess = 0

    while True: 
        guess = int(input("Enter a number between 1 and 100"))
        num_guess += 1

        if guess < secret_num:
            print("Too low, try again!")
        elif guess > secret_num:
            print("Too high, try again!")
        else:
            print("Congratulations, you guessed the number in", num_guess, "guesses!")
            break

Guess_num()
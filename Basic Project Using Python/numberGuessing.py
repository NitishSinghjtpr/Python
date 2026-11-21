import random

def guess_number():
    c_number = random.randrange(1, 101)

    while True:
        userInput = int(input("Enter your number: "))

        if userInput > c_number:
            print("Your guess number is too high")

        elif userInput < c_number:
            print("Your guess number is too low")

        else:
            print("Congratulations! Your guess is correct.")
            break
        

guess_number()
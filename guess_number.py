import random

computer = random.randint(1, 100)
print("I'am thinking of a number between 1 and 100.")
total = 0

while True:

    user = int(input("Enter your guess: "))
    total += 1

    if user < computer:
        print("You have guessed it low.")
    
    elif user > computer:
        print("You have guessed it high.")

    else:
        print("You have guessed it correct.")
        print(f"You guessed the number in {total} attempt")
        break
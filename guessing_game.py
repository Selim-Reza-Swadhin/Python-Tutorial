import random  # all import

# from random import randint  # for randint

for x in range(1, 101):
    guessNumber = int(input("Enter your guess between 1 to 5 : "))

    randomNumber = random.random() * 100  # big number

    # randomNumber = random.randint(1, 5)  # small number
    # randomNumber = randint(1, 5)

    if guessNumber == randomNumber:
        print("You have won")
    else:
        print("You have lost")
        print("Random number was : ", randomNumber)

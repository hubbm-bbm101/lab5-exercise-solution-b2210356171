import random

mynum=random.randint(1,100)

guess=int(input("Guess the number: "))

while mynum!=guess:
    if mynum>guess:
        print("increase your number")
    else:
        print("decrease your number")
    guess = int(input("Guess the number: "))

print("You have found the number!")
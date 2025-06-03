import random
compChoice = random.randint(1,100)
attempts = 0
print("Guess the number...")

#1
while True:
    userChoice = int(input("Your Choice: "))
    attempts += 1
    if userChoice > compChoice:
        print("Guess smaller no.")
    elif userChoice < compChoice:
        print("Guess bigger no.")
    else:
        break
print(f"You Guessed the correct no. {compChoice} in {attempts} attempts")

#----------------------------------------------------------------------------------------------------------

#2
userChoice = None
while userChoice != compChoice:
    userChoice = int(input("Your Choice: "))
    attempts += 1
    if userChoice > compChoice:
        print("Guess smaller no.")
    elif userChoice < compChoice:
        print("Guess bigger no.")
    else:
        print(f"You Guessed the correct no. {compChoice} in {attempts} attempts")


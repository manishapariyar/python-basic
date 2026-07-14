import random

number = random.randint(1, 10)
tries = 0

while True:
    num = int(input("Enter a guess number: "))
    tries += 1

    if num == number:
        print("You guessed it right!")
        break
    else:
        print("Wrong guess. Try again!")

print(f"You took {tries} tries to guess the number.")

import random
number = random.randint(0,9)
print("It's a guess the number game so you have to guess a number between o to 9")
user = int(input("guess the number"))
if user == number:
    print("Hurray!!")
    print(f"you guessed the number right it's {number}")
if user != number:
    print(f"Your guess is incorrect the number is {number}")
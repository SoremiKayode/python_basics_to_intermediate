

# random_number = random.random()
import random


randint = random.randint(2, 5)
randrange = random.randrange(1, 2)
count = 0
print(randrange)
print("Guess any number between 2 to 5")
guessed_number = int(input())

while guessed_number != randint:
    count += 1
    print("You're wrong")
    guessed_number = int(input())
    if count == 2:
        break
if guessed_number == randint :
    print("You're Correct")



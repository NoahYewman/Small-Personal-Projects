#Guess the number
import random

random_num = random.randint(1,101)

#print(random_num) #debugging

guess = int(input("Guess the number between 1-100: "))

while guess!= random_num:

    if guess > random_num:
        print("Your guess is greater than the random number, guess again.")
        guess = int(input())
    elif guess < random_num:
        print("Your guess is less than the random number, guess again.")
        guess = int(input())

print("Congratulations, you guessed the number! It was", random_num,"!")

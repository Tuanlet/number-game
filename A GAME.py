#A GAME
import random


print('Hello what is your name?')
name = str(input())

print('well hello '+ name + ', I am thinking of a number between 1 and 50, can you guess in less than 10 tries?')
secretNumber = random.randint(1,50)

for guessesTaken in range(1,10):
    print('Take a guess.')
    guess = int(input())

    if guess > secretNumber:
        print('Your guess is too high!')
    elif guess < secretNumber:
        print('your guess is too low!')
    else :
        break #this condition is for the correct guess!


if guess == secretNumber:
    print('Good job '+name+ ' it took ' + str(guessesTaken) + ' to guess my number')
else:
    print('Nope, the number I was thinking of was' + str(secretNumber) + '!')



    




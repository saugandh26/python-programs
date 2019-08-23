import random

guessTaken = 0

myName= input("Hello Whats your name?")


number = random.randint(1,20)

print("Well " +myName+ ",I am thinking a number between 1 and 20")

while guessTaken<6:
    print("Take a guess")
    guess = int(input())
    guessTaken = guessTaken + 1


    if guess < number :
        print("You guess too low")
    if guess > number:
        print("You guess too high")
    if guess== number:
        break

if guess == number:
    guessTaken= str(guessTaken)
    print("Good job " + myName +"! You guessed the right number in " +guessTaken + "guesses!")

if guess != number:
    number = str(number)
    print('Nope. The nuber was ' +number)

    

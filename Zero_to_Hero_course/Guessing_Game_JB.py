# import needed libraries
from random import randint


#explain the game
print("Let's play a game! \nI am thinking of a number between 1 and 100. \nCan you guess what it is? \n")

#use the randomint library to generate a random number for the answer
answer = randint(0,101)

# Set a counter equal to zero so you can count the number of times someone guesses the correct number
counter = 1

#initiate a prompt to have someone guess a number between 1-100
guess = [input('Guess a whole number between 1-100 \n')]

#create a while loop. As long as the guess isn't the answer, the program will ask for another number to have guessed and will record the number of tries!
while int(guess[-1]) != answer:
    # if the counter is at zero, spit out a certain prompt (WARM!, COLD!, OUT OF BOUNDS!)
    if counter == 1:
        if int(int(guess[-1])) >= (answer - 10) and int(guess[-1]) <= (answer + 10):
            print("WARM! \n")
            counter += 1
        elif int(guess[-1]) < (answer - 10) or int(guess[-1]) > (answer + 10):
            print("COLD! \n")
            counter += 1
        elif int(guess[-1]) < 1 or int(guess[-1]) >100:
            print("OUT OF BOUNDS! \n")
            counter +=1
    #If the counter is more than zero (more than one number guesses) than answer with a different set of prompts (WARMER!, COLDER! OUT OF BOUNDS!, SAME NUBMER SILLY!)
    elif counter > 1:
        guess.append(input('Guess another whole number \n'))
        if int(guess[-1]) == answer:
            continue
        elif abs(int(guess[-1]) - answer) < abs(int(guess[-2]) - answer):
            print("WARMER! \n")
            counter += 1
        elif abs(int(guess[-1]) - answer) > abs(int(guess[-2]) - answer):
            print("COLDER! \n")
            counter += 1
        elif int(guess[-1]) < 1 or int(guess[-1]) >100:
            print("OUT OF BOUNDS! \n")
            counter +=1
        elif int(guess[-1]) == int(guess[-2]):
            print("That's the same number, silly! \n")

else:
    if counter == 1:
        print(f'Great job! You guessed the correct number in one try!')
    if counter > 1:
        print(f'Great job! You guessed the correct number in {counter} tries!')

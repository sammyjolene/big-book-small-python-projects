# Challenge from The Big Book of Small Python Projects, Al Sweigart
# In Bagels, a deductive logic game, you must guess a secret three-digit number based on clues. 
#The game offers one of the following hints in response to your guess: 
##“Pico” when your guess has a correct digit in the wrong place, 
##“Fermi” when your guess has a correct digit in the correct place, and 
##“Bagels” if your guess has no correct digits. 
#You have 10 tries to guess the secret number.

print("Bagels, a deductive logic game.")
print("By Al Sweigart al@inventwithpython.com")
print("I am thinking of a 3-digit number. Try to guess what it is.")
print("Here are some clues:")
print("When I say:    That means:")
print("  Pico         One digit is correct but in the wrong position.")
print("  Fermi        One digit is correct and in the right position.")
print("  Bagels       No digit is correct.")
print("I have thought up a number.")
print(" You have 10 guesses to get it.")

import random
from collections import defaultdict
#Create the answer using random and a dictionary. key is the location (1, 2 or 3) while value equals a rantom number between 0 and 9, inclusive.

answer = ''
for i in range(1, 4):
    answer += str(random.randint(0, 9))
playing = True
count =1

#get the input from a player
def check_guess(guess):
    hint = ''
    if guess[0] not in answer and guess[1] not in answer and guess[2] not in answer:
        hint += "Bagels "
        print(hint)
    elif guess == answer:
        print("You Win!")
        playing = False
        return playing
    else:
        if guess[0] == answer[0]:
            hint += "Fermi "
        elif guess[0] == answer[1]:
            hint += "Pico "
        elif guess[0] == answer[2]:
            hint += "Pico "
        if guess[1] == answer[1]:
            hint += "Fermi "
        elif guess[1] == answer[2]:
            hint += "Pico "
        elif guess[1] == answer[0]:
            hint += "Pico "
        if guess[2] == answer[2]:
            hint += "Fermi "
        elif guess[2] == answer[0]:
            hint += "Pico "
        elif guess[2] == answer[1]:
            hint += "Pico "
        print('hint: ', hint)

while playing == True:
    guess = input("Please choose a number between 0 and 999: ")
    if len(guess) == 1:
        guess = '00' + guess
    elif len(guess) == 2:
        guess = '0' + guess
    while str(guess).isnumeric() == False:
        guess = input("Sorry that was not a number, please choose again: ")
    if check_guess(guess) == False:
        print("Game Over")
        break
    elif count == 10:
        print("Sorry you ran out of guesses. The answer was ", answer)
    else:
        print('guess number: ', count)
        count += 1


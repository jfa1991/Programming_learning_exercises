# Ex 9

# Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether they guessed
# too low, too high, or exactly right.
# (Hint: remember to use the user input lessons from the very first exercise)

# Extras:
# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken,
# and when the game ends, print this out.


import random

numberToGuess = random.randint(1,20)
print('Homes I have a number in mind, try to guess it')
counter = 1
while True:
    numberGuessed = int(input('Go head: '))

    if numberGuessed > numberToGuess:
        print('Nope to high, try again')
        counter = counter + 1
    elif numberGuessed < numberToGuess:
        print('Nope to low, try again')
        counter = counter + 1
    else:
        print('Homes you got it, it took you ' + str(counter) + ' tries to guess it right')
        counter = 1
        question = input('Wanna stop guessing, type: Exit: ')
        if question != 'Exit':
            print('Aight lets keep guessing')
        else:
            print('All right')
            break
    


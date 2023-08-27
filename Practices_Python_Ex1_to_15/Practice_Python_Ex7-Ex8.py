
# Ex 7

# Let’s say I give you a list saved in a variable:
# a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
# Write one line of Python that takes this list a and
# makes a new list that has only the even elements of this list in it.

import random

listRandomNumber = []
evenList=[]

for i in range(1,random.randint(1,100)):
    listRandomNumber.append(random.randint(1,1000))
    listRandomNumber.sort()
print('List of random numbers: ' + str(listRandomNumber))

[evenList.append(i) for i in listRandomNumber if i % 2 == 0]
print('Sublist of random even numbers: ' + str(evenList))

# Ex 8

# Make a two-player Rock-Paper-Scissors game.
# (Hint: Ask for player plays (using input), compare them,
# print out a message of congratulations to the winner,
# and ask if the players want to start a new game)

import random

print('lets play Rock-Paper-Scissors game')

RPS = ['Rock !', 'Paper !', 'Scissors !']

print('Rock-Paper-Scissors !')

while True:
    choiceP1 = (random.choice(RPS))
    choiceP2 = (random.choice(RPS))
    print(choiceP1)
    print(choiceP2)

    if choiceP1 == choiceP2:
        print('Draw, Rock-Paper-Scissors !')
    elif choiceP1 == 'Rock !' and choiceP2 == 'Paper !':
        print('You won mothefucka')
        question= input('Wanna play again ? ')
        if question == 'Yes':
            print('Aight! lets do it! Rock-Paper-Scissors !')
        elif question == 'No':
            print('Ok, I got you, you afraid to loose')
            break
    elif choiceP1 == 'Rock !' and choiceP2 == 'Scissors !':
        print('I won mothefucka')
        question= input('Wanna play again ? ')
        if question == 'Yes':
            print('Aight! lets do it! Rock-Paper-Scissors !')
        elif question == 'No':
            print('Ok, I got you, you afraid to loose again')
            break
    elif choiceP1 == 'Paper !' and choiceP2 == 'Rock !':
        print('I won mothefucka')
        question = input('Wanna play again? ')
        if question == 'Yes':
            print('Aight! lets do it! Rock-Paper-Scissors !')
        elif question == 'No':
            print('Ok, I got you, you afraid to loose again')
            break
    elif choiceP1 == 'Paper !' and choiceP2 == 'Scissors !':
        print('You won mothefucka')
        question = input('Wanna play again ? ')
        if question == 'Yes':
            print('Aight! lets do it! Rock-Paper-Scissors !')
        elif question == 'No':
            print('Ok, I got you, you afraid to loose')
            break
    elif choiceP1 == 'Scissors !' and choiceP2 == 'Rock !':
        print('You won mothefucka')
        question = input('Wanna play again ? ')
        if question == 'Yes':
            print('Aight! lets do it! Rock-Paper-Scissors !')
        elif question == 'No':
            print('Ok, I got you, you afraid to loose')
            break
    elif choiceP1 == 'Scissors !' and choiceP2 == 'Paper !':
        print('I won mothefucka')
        question = input('Wanna play again ? ')
        if question == 'Yes':
            print('Aight! lets do it! Rock-Paper-Scissors !')
        elif question == 'No':
            print('Ok, I got you, you afraid to loose')
            break


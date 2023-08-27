# Python Ex 25

'''
You, the user, will have in your head a number between 0 and 100.
The program will guess a number, and you, the user, will say whether
it is too high, too low, or your number.'''

import random, sys    


def binarySearch(listOfNumbers,compteur):

    
    low = 0
    upper = len(listOfNumbers)
    mid = (upper/2)
    midPosition = int(mid)
    incrementedMidPosition = midPosition + 1

    target = listOfNumbers[midPosition]
    print(target)
    reply = input()
    compteur = compteur + 1

    if reply == 'right':
        print('you got it homes. it took you '+ str(compteur) + ' tries')
    elif reply == 'too low':
        arrayU = listOfNumbers[incrementedMidPosition:upper]
        binarySearch(arrayU,compteur)
    elif reply == 'too high':
        arrayL= listOfNumbers[low:midPosition]
        binarySearch(arrayL,compteur)


listA = list()

print('Yo Homes! I have a number in mind,it\'s in a range btw 0 and 100,let\'s see in how many tries do you need')
print('Have a guess: ')
firstLimit = 50
print(firstLimit)

answer = input()

counter = 0

if answer.lower() == 'right':
    callfunction = 'no'
    print('Yup homes, you got it in only 1 try')

    

elif answer.lower() == 'too low':

    while answer.lower() == 'too low':

        addToFirstLimit = random.randint(1,20)
        firstLimit= firstLimit + addToFirstLimit
        print(firstLimit)
        answer = input()
        counter = counter+1
        

        if answer.lower() == 'too high':
            secondLimit = firstLimit
            firstLimit = firstLimit - addToFirstLimit
            #print(firstLimit)
            #print(secondLimit)
            listA = [i for i in range(firstLimit,secondLimit)]
            #print(listA)
            print('Ok so the number is between ' + str(firstLimit) + ' and ' + str(secondLimit))
            callfunction = 'yes'
            counter = counter + 1
            break
        

        elif answer.lower() == 'right':
            callfunction = 'no'
            counter = counter + 1
            print('you got it homes. it took you '+ str(counter) + ' tries')
            
          
        

    
elif answer.lower() == 'too high':

    while answer.lower() == 'too high':

        removeToFirstLimit = random.randint(1,20)
        firstLimit= firstLimit - removeToFirstLimit
        print(firstLimit)
        answer = input()
        counter = counter + 1

        if answer.lower() == 'too low':
            secondLimit = firstLimit 
            firstLimit = firstLimit + removeToFirstLimit
            #print(firstLimit)
            #print(secondLimit)
            listA = [j for j in range(secondLimit,firstLimit)]
            #print(listA)
            print('Ok so the number is between ' + str(secondLimit) + ' and ' + str(firstLimit))
            callfunction = 'yes'
            counter = counter + 1
            break
    

        elif answer.lower() == 'right':
            callfunction = 'no'
            counter = counter + 1
            print('you got it homes. it took you '+ str(counter) + ' tries')
            

if callfunction == 'yes':
    binarySearch(listA, counter)
else:
    sys.exit


        
    


    

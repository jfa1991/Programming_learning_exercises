# Python Practice Ex 20:

# Exercise no Search Binary
import random

randomNumberListDuplicate = list()
randomNumberList = list()

for i in range (random.randint(0,99)): # create list of random list
    randomNumberListDuplicate.append(random.randint(0,99))


for j in randomNumberListDuplicate: # Remove duplicates from first random list
    if j not in randomNumberList:
        randomNumberList.append(j)

orderedRandomNumberList = sorted(randomNumberList) # Elements of list
                                                # ordered in ascending order
print(orderedRandomNumberList)
print(len(randomNumberList))

def findNumberIntoList(numbersList,numberToFind):

    if numberToFind in numbersList:
        print('Yep Bro, Number {} is in my List.'.format(numberToFind))
    elif numberToFind not in numbersList:
        print('Nope Mate, {} is not in my List.'.format(numberToFind))

        while True:
            numberToFind = input('Keep Guessing: ')
            numberToFindInt = int(numberToFind)
            if numberToFindInt in numbersList:
                print('Yep Bro, Number {} is in my List.'.format(numberToFind))
                break
                
    

numberToGuess = input('\n\nYo I have a list in mind, guess a number and let\'s see if it is in my list: ')
numberGuessed = int(numberToGuess)

test = findNumberIntoList(orderedRandomNumberList,numberGuessed)



            

    
            

    




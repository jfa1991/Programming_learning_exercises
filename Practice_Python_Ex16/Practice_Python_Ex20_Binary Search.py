# Ex Practice Python using recursive method

import random, sys

randomNumberListDuplicate = list()
randomNumberList = list()

for i in range (random.randint(1,99)): # create list of random list
    randomNumberListDuplicate.append(random.randint(0,99))


for j in randomNumberListDuplicate: # Remove duplicates from first random list
    if j not in randomNumberList:
        randomNumberList.append(j)

orderedRandomNumberList = sorted(randomNumberList) # Elements of list
                                                # ordered in ascending order
print(orderedRandomNumberList)

L= len(orderedRandomNumberList)
print('Longueur Liste: ' + str(L))
L1 = L/2
print('Index central: ' + str(L1))
L2 = int(L1)
blabla = orderedRandomNumberList[L2]
print('Valeur centrale de la liste: ' + str(blabla) + ' position dans la liste: ' + str(L2)) 


#orderedRandomNumberList = listA
#print('Nouvelle liste orderedRandomNumber: ' + str(orderedRandomNumberList))


def binary_search(array, target):
    low = 0
    mid = len(array) / 2
    midLength = int(mid)
    upper = len(array)

    if len(array) == 1:
        if array[0] == target:
            print(target)
            return array[0]
        else:
            return False
    if target == array[midLength]:
        print(str(array[midLength]) + ' is in my list')
        return midLength

# By applying the recursive method, we may end up having a number which is
# positioned at the mid position of the list or as the only element of the
# list, which makes it also positioned at the mid position.

    else:
        if midLength > low: 
            arrayl = array[0:midLength]
            #print(arrayl)
            binary_search(arrayl, target)

# Divide the list in a first half, where all value below mid position are
# grouped together. Then we applied the recursive method till we may eventually
# get the number desired.

        if midLength < upper:
            arrayu = array[midLength:len(array)]
            #print(arrayu)
            binary_search(arrayu, target)

# Divide the list in a second half, where all value above mid position are
# grouped together. Then we applied the recursive method till we may eventually
# get the number desired.

numberToGuess = input('\n\nYo I have a list in mind, guess a number and let\'s see if it is in my list: ')
numberGuessed = int(numberToGuess)

if numberGuessed not in orderedRandomNumberList:
        print(numberToGuess + ' is not in the list I have in mind')
        sys.exit

if __name__ == "__main__":
    binary_search(orderedRandomNumberList,numberGuessed)





    

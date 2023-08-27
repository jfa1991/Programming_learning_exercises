# Exercise 14 
# Write a program (function!) that takes a list and returns a new list
# that contains all the elements of the first list minus all the duplicates.

# Extras:

# Write two different functions to do this:
# one using a loop and constructing a list, and another using sets.


# Ex. 14 using loop and constructing a list

import random

def noDuplicateList():

    noDuplicateRandomList= list()
    
    randomListAP = random.sample(range(100), random.randint(1,30))
    randomListAP.sort()
    print('randomListAP:' + str(randomListAP))

    [noDuplicateRandomList.append(i) for i in randomListAP if i not in noDuplicateRandomList]

    print('Testing function noDuplicateRandomList: ' + str(noDuplicateRandomList))


test = noDuplicateList()


# This time using a list as a parameter into the function

def noDuplicateListParameter(listA):
    noDuplicateRandomList1= list()
    [noDuplicateRandomList1.append(i) for i in listA if i not in noDuplicateRandomList1]
    return noDuplicateRandomList1

listB = [1,1,2,2,4,5,7,9,11,11,15,18,19,21,21]


test1=noDuplicateListParameter(listB)
print('Testing function noDuplicateListParameter: ' + str(test1))


# Ex.14 using Set

def noDuplicateListSET():

    randomListAP = random.sample(range(100), random.randint(1,30))
    randomListAP.sort()
    print(randomListAP)

    randomSet = set(randomListAP)
    print(randomSet)
    noDuplicateRandomList1 = list(randomSet)
    print('Testing function noDuplicateListSet: ' + str(noDuplicateRandomList1))

test2 = noDuplicateListSET()

# Ex 14 using Set, using a list as a parameter into the function

def noDuplicateListSetParameter(listD):

    setD = set(listD)
    noDuplicateListD= list(setD)
    return noDuplicateListD

listB = [1,1,2,2,4,5,7,9,11,11,15,18,19,21,21]

test2 = noDuplicateListSetParameter(listB)
print('Testing function noDuplicateListSetParameter: ' + str(test2))
    

    

    





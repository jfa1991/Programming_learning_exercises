# Ex 3 Practice Python

# Take a list, say for example this one:

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list
# that are less than 50.

import random

randomList = [] # variable List created
listUnder50 = []

for i in range(random.randint(1,30)): # Creation of a random sample list containing
    randomList.append(random.randint(1,100)) # random numbers btw 1 and 100
print(randomList)

for i in randomList:
    if i < 50:
        listUnder50.append(i)
print(listUnder50)

print([i for i in randomList if i < 50]) # same as above in one line.
                        # created/print a list from variable randomList,
                        # where each index in listUnder50 are < 50



# Variant to Ex 3

import random

randomListV= []
ListUnder50V = []

for i in range(random.randint(1,30)):
    randomListV.append(random.randint(1,100))
print(randomListV)

[ListUnder50V.append(j) for j in randomListV if j < 50]
print(ListUnder50V)



# Extra
# Ask the user for a number and return a list that contains only elements
# from the original list a that are smaller than that number given by the user.


import random

randomList = []
listNumber = []

for i in range(random.randint(1,30)): # Creation of a random sample list containing
    randomList.append(random.randint(1,100)) # random numbers btw 1 and 100

print('I have a list of numbers in mind, Homes give me a number:')

numberGiven= random.randint(1,100) # random number assigned to a variable
print(numberGiven)

for j in randomList: # creation of list including numbers from randomList which are
    if j< numberGiven: # smaller than the random number assigned to the variable numberGiven
        listNumber.append(j)
print(listNumber)

print([i for i in randomList if i < numberGiven]) # same as above line
                                    # created/print a list where each index in List are
                                    # < numberGiven

# Variant to Extra

import random

randomListVE = []
listNumberVE = []

for i in range(random.randint(1,30)):
    randomListVE.append(random.randint(1,100))
print('I have a second list of number in mind Homes, give ve me a number:')

givenNumberVE = random.randint(1,100)
print(givenNumberVE)

[listNumberVE.append(j) for j in randomListVE if j < givenNumberVE]
print('Ok this the serie of numbers which I was thinking of and which are smaller than your number ' + str(listNumberVE))


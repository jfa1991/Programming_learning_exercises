# Ex 5


# Take two lists, say for example these two:

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# and write a program that returns a list that contains only
# the elements that are common between the lists (without duplicates).
# Make sure your program works on two lists of different sizes.

# Extras:

# Randomly generate two lists to test this
# Write this in one line of Python


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = list()

for i in a: # put common numbers of listA and listB in a same list
    if i in b and i not in c:
        c.append(i)
print(c)

# Extra random lists

import random


listA = list()
listB = list()
commonList= list()


for j in range(1,random.randint(1,20)):
    listA.append(random.randint(1,50))
listA.sort()
print(listA)

for i in range(1,random.randint(1,20)):
    listB.append(random.randint(1,50))
listB.sort()
print(listB)

for i in listA: # put common numbers of listA and listB in a same list
    if i in listB and i not in commonList:
        commonList.append(i)
print(commonList)




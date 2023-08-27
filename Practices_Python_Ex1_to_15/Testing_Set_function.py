# Testing Set() function

listA= [1,2,2,3,4,5,6,7,8,9,10]
listB = [2,2,4,6,8,10,12,14]

commonList =list()

commonList = set(listA) & set(listB)  # set() function join in a "List" values
                                    # which are common between two list
                                    
print(commonList) # print {2, 4, 6, 8, 10}

a= ['Fabio', 'Bob', 'Jo']
b = ['Lol', 'Jack', 'Fabio']

c = set(a) & set(b)
print(c)

# Write a program that returns a list that contains only the
# elements that are common between the lists (without duplicates).

import random

listAE = list()
listBE = list()

commonListE = list()

[listAE.append(random.randint(1,50)) for i in range(1,random.randint(1,20))]
listAE.sort()
print('Random list A: ' + str(listAE))


[listBE.append(random.randint(1,50)) for j in range(1,random.randint(1,20))]
listBE.sort()
print('Random list B: ' + str(listBE))

commonListE = set(listAE) & set(listBE)
print('List containing common random numbers: ' + str(commonListE))

# Testing how to generate a fixed indexed list of random numbers

randomFixedList = random.sample(range(100), 10) # Generate a fixed indexed list
                                                # 10 random number
randomFixedList.sort()
print('Random Fixed List: ' + str(randomFixedList))

# Testing how to generated a random sample indexed list of random numbers

randomSampledList = random.sample(range(100), random.randint(1,100))
randomSampledList.sort()
print('Random Sample List: ' + str(randomSampledList))

# Exercices with variant function set() and random.sample()


listAVE = random.sample(range(1,100), random.randint(1,100))
listAVE.sort()
print('Random List A: ' + str(listAVE))

listBVE = random.sample(range(1,100), random.randint(1,100))
listBVE.sort()
print('Random List B: ' + str(listBVE))


commonListVE = set([i for i in listAVE for j in listBVE if i==j])
print('List containing common random numbers: ' + str(commonListVE))
              


# Write a program that return a list whose value are the product of two random
# sample list

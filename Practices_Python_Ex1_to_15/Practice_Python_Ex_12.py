# Create a function generating a list composed only by distinct value from a
# different list

import random

def DistinctValueList(listA):

    uniqueValueList = list()

    [uniqueValueList.append(i) for i in listA if i not in uniqueValueList]

    


listB =[1,2,2,3,4,5,6,7,7]
print(listB)
DistinctValueList(listB)




# Practice Python Ex 12

# Write a program that takes a list of numbers
# (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only
# the first and last elements of the given list.

import random

listA = [1,2,4]
print(listA[0]) # print the value of index 0.
print(len(listA))
listB =set(listA) # listA converted into a type Set
print('ListB: ' + str(len(listB))) # obtain length of set ListB, convert it into
                                    # a list again and print it. 

randomList = random.sample(range(100), random.randint(1,100))
randomList.sort()
print('Random ListA: '  + str(randomList))


res =  [ randomList[i] for i in (0,-1) ] # for i in (0,-1) is used to
                                         # recover item in random list at specific
                                         # position. Assuming that instead of 
                                         # writing 0, I would have wrote 1
                                         # I would have recover indexed item 1
                                         # 
print('First and last element of Random ListA: ' + str(res))

# Practice Python Ex 12 writing a function:

def firstAndLast():

    randomListF = random.sample(range(100), random.randint(1,100))
    randomListF.sort()
    print('Here is a list of random numbers: '+ str(randomListF))

    listFirstAndLast = [randomListF[i] for i in (0,-1)]
    print('First and last element of Random ListF: ' + str(listFirstAndLast))

Test = firstAndLast()

# Write a program Asking the user to provide a list of number. Ask the user as
# well to pick n element of the list and do provide for each n element their
# position in the original list. From the position obtained, recover the values.
# 


print('Thats a new exercise')


def Ex12():

    i =1
    indexList=[]
    
    print('Homes, give me a list containing between 10 and 30 elements whose range is between 0 and 99, no duplicate please: ')
    randomList = random.sample(range(100),random.randint(10,31)) # create a random list of number whose sample size is random
    randomList.sort()
    noDuplicateRandomSet = set(randomList) # remove eventual duplicate and
                                            # convert list into dictionary
    noDuplicateRandomList = list(noDuplicateRandomSet) # convert set into list
    noDuplicateRandomList.sort()

    print('Random List: ' + str(noDuplicateRandomList))
    print('Your list contain ' + str(len(noDuplicateRandomList)) + ' elements')

    print('Aight, pick max 10 elements from your list without telling me their value')
    nElements = random.randint(1,10)
    print(nElements)
    print('Ok cool, amongst those n elements give me for each of them their position in your list')
    

    while i <= nElements:

        randomSelectedValue = random.choice(noDuplicateRandomList)  # a random value is
                                                                    # selected amongst
                                                                    # noDuplicateRandomList

        index= randomList.index(randomSelectedValue) # creating a new list, each value 
                                                     # added to the list represents the
                                                     # index of a each randomSelectValue                                                
        indexList.append(index)
        
        indexSet=set(indexList) # remove duplicate from indexList 
        
                                
        if len(indexSet) == i: 
            i=i+1
            finalIndexList = list(indexSet)

        elif len(indexSet) < i:
            i=i
            finalIndexList = list(indexSet)
            
    # indexSet=set(indexList) va enlever des éventuels doublons, ce qui pourrait amener
    # le nombre d'élément de la lista à être inférieur au nombre de nElements. Le
    # stratagème au-desssus a pour but de faire en sorte que tant que si la grandeur du
    # set indexSet n'est pas égale à la valeur absolue de l'index i, l'index i ne peut pas
    # croître pour attendre la valeur de nElements. 

    finalIndexList.sort()
    
    for i in finalIndexList: # print position of each n element picked by user.
        print('Position: ' + str((i)))

    print('That means that your chose') 
    for j in finalIndexList:
        indexPosition = (j)
        print('number: ' + str(noDuplicateRandomList[indexPosition]))
        
   # print the value of each position selected randomly in noDuplicateRandomList
 

Test= Ex12()     

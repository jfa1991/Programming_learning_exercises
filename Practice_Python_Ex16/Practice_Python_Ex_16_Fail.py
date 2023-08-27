# Ex 16

# Write a password generator. Strong passwords have a mix
# of lowercase letters, uppercase letters, numbers, and symbols.
# The passwords should be random, generating a new password every time
# the user asks for a new password. Include your run-time code
# in a main method.

# I tried Ex 16 but it did not work as expected. I have learnt nevertheless some
# interesting concepts which are worth keeping.

# In my python it is better create a new list than trying to modify it,
# or at least as a beginner, I believe it is ill-advised because it can quickly
# lead to messed up your code !!

# Use of enumarate function is an option if you plan to make changes in a list,
# but you better know what are the value of the index you would like to change.

# The function join which enable to create a string out a list, works only
# with list containing string.

# As it is possible to select a random number,  you are
# also able in python to select a random letter of the alphabeth as follows e.g:

# b = random.choice(string.ascii_lowercase)
    #print(b)


import random
import string

def passwordGenerator():
    allName = input('Welcome to Badass.com, please enter your first and Last name: ')
    splitName = allName.split() # split strings into a list
    firstName = splitName[0] # recover First Name
    lastName = splitName[1]
    firstNameString = str(firstName) # variable firstName is a list data type,
                                    # it is now converted into a string
    lastNameString = str(lastName)

    print('\nHi ' + firstName + '! In order to beneficiate of our premium contents\nplease sign up.')
    

    signUp = input('\nIf indeed you would you like to sign up, please type the word "Yes": ')
    if signUp == 'Yes':
        print('\nGreat, We are glad you decided to sign up Homes !')

    print('\nIn order to maximize the security of your account, we will attribute you\na password.')
    randomSizePassword = random.sample(range(1,13),random.randint(5,12)) 
    print(randomSizePassword) # create a random size list, the idea is to replace
                              # elements in the list with random characters
                              # to create a random password.

    firstCharacter = random.choice(firstName) # selected random character from
                                             # First Name
    lastCharacter = random.choice(lastName) # selected random character from
                                            # Last Name

    randomSizePassword[0] = firstCharacter # replaced first element of list randomSizePassword
                                           # with the value stored in firstCharacter
    randomSizePassword[-1] = lastCharacter # same as above but with last element
    print(randomSizePassword)

    lengthFirstName = len(firstNameString) 
    if lengthFirstName > 9:
        lengthFirstName = random.randint(1,10)

    lengthLastName = len(lastNameString)
    if lengthLastName > 9:
        lengthLastName = random.randint(1,10)

    # two elements of list randomSizePassword will be replaced with two digits
    # representing respectively the lenght of First and Last name User, if length
    # of string is larger than 9, it will be replaced with a random number btw
    # 1 and 9.

    randomSizePassword[1] = lengthLastName # value stored in variable
                                         # lenghtLastName replace value stored
                                         # in position 1 in list RandomSizePassword
    randomSizePassword[-2] = lengthFirstName
    print(randomSizePassword)

    #for i in randomSizePassword[2:-2]:
        #indexList = randomSizePassword.index(i)
        #print('value randomSizePassword associated with indexList: ' + str(indexList) + ' is ' + str(i))

    finalPassword = ' '.join(randomSizePassword)
    print(finalPassword)


    #b = random.choice(string.ascii_lowercase)
    #print(b)


testest = passwordGenerator()

# password au moins 5 charactères:
# Au minimum:
# premièr et dernier charactère password une lettre au hasard de allName,
# entre-deux au moins un symbole spécial et deux chiffre
# représentant longeur nom et prenom.

# Si longeur password > 5 remplir le reste avec lettre au hasard alphabet. 


# Ex 16

# In my first attemptf to complete Ex 16, it was not a success. Here I tried
# again.


# Write a password generator. Strong passwords have a mix
# of lowercase letters, uppercase letters, numbers, and symbols.
# The passwords should be random, generating a new password every time
# the user asks for a new password. Include your run-time code
# in a main method.

# I structured my code as following:
# a first part asking the user for his/her First and Last name,
# then if the user would like to sign up. If he/she signs
# up, asking how strong the password should be with 3 different levels.

# The way password are generated are different from each level.

# In level 1, I use the lenght of First and Last name to determine the length
# of the password.The characters are either a random letter of the alphabet
# or random number between 1 and 9. First character is always a letter
# followed by a number, I decided to alternate each other.

# In level 2, I still use the lenght of First and Last Name to determine the
# length but it should be minimum 6 characters. The characters are either
# a random letter of the alphabet or random number between 1 and 9.
# First character is always a letter followed by a number, I decided to
# alternate each other. This time a special symbol is added at the end of the
# password.

# In level 3, the lenght is always 9 characters. Its always
# a letter, a number and a symbol, in this specific order.

# To conclude the user is always asked whatever the level is if
# he/she would like a new# password

test = list()


import random
import string

def passwordGenerator():

    allName = input('Welcome to Badass.com, please enter your First and Last name: ')
    splitName = allName.split() # split string allName into a list
    firstName = splitName[0] # recover 1st element of the list which First Name
    lastName = splitName[1] # recover 2nd element of the list which is Last Name

    firstNameString = str(firstName) # variable firstName is a list data type,
                                    # it is now converted into a string
    lastNameString = str(lastName) 

    print('\nHi ' + firstName + '! In order to beneficiate of our premium contents\nplease sign up.')
    

    signUp = input('\nIf indeed you would like to sign up, please type the word "Yes", otherwise type "No": ')
    if signUp =='No':
        print('\nNo worries, buddy you can sign up later in case you may change\nidea')

    elif signUp == 'Yes':
        print('\nGreat, We are glad you decided to sign up Homes !')

    print('\nIn order to maximize the security of your account,\nyou will be attributed a password.')

    levelOfSafetyPassword = input('\nAmongst the following options: \nLevel 1\nLevel 2\nLevel 3\nSelect the level of safety of your password: ')

    if levelOfSafetyPassword == 'Level 1':

        while True:

            lenghtPassword = len(allName)-1
            if lenghtPassword % 2 == 0:
                halfLenghtPassword = lenghtPassword/2
            elif lenghtPassword % 2 == 1:
                halfLenghtPassword = round(lenghtPassword/2) # round the password,
                                                            # if halfLenghtPassword = 3,5
                                                            # it is rounded to 4.

            halfLengthPasswordI=int(halfLenghtPassword)

            rangePassword = int(lenghtPassword-halfLengthPasswordI)

            lettersInPassword = list() # list created to put random letters

            for i in range(rangePassword):
                randomLetter = random.choice(string.ascii_lowercase)
                lettersInPassword.append(randomLetter)

            numbersInPassword = list() # list created to put then random numbers

            for j in range(rangePassword):
                randomNumber = random.randint(1,10)
                numbersInPassword.append(randomNumber)

            password = list()

            indexList = list()

            for i in range(rangePassword): # create a list representing index position
                indexList.append(i)
            #print(indexList)

            for j in indexList:
                if j == 0 or j % 2 == 0:
                    valueToAssignToPassword = lettersInPassword[j] 
                    password.append(valueToAssignToPassword)

                elif j % 2 == 1:
                    valueToAssignToPassword = numbersInPassword[j]
                    valueNumberToAssignToPasswordStrFormat =str(valueToAssignToPassword)
                    # convert integer value stored in VTATP into a string in order to be
                    # able to use function join(). 
                    password.append(valueNumberToAssignToPasswordStrFormat)

            # The idea is to create a list reprsenting index, to then use the value
            # stored in j (value stored is index position) to recover values in lists
            # lettersInPassword and numbersInPassword.

            #print('Elements of password still under list Format:' + str(password))

            finalPassword =''.join(password) # elements of list put together into a string

            finalPasswordCapitalized = finalPassword.capitalize() # First element of password
                                                                    # capitalized
            print(finalPassword)

            if signUp == 'Yes':
                print('\nyou were attributed the following password: ')
                print(finalPasswordCapitalized)

            askForNewPassword = input('\nEnter the following sentence if you would like to be attributed a new password:\nI have yet to become a Badass: ')
            if askForNewPassword !='I have yet to become a Badass':
                print('Congrats! Now that you password is set,\nyou finally ready to become a true Badass!')
                break

    elif levelOfSafetyPassword == 'Level 2':

        while True:

            lenghtPassword = len(allName)-1

            if lenghtPassword < 6:
                lenghtPassword = 10

            if lenghtPassword % 2 == 0:
                halfLenghtPassword = lenghtPassword/2

            elif lenghtPassword % 2 == 1:
                halfLenghtPassword = round(lenghtPassword/2)

            halfLengthPasswordI=int(halfLenghtPassword)

            rangePassword = int(lenghtPassword-halfLengthPasswordI)

            lettersInPassword = list()

            for i in range(rangePassword):
                randomLetter = random.choice(string.ascii_lowercase)
                lettersInPassword.append(randomLetter)

            numbersInPassword = list()

            for j in range(rangePassword):
                randomNumber = random.randint(1,10)
                numbersInPassword.append(randomNumber)

            symbolsInPassword = ['*','%','&','!','$','£','@','+']

            password = list()
            indexList = list()

            for i in range(rangePassword):
                indexList.append(i)
            #print(indexList)

            for j in indexList:
                if j == 0 or j % 2 == 0:
                    valueToAssignToPassword = lettersInPassword[j]
                    password.append(valueToAssignToPassword)

                elif j % 2 == 1:
                    valueToAssignToPassword = numbersInPassword[j]
                    valueNumberToAssignToPasswordStrFormat =str(valueToAssignToPassword)
                    password.append(valueNumberToAssignToPasswordStrFormat)
                    #print('Elements of password still under list Format:' + str(password))

            symbolToAddToPassword = random.choice(symbolsInPassword)
            password.append(symbolToAddToPassword)

            finalPassword =''.join(password)
            finalPasswordCapitalized = finalPassword.capitalize()
            print(finalPassword)

            if signUp == 'Yes':
                print('\nyou were attributed the following password: ')
                print(finalPasswordCapitalized)

            askForNewPassword = input('\nEnter the following sentence if you would like to be attributed a new password:\nI have yet to become a Badass: ')
            if askForNewPassword !='I have yet to become a Badass':
                print('Congrats! Now that you password is set,\nyou finally ready to become a true Badass!')
                break
            
    elif levelOfSafetyPassword == 'Level 3':

    # in this part I Divided the password into thre 3 lists each one representing
    # one third of the lenght of the password. The 3 lists are joined
    # toghether and then converted into a string. 
    

        while True:

            lenghtPassword = 9
            rangePassword = 3
            lettersInPassword = list()

            for i in range(rangePassword): 
                randomLetter = random.choice(string.ascii_lowercase)
                lettersInPassword.append(randomLetter)

                # create a list of only random
                # letters to assign later to one
                # of the three intermediate list
                # representing a third of length
                # of the password

            numbersInPassword = list()

            for j in range(rangePassword): 
                randomNumber = random.randint(1,10)
                numbersInPassword.append(randomNumber)

                # create a list of only random
                # numbers to assign later to one
                # of the three intermediate list
                # representing a third of the lenght
                # of the password

            symbolsInPassword = ['*','%','&','!','$','£','@','+']
            symbolsPassword = list()

            for x in range(rangePassword):
                symbolToAddToPassword = random.choice(symbolsInPassword)
                symbolsPassword.append(symbolToAddToPassword)
            # create a list of only symbols
            # to assign later to one
            # of the three intermediate list
            # representing a third of the lenght
            # of the password
                

            passwordFirstPart = list()
            passwordSecondPart = list()
            passwordThirdPart = list()
            indexList = list()

            for i in range(rangePassword):
                indexList.append(i)
            #print(indexList)

            for j in indexList:
                if j == 0:
                    valueToAssignToPassword = lettersInPassword[0]
                    passwordFirstPart.append(valueToAssignToPassword)

                elif j == 1:
                    valueToAssignToPassword = numbersInPassword[0]
                    valueNumberToAssignToPasswordStrFormat =str(valueToAssignToPassword)
                    passwordFirstPart.append(valueNumberToAssignToPasswordStrFormat)
                    #print('Elements of password still under list Format:' + str(password))

                elif j ==2:
                    valueToAssignToPassword = symbolsPassword[0]
                    passwordFirstPart.append(valueToAssignToPassword)

            for i in indexList:
                if i == 0:
                    valueToAssignToPassword = lettersInPassword[1]
                    passwordSecondPart.append(valueToAssignToPassword)
                elif i == 1:
                    valueToAssignToPassword = numbersInPassword[1]
                    valueNumberToAssignToPasswordStrFormat =str(valueToAssignToPassword)
                    passwordSecondPart.append(valueNumberToAssignToPasswordStrFormat)
                elif i==2:
                    valueToAssignToPassword = symbolsPassword[1]
                    passwordSecondPart.append(valueToAssignToPassword)

            for x in indexList:
                if x == 0:
                    valueToAssignToPassword = lettersInPassword[2]
                    passwordThirdPart.append(valueToAssignToPassword)
                elif x == 1:
                    valueToAssignToPassword = numbersInPassword[2]
                    valueNumberToAssignToPasswordStrFormat =str(valueToAssignToPassword)
                    passwordThirdPart.append(valueNumberToAssignToPasswordStrFormat)
                elif x==2:
                    valueToAssignToPassword = symbolsPassword[x]
                    passwordThirdPart.append(valueToAssignToPassword)

            #print('\npasswordFirstPart: ' + str(passwordFirstPart))
            #print('\npasswordSecondPart: ' + str(passwordSecondPart))
            #print('\npasswordThridPart: ' + str(passwordThirdPart))

            password = passwordFirstPart + passwordSecondPart + passwordThirdPart
            # joined the three lists representing each one, one third of the
            # password.

            finalPassword =''.join(password) 
            finalPasswordCapitalized = finalPassword.capitalize()
            print(finalPassword)

            if signUp == 'Yes':
                print('\nyou were attributed the following password: ')
                print(finalPasswordCapitalized)

            askForNewPassword = input('\nEnter the following sentence if you would like to be attributed a new password:\nI have yet to become a Badass, otherwhise type whatever you want: ') 
            if askForNewPassword !='I have yet to become a Badass':
                print('Congrats! Now that you password is set,\nyou are finally ready to become a true Badass!')
                break
        
   

        
    


test = passwordGenerator()


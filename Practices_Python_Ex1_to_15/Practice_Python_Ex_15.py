# Testing split() method

testString = 'Hello Babes, How you doing'
result = testString.split('H')
print(result)

# print ['', 'ello Babes, ', 'ow you doing'] will split on character H,
# character H will be replaced by blank space

testString = 'Hello Babes, How you doing'
result = testString.split()
print(result)
# print ['Hello', 'Babes,', 'How', 'you', 'doing']
# If you do not include any character, it means “split on all whitespace”:

# Testing join () method

allTimeGreatNBA = ['MJ','Lebron','Magic','Kareem','Bird','Kobe','KD']
print(allTimeGreatNBA)
result= '*$*'.join(allTimeGreatNBA)
print(result)

#print before using method join():

# ['MJ', 'Lebron', 'Magic', 'Kareem', 'Bird', 'Kobe', 'KD']

#print after using method join():

# MJ*$*Lebron*$*Magic*$*Kareem*$*Bird*$*Kobe*$*KD

# no more comma after each element of the list, each element joined by *$* sign.



testString = 'Hello Babes, How you doing'
result = testString.split()

result.reverse()
print(result)
    


# Ex 15

# Write a program (using functions!) that asks the user for a long string
# containing multiple words. Print back to the user the same string,
# except with the words in backwards order.


def backwardsOrder():

    askForAString = input('Please enter a sentence: ')
    splitString = askForAString.split() # split string into a list
                                    # e.g Hello Jack becomes ['Hello', 'Jack']
    
    splitString.reverse() # reverse order of item in a list
   
    finalResult = ' '.join(splitString) # enable to form a string from a list
    print(finalResult)

test= backwardsOrder()

# Variation to function backWardOrder()

name=input("Enter your name:").split()
name=name[::-1] # reverse order into a string e.g from Hello to olleH but also
print(name)     # but also order in a list
print(' '.join(name))

    

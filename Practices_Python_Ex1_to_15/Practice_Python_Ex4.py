# Ex 4

# Create a program that asks the user for a number and then prints out
# a list of all the divisors of that number.(If you don’t know
# what a divisor is, it is a number that divides evenly into another number.
# For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

import random

listDivisors= []

print('homes give me a number:')
givenNumber = random.randint(1,100)
print(givenNumber)

for i in range(1,givenNumber):
    if givenNumber % i == 0:
        listDivisors.append(i)
print(listDivisors)
    

# Ex 4 Variant

import random

listDivisorsV= []

print('homes give me a number:')
givenNumberV = random.randint(1,100)
print(givenNumberV)

[listDivisorsV.append(i) for i in range(1,givenNumberV) if givenNumberV % i == 0]
print('Here is a list of number representing the divisors of the number you picked ' + str(listDivisorsV))





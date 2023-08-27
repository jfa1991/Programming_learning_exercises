# Ex 1 Year 

# Ask user to enter their name and their age.
# Print out a message addressed to them that tells them the year
# that they will turn 100 years old.

nameUser = input('Your name MF ?')
ageUser = input('Your age ?')
age100 = (100 - int(ageUser)) + 2019

print(nameUser + ' you will turn 100 years in ' + str(age100))


# Testing datetime function

import datetime
nowComplete = datetime.datetime.now()
print(nowComplete) # print year-month-day hours.min.second.

nowYMD= datetime.date.today() # print year-month-day
print(nowYMD)

nowYear = datetime.datetime.now().year # print only year
print(nowYear)

from datetime import time

nowTime = time()
print(nowTime) #print 00:00:00
nowTime1 = time(16,15,40)
print(nowTime1) #print 16:15:40


# testing format Method


stringContainingName = 'fabio cappadona'
string = 'Hello {}'.format(stringContainingName)
print(string) #print Hello fabio cappadona

stringContainingName = 'fabio cappadona'
string = 'Hello {}'.format(stringContainingName.title())
print(string) #print Hello Fabio Cappadona

age = int(input('your age ?'))
print('you are {}'.format(age))

# Ex 1 using datetime function/format method

import datetime

nowY = datetime.datetime.now().year

nameUser = input('Your name MF ?')
ageUser = input('Yo {}'.format(nameUser.title()) + ' how old are you ?')
age100 = ((100 - int(ageUser) + int(nowY)))

print('aight we are in ' + str(nowY) + ' that means you will turn 100 in ' + str(age100))

                
# Extras:

# Add on to the previous program by asking the user for another number
# and printing out that many copies of the previous message.
# (Hint: order of operations exists in Python)
# Print out that many copies of the previous message on separate lines.
# (Hint: the string "\n is the same as pressing the ENTER button)


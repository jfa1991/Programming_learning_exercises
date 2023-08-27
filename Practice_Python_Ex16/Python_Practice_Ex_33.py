# Python Practice Ex 33

''' For this exercise, we will keep track of when
    our friend’s birthdays are,and be able to find
    that information based on their name.
    Create a dictionary (in your file) of names and birthdays.
    When you run your program it should ask the user to enter
    a name, and return the birthday of that person back to them'''

import datetime, random

a = datetime.datetime(2011,10,22)

# Creating Date Objects
# To create a date, we can use the datetime() class (constructor)
# The datetime() class requires : year, month, day.

a = datetime.datetime(2011,10,22)
print(a)

''' The datetime object has a method for formatting date objects
into readable strings.

The method is called strftime(), and takes one parameter,
format, to specify the format of the returned string'''

print(a.strftime('%x'))

birthdays = {'Chandler': '11/10/2000', 'Phoebe': '22/09/1994', 'Joe': '09/03/1993',
             'Monica': '10/02/1999', 'Ross': '31/07/1991', 'Rachel': '03/12/1995'}


print('Hey yo !, would you like to know the birthdays of: ')

for k in birthdays.keys():
    print(k)
print('?')
    
firstQuestion = input()
firstQueston = firstQuestion.lower()

if firstQuestion =='yes':
    print('\nWho\'s birthday do you want to look up?')
    answer = random.choice(list(birthdays))
    print(answer)
    print('Ok {}\'s birthday is the {}'.format(answer,birthdays.get(answer)))

elif firstQuestion == 'no':
    print('Aight Homes as you wish')

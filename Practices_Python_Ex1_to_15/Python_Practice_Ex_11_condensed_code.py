# Practice Python Ex 11 condensed code

# Ask user for a prime number outside 1 and 2, keep asking the user until
# this one gets it. 


def primeNumber1():

    import random
    import sys

    listDivisors = list()
    print('Homes give me a prime number outside 1 and 2: ')
    numberAsked = random.randint(1,100)
    print(numberAsked)

    if numberAsked == 1 or numberAsked ==2:
        print('Nope homes,I told you outside 1 or 2')
        numberAsked = random.randint(3,100)
        print(numberAsked)

    [listDivisors.append(i) for i in range(1,numberAsked+1 ) if numberAsked % i == 0]

    if len(listDivisors)>2:
        print(str(numberAsked) + ' is not a prime number')

    elif len(listDivisors) <= 2:
        print('Aight you got it !')
        sys.exit()

    while True:

        listDivisors = list()
        print('Try again: ')
        numberAsked = random.randint(1,100)
        print(numberAsked)

        if numberAsked == 1 or numberAsked ==2:
            print('Nope homes,I told you outside 1 or 2')
            numberAsked = random.randint(1,100)
            print(numberAsked)

        [listDivisors.append(i) for i in range(1,numberAsked+1) if numberAsked % i == 0]

        if len(listDivisors)>2:
            print(str(numberAsked) + ' is not a prime number')

        else:
            print(str(numberAsked) + ' is a prime number')
            break

test = primeNumber1()

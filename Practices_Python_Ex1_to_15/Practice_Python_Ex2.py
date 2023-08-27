# Ex 2

# Ask the user for a number. Depending on whether the number is even or odd,
# print out an appropriate message to the user.

numberAsk =int(input('Say a number homes:'))

if numberAsk % 2 == 0:
    print('Thats a even number, now give me an odd one:')
    secondNumberAsk= int(input())
    if secondNumberAsk % 2 == 1:
        print('Thats what I am talking about')
    else:
        while True:
            secondNumberAsk=int(input('I told you give me a damn odd number:'))
            if secondNumberAsk % 2 == 1:
                print('Thats what I am talking about')
                break
                      

else:
    print('That an odd number, now give me an even number:')
    secondNumberAsk = int(input())
    if secondNumberAsk % 2 == 0:
        print('Thats what I am talking about')
    else:
        while True:
            secondNumberAsk=int(input('I told you give me a damn odd number:'))
            if secondNumberAsk % 2 == 0:
                print('Thats what I am talking about')
                break

# Ex 2 Extra
# If the number is a multiple of 4, print out a different message.

numberAsk =int(input('Homes, say a number which is multiple of 4:'))

if numberAsk % 4 == 0:
    print('Thats a multiple of 4 as well as an even number,now give me an odd one')
    secondNumberAsk = int(input())
    if secondNumberAsk % 2 == 1:
        print('Thats what I am talking about')
    else:
        while True:
            secondNumberAsk=int(input('I told you to give me a damn odd number'))
            if secondNumberAsk % 2 == 1:
                print('Thats what I am talking about')
                break
            
elif numberAsk % 4 !=0 and numberAsk % 2 == 0:
    print('Thats an even number but I would like you to give me a number which is also a multiple of 4:')
    while True:
        secondNumberAsk = int(input())
        if secondNumberAsk % 4 !=0 and secondNumberAsk % 2 == 0:
            print('Nope thats again an even number but not yet a multiple of 4, try again:')
        elif secondNumberAsk % 2 == 1:
            print('Nope thats an odd number, try again:')
        elif secondNumberAsk % 4 == 0:
                print('Thats what I am talking about, now give me an odd number:')
                break
    while True:
        thirdNumberAsk = int(input())
        if thirdNumberAsk % 2 == 0:
            print('Thats an even number homes, try again:')
        else:
            print('Aight you got it')
            break

else:
    print('Thats not a multiple of 4 and not a even number, try again:')
    while True:
        secondNumberAsk = int(input())
        if secondNumberAsk % 4 !=0 and secondNumberAsk % 2 == 0:
            print('Thats an even number but I would like you to give me a number which is also a multiple of 4:')
        elif secondNumberAsk % 2 == 1:
            print('Thats an odd number, try again:')
        elif secondNumberAsk % 4 == 0:
            print('Thats what I am talking about, now give me an odd number:')
            break
    while True:
        thirdNumberAsk = int(input())
        if thirdNumberAsk % 2 == 0:
            print('Thats an even number homes, try again:')
        else:
            print('Aight you got it')
            break

    
                                
                                
                                



    

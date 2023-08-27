
def findMax(x,y,z):

    if x > y and y > z:
        result = x 
    elif y > x and x > z:
        result = y
    elif z > y and y > x:
        result = z
    print('The biggest number is ' + str(result))

def findMax1(x,y,z):
    listA = [x,y,z]
    listA.sort()
    print(listA) 
    Max = listA[-1]

    print(Max)


print('Yo homes give me tree numbers: ')

a = input('first: ')
b = input('second: ')
c = input('third: ')

findMax1(a,b,c)


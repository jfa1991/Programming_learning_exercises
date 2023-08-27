# Write a program that asks the user how many Fibonnaci numbers to generate
# and then generates them. Make sure to ask the user to enter the number
# of numbers in the sequence to generate.

# Hint: The Fibonnaci seqence is a sequence of numbers where the next number
# in the sequence is the sum of the previous two numbers in the sequence.
# The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)


def Fibonacci():

    
    sequenceNumber = int(input('Give me a number, I will tell you which value this number has in Fibonacci sequance: '))

    indexPositionList= list()

    [indexPositionList.append(i) for i in range(1,sequenceNumber+1)]
    # creating a list representig the sequences of numbers

    print(sequenceNumber)

    fiboNumberList = []


    for i in range(0, len(indexPositionList)):
            indexPosition = (i)
            if indexPosition <= 1:
                fiboNumberList.append(1)  
            elif indexPosition > 1:
                fiboNumber = fiboNumberList[indexPosition -2] + fiboNumberList[indexPosition -1]
                fiboNumberList.append(fiboNumber)
               

    
    print(fiboNumberList)
    print(fiboNumber)
    
                
        
     

        #elif len(fiboNumberList) > 1:
            #indexPosition = i + 1
            
        
        #fiboNumberList.append(fiboNumberList[indexPosition-1] + fiboNumberList[indexPosition-2])
        #print(str(fiboNumberList))
                   

# fiboNumber = (fiboNumber-1 + FiboNumber-2)

    

   
    
test = Fibonacci()

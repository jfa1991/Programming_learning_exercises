# Testing

askWord = input('Enter a word: ')

for i in askWord: # print for each character of the string, its index
    print(askWord.index(i))

askWord1 = input('Enter a second word: ')

for i in askWord1: # print for each character of the string, its value
    print([i])

askWord2 = input('Enter a third word: ')

print(askWord2)

string1 = askWord2[::-1] # Reverse the string, e.g 'Fabio' becomes 'oibaF'
print(string1)

# Ex 6

# Ask the user for a string and print out whether this string is a
# palindrome or not.A palindrome is a string that reads the same
#forwards and backwards.

print('lets play a game, find a word which is a palindrome')

askString= input('Go head:')

reverseString = askString[::-1]

if reverseString == askString:
    print('Homes that a palindrome')
else:
    print('Thats not a palindrome')


# Ex 6 Extra

print('lets play a game, find a word which is a palindrome')

while True:
    askString1 =input('Go head: ')
    reverseString1 = askString1[::-1]

    if reverseString1 != askString1:
         print('Thats not a palindrome, try again')
    else:
        print('Homes, thats a palindrome, you got it')
        break


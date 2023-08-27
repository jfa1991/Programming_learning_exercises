''' Ask the user to guess a 4-digit number.
    For every digit that the user guessed correctly in the correct place,
    they have a “cow”. For every digit the user guessed correctly
    in the wrong place is a “bull.”

    Every time the user makes a guess,
    tell them how many “cows” and “bulls” they have.
    Once the user guesses the correct number, the game is over.
    Keep track of the number of guesses the user makes throughout
    the game and tell the user at the end.'''

import random

def cowBull_loop():
    ask= str(input("enter a four digit number: "))
    cow=0
    bullCow=0  #total number of digit guessed perfectly. right place + wrong place
    for i in range(0,4):
        if num[i]==ask[i]:
            cow+=1
    for i in num:
        if i in ask:
            bullCow +=1
    bull=bullCow-cow # bull est la condition suffisante, cow représente
                    #la condition nécessaire, si cow est déjà obtenu
                    # bull sera automatiquement obtenu, afin de ne compter bulls
                    # lorsque l'on obtient cow, on va soustraire soustrait à la
                    # variable bullCow la valeur de la valer cow.
                                      
    print("you have {} cow and {} bulls".format(cow,bull))
    return cow # sans la syntaxe 'return cow', la boucle ne s'arrêterai jamais
              # car une fois la fonction éxécutée et terminée la valeur 
              # 'se dissipe' et ne serait pas stocker dans la variable cow.


if __name__=="__main__":
    
# ensure that functions will be just only imported and
# not automatically executed if I reuse this method by import ...  
num= str(random.randrange(1000,9999)) # for testing use str(2727)
cow= 0
count=0
while cow !=4:
        count+=1
        cow = cowBull_loop()







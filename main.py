'''s=snake
w=water
g=gun
 in numbers: s is 1, w is -1 and g is 0'''

import random
computer=random.choice([1,-1,0])

youstr=input("enter your choice: ")

youdict={"s":1,"w":-1, "g":0}

reversedict={1: "snake", -1: "water" , 0: "gun"}

you=youdict[youstr]

print(f"you chose {reversedict[you]}\ncomputer chose {reversedict[computer]}")

if(computer==you):
    print("tie!")

else:
    if(computer==1 and you==0):
        print("hurray! you win....")


    elif(computer==-1 and you==1):
        print("hurray! you win...")


    elif(computer==-1 and you==0):
        print("you lose! hahaha")
    
    elif(computer==1 and you==-1):
        print("you lose! hahaha")
    
    elif(computer==0 and you ==-1):
        print("hurray! you win...")

    elif(computer==0 and you==1):
        print("you lose! hahaha")

    else:
      print("something went wrong")


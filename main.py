import random
'''
1 for rock
-1 for paper
0 for scissors
'''
computer=random.choice([1,-1,0])
youStr=(input("Enter your choice: "))
Dict={"rock":1,"paper":-1,"scissors":0}
reverseDict={1:"rock",-1:"paper",0:"scissors"}
you=Dict[youStr]

print(f"You chose {reverseDict[you]} and Computer chose {reverseDict[computer]}")
if(computer == you):
    print("its a draw")

else:
    if(computer==1 and you==-1):
        print("you win")
    elif(computer==1 and you==0):
        print("you lose")
    elif(computer==-1 and you==0):
        print("you win")
    elif(computer==-1 and you==1):
        print("you lose")
    elif(computer==0 and you==1):
        print("you win")
    elif(computer==0 and you==-1):
        print("you lose")
    else:
        print("something went wrong ")

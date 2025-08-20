import random

computer = random.choice ([-1, 0, 1])
a = input("Enter Your Choice: ")
dict = {"R": 1, "P": -1, "S": 0}
ReverseDict = {1: "Rock", -1: "Paper", 0: "Scissors"}
you = dict[a]
print(f"You Choose {ReverseDict[you]}\nComputer Choose {ReverseDict[computer]}")

if (computer==you):
    print("It's a Draw!!")

else:
    if(computer==-1 and you==1):
        print("You Loose!")
    elif(computer==-1 and you ==-0):
        print("You Win!")
    elif(computer==1 and you==-1):
        print("You Loose!")
    elif(computer==1 and you==0):
        print("You Loose!")
    elif(computer==0 and you==-1):
        print("You Loose! ")
    elif(computer==0 and you==1):
        print("You Win!")
    else:
        print("Something Went Wrong!")
    


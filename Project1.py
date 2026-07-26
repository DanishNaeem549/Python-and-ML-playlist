computer = -1
youstr =  input("enter you choice")
youdict = {"s": 1, "w": -1, "g" : 0}
you = youdict[youstr]


if(computer == you):
    print("match draw")
else:
    if (computer==-1 and you==1):
        print ("you win")
    elif(computer==-1 and you==0):
        print("you lose")
    elif(computer==1 and you==-1):
        print("you lose")
    elif(computer==1 and you==0):
        print("you win")           
    elif(computer==0 and you==-1):
        print("you win")
    elif(computer==0 and you==1):
        print("you lose")    
    else:
         print("some thing wrong")


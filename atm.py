### AUTOMATED TELLER MACHINE (ATM)
A=70000
print("please insert your card")
print("please select your language","\n",
      "1.HINDI\n",
      "2.ENGLISH")
l=int(input("Enter your language 1/2:-"))
if l==2:
    print("1.withdrawl\n",
          "2.balance enquiry\n",
          "3.deposite")
    o=int(input("Enter your option from 1/2/3:-"))
    if o==1:
        print("1.savings\n",
              "2.merchant")
        a=int(input("choose 1/2 :-"))
        if a==1:
            pin=int(input("Enter your pin here:-"))
            if pin>999 and pin<9999:
                w=int(input("Enter withdraw amount here:-"))
                if w<A and w>0:
                    print("please take your cash",w)
                    print("Available balance:-",A-w)
                    print("please take your card")
                    print("THANK YOU")
                else:
                    print("please enter a valid amount")
            else:
                print("Incorrect pin")
                print("Try again")
        else:
            pin=int(input("Enter your pin here:-"))
            if pin>999 and pin<9999:
                w=int(input("Enter withdraw amount here:-"))
                if w<A and w>0:
                    print("please take your cash",w)
                    print("Available balance:-",A-w)
                    print("please take your card")
                    print("THANK YOU")
                else:
                    print("please enter a valid amount")
            else:
                print("Incorrect pin")
                print("Try again")
    elif o==2:
        print("1.savings\n",
              "2.merchant")
        a=input("choose 1/2 :-")
        if a==1:
            pin=int(input("Enter your pin here:-"))
            if pin>999 and pin<9999:
                print("Available balance:-",A)
                print("please take your card")
                print("THANK YOU")
            else:
                print("Incorrect pin")
                print("Try again")
        else:
            pin=int(input("Enter your pin here:-"))
            if pin>999 and pin<9999:
                print("Available balance:-",A)
                print("please take your card")
                print("THANK YOU")
            else:
                print("Incorrect pin")
                print("Try again")
    elif o==3:
        print("1.savings\n",
              "2.merchant")
        a=input("choose 1/2 :-")
        if a==1:
            pin=int(input("Enter your pin here:-"))
            if pin>999 and pin<9999:
                d=int(input("Enter deposit amount here:-"))
                if d>0:
                    print("please put your cash here",d)
                    print("Available balance:-",A+d)
                    print("please take your card")
                    print("THANK YOU")
                else:
                    print("please enter a valid amount")
            else:
                print("Incorrect pin")
                print("Try again")
        else:
            pin=int(input("Enter your pin here:-"))
            if pin>999 and pin<9999:
                d=int(input("Enter deposite amount here:-"))
                if d>0:
                    print("please put your cash here",d)
                    print("Available balance:-",A+d)
                    print("please take your card")
                    print("THANK YOU")
                else:
                    print("please enter a valid amount")
            else:
                print("Incorrect pin")
                print("Try again")
else:
    print("THANK YOU")
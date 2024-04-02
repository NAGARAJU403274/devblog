pwd="naga123@"
curamnt=200000
print("______X welcome To Yourbank X_____")
print(" please insert your atm card")
psw=input("enter yuor password")

print('''please choose your option
          1.withdraw money
          2.deposite money
          ''')
if(pwd==psw):
    opt=int(input("please enter option"))
    if(opt==1):
        wamunt=int(input('enter withdrawal amount'))
        print("cuurent balance:",curamnt-wamunt)
    if(opt==2):
        wamunt=int(input('enter deposite amount'))
        print("cuurent balance:",curamnt+wamunt)
    else:
        print("plase enter vlaid option")
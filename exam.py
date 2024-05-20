def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

i=1
while i<5:
 a=int(input("Enter first number: "))
 b=int(input("Enter second number: "))
 print(" 1 - addition\n 2 - subtraction\n 3 - multiplication\n 4 - division\n")
 ch=int(input("Enter choice:"))
 if ch==1:
    print(a,"+",b,"=",add(a,b))
 elif ch==2:
    print(a,"-",b,"=",sub(a,b))
 elif ch==3:
    print(a,"*",b,"=",mul(a,b))
 elif ch==4:
    print(a,"/",b,"=",div(a,b))
 else:
    print("invalid")
    break
i+=1

#calculator
a=int(input("Enter A:"))
b=int(input("Enter B:"))
operator=input("Enter Operator <add,sub,mul,div>:")
if(operator=="add"):
    print(a+b)
elif(operator=="sub"):
    print(a-b)
elif(operator=="mul"):
    print(a*b)
elif(operator=="div"):
    print(a/b)
else:print("Invalid Operator")
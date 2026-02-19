#even odd count
counteve=0
countodd=0
a=int(input("Enter A:"))
b=int(input("Enter B:"))
for i in range(a+1,b+1):
    if(i%2==0):
        counteve=counteve+1
    elif(i%2==1):
        countodd=countodd+1

print("Even Count:",counteve)
print("Odd Count:",countodd)
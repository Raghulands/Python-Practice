#even numbers in range
count=0
a=int(input("Enter A:"))
b=int(input("Enter B:"))
for i in range(a+1,b+1):
    if(i%2==0):
        print(i)
        count=count+1

print("Count:",count)
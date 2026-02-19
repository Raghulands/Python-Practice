#Divisible Count
count=0
for i in range (1,101):
    if(i%3==0):
        if(i%5==0):
            count=count+1
print(count)
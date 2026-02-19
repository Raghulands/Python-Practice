#sum of list
rangenum=int(input())
a=[]
for i in range(rangenum):
    num=int(input())
    a.append(num)
sum=0
for i in a:
    sum=sum+i

print(sum)
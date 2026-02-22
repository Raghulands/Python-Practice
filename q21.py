#calwithfunc.
def add():
    print(a+b)
def sub():
    print(a-b)
def mul():
    print(a*b)
def div():
    print(a/b)

print("Enter Numbers:")
a=int(input())
b=int(input())
print("Oper? <add,sub,mul,div>")
c=input()
if c=="add":
    add()
elif c=="sub":
    sub()
elif c=="mul":
    mul()
elif c=="div":
    div()
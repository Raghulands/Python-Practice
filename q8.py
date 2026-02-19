#Loan Eligibility
salary=int(input("Enter Salary:"))
age=int(input("Enter Age:"))
if(salary>=20000):
    if(age<=25):
        loanamt=int(input("Enter Loan Amount:"))
else:
    print("Not Eligible")

if(loanamt<=50000):
    print("Eligible")
elif(loanamt>50000):
    print("Maximum is 50000")

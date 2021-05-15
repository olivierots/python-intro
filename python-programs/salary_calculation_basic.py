# salary, tax, net salary calculation based on a few conditions

salary=float(input("Enter your salary:" ))

if salary>=2000:
   tax=salary*21/100
   net=salary-tax

if salary<2000:
   tax=salary*15/100
   net=salary-tax

print("your salary is:", salary)
print("your tax is:", tax)
print("your net salary is:", net)

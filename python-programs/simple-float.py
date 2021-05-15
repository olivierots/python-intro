#  using float everywhere is better as it covers both integer  and float (decimal and non decimals) 

qty=input("Enter Qty bought:")
price=input("Enter unit price")

bill=float(qty) * float(price)

print("your bill is:", bill)


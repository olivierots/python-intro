product=input("ENter the product bought:")
qty=input("Enter Qty bought:")
price=input("Enter unit price:")
bill=float(qty) * float(price)
vat=bill*21/100

print("your bill details:")
print("product:",product)
print("quantity:", qty)
print("unit price:",price)
print("your billing amount:", bill)
print("vat calculated is:",vat)
print("total bill:",bill+vat)

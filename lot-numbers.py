# lets say your company has a product with this lot number: "037-00901-00021"
# 037 is the country code. 00901 is the product code. 00027 is the bacth number.
# create a program to print:
#    country code: _ _ _
#    product code: _ _ _
#    batch number: _ _ _
# [4] = 0123
# [:3] get the first 3 strings

lot_number = "037-00901-00027"
print("Country code:" , lot_number[0:3])
print("Product code:" , lot_number[4:9])
print("Product code:" , lot_number[10:])

import pandas as pd
file = pd.ExcelFile(r"C:\Users\Olivier\Desktop\Python\sales.xlsx")
print(file.sheet_names)
['sales', 'customers']

sheet = file.parse('sales')
print(sheet)
        Date             Customer  Invoice  Amount
0 2018-12-01  Steel Brothers Inc.       98    1340
1 2018-12-10             MMC Inc.       99    1900
2 2018-12-12             MMC Inc.      100    2900
3 2018-12-18  Steel Brothers Inc.      101     977
4 2018-12-21     Steel & Iron LLC      102    3400

type(sheet)
<class 'pandas.core.frame.DataFrame'>

 print(sheet.Date)
0   2018-12-01
1   2018-12-10
2   2018-12-12
3   2018-12-18
4   2018-12-21
Name: Date, dtype: datetime64[ns]

sheet
        Date             Customer  Invoice  Amount
0 2018-12-01  Steel Brothers Inc.       98    1340
1 2018-12-10             MMC Inc.       99    1900
2 2018-12-12             MMC Inc.      100    2900
3 2018-12-18  Steel Brothers Inc.      101     977
4 2018-12-21     Steel & Iron LLC      102    3400

>>> sheet.Amount.sum()
10517

sheet.loc[0]
Date        2018-12-01 00:00:00
Customer    Steel Brothers Inc.
Invoice                      98
Amount                     1340
Name: 0, dtype: object

sheet.loc[0, "Amount"]
1340

>>> sheet.set_index("Customer" , inplace=True)
>>> sheet.loc["MMC Inc."]
               Date  Invoice  Amount
Customer                            
MMC Inc. 2018-12-10       99    1900
MMC Inc. 2018-12-12      100    2900

 sheet = sheet.reset_index()

 sheet.loc[ sheet["Invoice"] == 99 ]   ==> locate invice No 99
   Customer       Date  Invoice  Amount
1  MMC Inc. 2018-12-10       99    1900

sheet.loc[ sheet["Amount"] > 2000 ]
           Customer       Date  Invoice  Amount
2          MMC Inc. 2018-12-12      100    2900
4  Steel & Iron LLC 2018-12-21      102    3400

sheet.loc[ sheet["Amount"].idxmax() ] ==> invoice with the highest amount

>>> sheet.loc[ sheet["Amount"].idxmax()]["Customer"] ==> customer with the highest amount
'Steel & Iron LLC'

>>> sheet.loc[ sheet["Amount"] > 1800 ]["Customer"]
1            MMC Inc.
2            MMC Inc.
4    Steel & Iron LLC
Name: Customer, dtype: object
>>> sheet.loc[ sheet["Amount"] > 1800 ]["Customer"].unique()
array(['MMC Inc.', 'Steel & Iron LLC'], dtype=object)

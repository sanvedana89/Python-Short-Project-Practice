import calendar
from datetime import datetime
now=datetime.now()
print("current time:",now.strftime("%H:%M:%S"))
year=2002
month=4
day =6
print(calendar.month(year,month,day))
# YY=int(input("enter year:"))
# MM=int(input("ENTER MONTH(1-12):"))
# print(calendar.month((YY,MM)))
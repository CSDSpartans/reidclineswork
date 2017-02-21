#!/usr/bin/env python3

from datetime import datetime
from datetime import timedelta
daysold = input('How many days from a date would you like?')
print(daysold +' days from today is:')
print(datetime.now() + timedelta(days=int(daysold)))

date = input("What is the date you would like to use? YYYY/MM/DD \n").replace("/","")

#print(daysold +' days old'+ date +':')
#print (birthday + timedelta(days=5661))
year=int(date[0:4])
month=int(date[4:6])
day=int(date[6:8])
print("Your birthday is "+str(year)+"/"+str(month)+"/"+str(day)+"?")
#Maybe use an until loop here
if input("(Y/n)") in ("Y","y","",None):
    print('You will be '+ daysold +' days old on:')
    print(datetime(year,month,day) + timedelta(days=int(daysold)))

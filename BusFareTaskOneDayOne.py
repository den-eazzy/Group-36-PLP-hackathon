from datetime import date                                                #import date fom datetime module
date = date.today()
day= date.strftime("%a")
week = {"Mon":0,"Tue":1,"Wed":2,"Thu":3,"Fri":4,"Sat":5,"Sun":6}        #dictionary to store key value pairs for the week days
if week[day] in range(0,5):                                             #if week day is btn mon - fri
    fare=100
elif week[day]==5:                                                       #if day is saturday
    fare=60
else:
    fare=80                                                             #if day is sunday

print("Date:",date)
print("Day:",day)
print("Fare:",fare)
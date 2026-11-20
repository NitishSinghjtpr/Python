#import a module named datetime to works with dates as date objects.

import datetime
# x=datetime.datetime.now() #print current datetime
# print(x)

# d=datetime.datetime(2002,3,11)
# print(d)

now=datetime.datetime.now()

year=now.strftime("%Y")
print(year)
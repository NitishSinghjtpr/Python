#import a module named datetime to works with dates as date objects.

import datetime
# x=datetime.datetime.now() #print current datetime
# print(x)

# d=datetime.datetime(2002,3,11)
# print(d)

now=datetime.datetime.now()

year=now.strftime("%Y")
print(year)

#%b Month name, short version Nov
#%B Month name, full version November
#%m Month as a number 01-12    11
#%y year short version 26
#%Y year full version 2026
#%H hour 00-23       21
#%l hour 00-12        9
#%p AM/PM            PM 
#%M Minute 00-59     08
#%s Secund           26

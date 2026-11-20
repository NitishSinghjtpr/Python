#first way to import

# import  demo

# demo.sum(5,5)
# print(demo)

#2nd way to import

# from demo import sum #when calling single fumction
# sum(6,2)

# from demo import * #using * i'm calling all function
# sum(5,8)
# sub(10,2)

#3rd way to import

# import demo as m 

# m.sub(78,8)
# m.sum(7,8)


import math
#Math module in python
# math.ceil(x) #ceil always return int value in next integer(suppose x=10.5 then return 11).

# print(math.floor(10.6)) # ye ceil ka ulta hai ye v integer return karega but pahle ka int 

# x=-11.2
# print(math.ceil(x))

#math.fabs(x) #always return +ve number
# print(math.fabs(x)) #if x=-11.3 then return 11.3

# print(math.factorial(5)) # ye factorial calculate kar deta hai but -ve value me error through karta hai

# print(math.fsum([1,2,3]))#ye pura list ki value ko sum karta hai and return float value

# print(math.sqrt(4)) #ye check karta hai ki kiska ye square value hai if 16 then output 4

#Random Module
import random
#random.randint(a,b) return a number between a and b  where a and b are include.
# print(random.randint(5,20))

#random.randrange(a,b) return a number between a and b but a include b not include.
# print(random.randrange(5,10))

#random.choice(l) where l is a list

# l=["Nitish","dipu","amol","sonu"]
# print(random.choice(l))

#random.random() always return between 0-1
# r=random.random()
# print(r)

#random.shuffle() rearrange the element and it always works on list 
# l=[12,15,16,20,25]
# random.shuffle(l)
# print(l)

#random.uniform(a,b) iska kaam hai ki a and b k bich ka koi v float value return karna 
# u=random.uniform(5,10)
# print(u)
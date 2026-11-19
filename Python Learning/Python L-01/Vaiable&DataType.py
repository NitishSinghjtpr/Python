#Our First Program
# print("Jai Shree Ram")

##--

# print("Python", "is", "fun")
# print(10 + 5)

##--

# name = "Nitish"
# age=21
# price=25.26
# print(name)
# print(age)
# print(price)

##value update

# age=23
# age=25
# print(age)

##--Data Type

# age = 21
# pi = 3.14
# complex_num = 2 + 3j
# A = True
# name = "Nitish"
# x = None    #None: No value

# print(type(age))
# print(type(pi))
# print(type(complex_num))
# print(type(A))
# print(type(name))
# print(type(x))

##-- Print Sum

# a=5
# b=30
# sum=a+b
# print("Sim is", sum)

##-- Arithmetic Operators

# a,b=10,3
# print(a+b) #addition
# print(a-b)#substraction
# print(a*b)#multiplication
# print(a/b)#division(always gives float number)
# print(a%b)#remainder
# print(a**b)#power: 10 to the power 3

##--Relational/Comparison operator
#== , != , > , < , >= , <= these always gives True or False

# a,b=10,3

# print(a==b)
# print(a!=b)
# print(a>b)
# print(a<b)
# print(a>=b)
# print(a<=b)

##--Assignment Operators
# =, +=, -=, *=, /=, %=, **= Shortcuts that update a variable

# num=10
# num+=5
# print(num)
# num-=5
# print(num)
# num*=5
# print(num)
# num/=2
# print(num)
# num**=2
# print(num)

##-- Logical Operators
# and, or, not Used to combine conditions.

# a,b=True,False

# print(a and b)
# print(a or b)
# print(not a)
# print((5 > 3) and (2 > 1))

##-- Type Converson

# a,b=1,2.0

# sum=a+b
# print(sum)#int is converted to float 

#But python can't add a number and a string

# a,b=1, "2"
# sum=a+b
# print(sum) #through Error

##-- Type Casting

# a,b=1, "2"
# c=int(b)#Type casting here
# sum=a+c
# print(sum) 

# print(int("25"))
# print(float(5))
# print(str(100))
# print(ord("A")) #Unicode value
# print(hex(255)) #hexadecimal string
# print(oct(8))   #octal string


##-- Input in Python

# number=input("Enter a number: ") #the result of input is always a string
# print(number)
# print(type(number))
# age=int(input("Enter your age :"))
# print(age)
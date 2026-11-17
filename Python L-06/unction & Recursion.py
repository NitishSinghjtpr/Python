#1. Functions in Python

# A function is a block of statements that performs a specific task. We write it once and can use it many times.

# def func_name(param1, param2):  #function defination  
#     # some work 
#     print(param1+param2)
# func_name(5,5)  #function call

#def keyword starts a function definition.
#Parameters are the names in the definition; arguments are the actual values passed in the call
#return sends a value back to where the function was called.
#A function runs only when it is called.

# def calc_sum(a, b): 
#     s = a + b 
#     return s 
# print(calc_sum(2, 3)) 
# print(calc_sum(10, 20))

##--A function without return gives back None :

# def greet(name): 
#     print("Hello,", name) 
    
# result = greet("Aman") 
# print(result)

#2. Types of Functions
#i.>Built in function print() , len() , type() , range()
#ii.>User define function  Created with def , like calc_sum() above

#3. Default Parameters
#A default value can be given to a parameter. It is used when no argument is passed for it.

# def calc_product(a=1, b=2): 
#     return a * b 
# print(calc_product())     #uses default   
# print(calc_product(5))    #a=5 and b default wala.
# print(calc_product(5, 6)) 


###--- Recursion
#- Recursion is when a function calls itself repeatedly. Every recursive function needs a base case: a condition where it stops calling itself. Without it, the function would run forever (and Python stops it with a RecursionError ).

#Q1. print n to 1

# def show(n):
#     if n==0: # base case
#         return
#     print(n)
#     show(n-1) #function call itself

# show(10)    

#Q2. Factorial using Recursion

# def fact(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*fact(n-1)
# print(fact(5))


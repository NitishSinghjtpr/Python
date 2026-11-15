###--- Loops

#-Loops are used to repeat instructions. Python has two kinds of loops: for loops and while loops

##- while Loop
# A while loop keeps running as long as its condition is True.

#Syntax:
# while condition:
#     # code to be executed

#print hello 5 times using while loop

# count = 0
# while count < 5:
#     print("Hello")
#     count += 1

#Print numbers from 1 to 10 using while loop

# count = 1
# while count <= 10:
#     print(count)
#     count += 1

##-- break and continue Statements
# break: Exits the loop completely
# continue: Skips the current iteration and moves to the next one

#example of break statement

# nums = [1, 2, 3, 4, 5]
# x = 3
# idx=0
# while idx < len(nums):
#     if nums[idx] == x:
#         print("Number found at index:", idx)
#         break
#     idx += 1


##example of continue statement

# i = 0
# while i < 5:
#     i += 1
#     if i == 3:
#         continue
#     print(i)

##--For Loop
# A for loop is used to iterate over a sequence (like a list, tuple, or string) and execute a block of code for each item in the sequence.

#Syntax:
# for item in sequence:
#     # code to be executed

#example of for loop

# numbers = [1, 2, 3, 4, 5]
# for num in numbers:
#     print(num)

#loop through a string

# for ch in "python":
#     print(ch)

#For with else

# numbers = [1, 2, 3, 4, 5]
# for num in numbers:
#     print(num)
# else:
#     print("Loop completed successfully")

## Range Function
# The range() function generates a sequence of numbers. It is often used in for loops to specify the number of iterations.
# range(start, stop, step)
#Example 1 of range function

# for i in range(5):  # Generates numbers from 0 to 4
#     print(i)

#Example 2
# for el in range(1,5):
#     print(el)

#example 3
# for el in range(1,10,2):
#     print(el)

##-- pass statement
#pass is a null statement that does nothing. It is used as a placeholder for code you will write later, because Python does not allow an empty block
#It is also commonly used in exception handling, which we will learn later.

# for el in range(10): 
#     pass        # to be written later 
# print("Program continues")


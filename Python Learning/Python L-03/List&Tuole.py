##-- List []

# marks = [87, 64, 33, 95, 76] 
# student = ["Karan", 85, "Delhi"] 
# print(marks) 
# print(student) 
# print(marks[0])       
# print(student[2])

## Like strings, list indexing starts from 0. But unlike strings, lists are mutable, meaning that their elements can be changed.


# student = ["Karan", 85, "Delhi"] 
# student[0] = "Arjun"      
# print(student) 
# print(len(student)) 

###--- List slicing

# list_names = ["Karan", "Arjun", "Rohit", "Rahul", "Amit"]
# print(list_names[0:3]) #ending index not included
# print(list_names[2:]) #starting index included
# print(list_names[:4]) #ending index not included
# print(list_names[:]) #prints all elements
# print(list_names[-1]) #prints last element
# print(list_names[-3:-1]) #prints elements from -3 to -1 (-1 not included)

###--- List Methods

# nums = [2, 1, 3] 
# nums.append(4) 
# print(nums) 
# nums = [2, 1, 3] 
# nums.sort() 
# print(nums) 
# nums.sort(reverse=True) 
# print(nums) 
# nums = [2, 1, 3] 
# nums.reverse() 
# print(nums) 

# nums = [2, 1, 3] 
# nums.insert(1, 5)  #insert 5 at index 1   
# print(nums) 
# nums = [2, 1, 3, 1] 
# nums.remove(1)        #removes first occurrence of 1
# print(nums) 
# nums = [2, 1, 3, 1] 
# nums.pop(2)         #removes element at index 2  
# print(nums)

###--- Tuples ()
# Tupples are similar to lists, but they are immutable, meaning that their elements cannot be changed after they are created. Tuples are defined using parentheses ().

# tup=(1, 2, 3, 4, 5)
# print(tup)
# print(tup[0])
# print(tup[1:3])
# print(len(tup))

# tup = (87, 64, 33, 95, 76) 
# tup[0] = 43  #Error

##-- Creating tuples:

# tup1=() #empty tuple
# tup2=(1,) #single element tuple
# tup3=(1, 2, 3) #multiple element tuple

##-- Tupple methods:

#- tup.index(el)
#- tup.count(el)

# tup = (1, 2, 3, 4, 5, 1, 2)
# print(tup.index(3))  # Output: 2
# print(tup.count(2))  # Output: 2


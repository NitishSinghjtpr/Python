###--- 1. Dictionary in Python
#Dictionaries store data in key : value pairs, written inside curly brackets{} 
# Mutable: you can change, add or remove items. 
# No duplicate keys: if a key repeats, the latest value replaces the old one. 
# Values can be of any type: string, number, list, even another dictionary.

# info = { 
#     "name": "nitish", 
#     "cgpa": 9.6, 
#     "marks": [98, 97, 95], 
# } 
# print(info["name"]) 
# print(info["cgpa"]) 
# print(info["marks"])


##-- Use dict["key"] to access the value of a key.
##-- Use dict["key"]=value to change the value of a key.

# info = {"name": "nitish", "cgpa": 9.6} 
# info["cgpa"] = 9.8          #changing the value of key "cgpa"
# info["city"] = "Delhi"      #adding a new key-value pair
# print(info)

##-- 2. Nested Dictionaries
#- A dictionary can be stored as a value inside another dictionary.

# student = {
#      "name": "nitish", 
#      "score": {
#         "chem": 98, "phy": 97, "math": 95, 
#         }, } 
# print(student["score"]) 
# print(student["score"]["math"])

##-- 3. Dictionary Methods
#- dict.keys() - returns a list of all the keys in the dictionary.
#- dict.values() - returns a list of all the values in the dictionary.  
#- dict.items() - returns a list of all the key-value pairs in the dictionary.
#- dict.get(key) - returns the value of the specified key.
#- dict.pop(key) - removes the specified key and returns its value.
#- dict.update(dict2) - adds the key-value pairs from dict2 to dict1.

# student = {
#     "name": "nitish", 
#     "cgpa": 9.6
#     } 
# print(student.keys()) 
# print(student.values()) 
# print(student.items()) 
# print(list(student.keys())) #convert to list

# student = {"name": "nitish", "cgpa": 9.6}
# print(student.get("name"))
# print(student.get("cgpa"))
# print(student.get("marks")) #returns None if key not found

# student = {"name": "nitish", "cgpa": 9.6}
# student.update({"marks": [98, 97, 95]}) #adding a new key-value pair
# print(student)


###--- Set in Python

# Sets are unordered collections of unique elements, written inside curly brackets{} 
#Each element must be immutable (numbers, strings, tuples). Lists cannot be stored in a set.
#Sets have no duplicate elements. If a duplicate is added, it will be ignored.
# Sets have no indexing, meaning that you cannot access elements by their position in the set. Like nums[0] will give an error.

# nums = {1, 2, 3, 4} 
# set2 = {1, 2, 2, 2}     #repeated elements will be ignored 
# print(nums) 
# print(set2) 
# print(len(set2))

#-An empty set is created with set() . Writing set.{} will create an empty dictionary, not a set.

# null_set = set() 
# print(type(null_set)) # this one set
# print(type({})) #this one dictionary

##--set methods
#- set.add(elem) - adds an element to the set.
#- set.remove(elem) - removes an element from the set. Raises KeyError if the element is not found.
#- set.discard(elem) - removes an element from the set if it is present.   
# - set.pop() - removes and returns a random value. Raises KeyError if the set is empty.
# - set.clear() - removes all elements from the set.
# - set.union(set2) - returns a new set with all elements from both sets.
# - set.intersection(set2) - returns a new set with only the elements that are 

# nums = {1, 2, 3} 
# nums.add(4) 
# nums.add(2)     #already present, will be ignored   
# print(nums) 
# nums.remove(3) 
# print(nums) 
# nums.clear() 
# print(nums)

# set1 = {1, 2, 3} 
# set2 = {2, 3, 4}  
# print(set1.union(set2)) 
# print(set1.intersection(set2)) #return only common element who present in both sets


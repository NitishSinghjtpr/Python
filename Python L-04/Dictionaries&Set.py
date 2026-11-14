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





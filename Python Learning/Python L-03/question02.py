# Q2. Check if a list is a palindrome (reads the same forwards and backwards).

list =[1,2,2,1]

copy_list=list.copy()
copy_list.reverse()
if list==copy_list:
    print("The list is a palindrome.")
else:
    print("The list is not a palindrome.")
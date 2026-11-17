#Q2. Write a recursive function to print all elements in a list.

def print_list(items,idx=0):
    if idx==len(items):
        return
    print(items[idx])
    print_list(items,idx+1)
print_list(["Nitish","Manish","Arun"])

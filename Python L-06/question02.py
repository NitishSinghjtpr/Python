#Q2. Write a function to print the elements of a list in a single line (list is the parameter).

def print_list(items):
    for item in items:
        print(item, end=" ")
    print()
print_list(["Nitish","Manish","Harsh"])
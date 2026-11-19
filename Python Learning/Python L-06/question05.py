#Q1. Write a recursive function to calculate the sum of the first n natural numbers.

def calc_sum(n):
    if n==0:
        return 0
    return n+calc_sum(n-1)
print(calc_sum(10))
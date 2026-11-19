# Search for a number x in this tuple using a loop.

nums = (10, 22, 33, 24, 35)
x = int(input("Enter a number to search: "))
idx = 0
while idx < len(nums):
    if nums[idx] == x:
        print("Number found at index:", idx)
        break
    idx += 1
else:
    print("Number not found in the tuple")
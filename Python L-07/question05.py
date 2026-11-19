#Q5. From a file containing numbers separated by commas, print the count of even numbers.

count =0
with open("number.txt","r")as f:
    data=f.read()
nums=data.split(",")
for num in nums:
    if int(num)%2==0:
        count+=1
print("Even Numbers :",count)
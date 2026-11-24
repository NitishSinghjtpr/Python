#print trangle star

# for i in range(1, 6):
#     for j in range(1, i+1):
#         print("*", end="")
#     print()

#Reverse trangle

# for i in range(5,0,-1):
#     for j in range(i):
#         print("*",end="")
#     print()

#Pyramid star
for i in range(1, 6):
    for j in range(5-i):
        print(" ", end="")

    for k in range(2*i-1):
        print("*", end="")

    print()
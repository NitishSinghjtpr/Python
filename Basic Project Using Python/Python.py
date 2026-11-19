rent=int(input("Enter your hostel/flat rent = "))
food=int(input("Enter the amount of food ordered = "))
electricity=int(input("Enter the total electricity spend = "))
charge_per_unit=int(input("Enter the charge per unit ="))
persons=int(input("Enter the number of persons living at room = "))

total_bill = electricity * charge_per_unit

output = (food+rent+total_bill)/persons

print("Each person will pay :", output)

#Q4. Write a function to convert USD to INR.

def usd_to_inr(usd, rate=83): 
    return usd * rate 
print(usd_to_inr(10))           
print(usd_to_inr(10, 88)) 
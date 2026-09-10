Order_amount=int(input("Enter order amount: Rs."))
if Order_amount>=2000:
    delivery_charge=0
elif Order_amount>=1000:
    delivery_charge=50
else:
    delivery_charge=100
final_amount=Order_amount+delivery_charge
print("Delivery charge: Rs. ",delivery_charge)
print("Final amount:Rs. ",final_amount)
  

    
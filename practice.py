n = int(input("Enter Amount:"))
if n>=5000:
   discount_percent=n*20/100
elif n>=3000:
   discount_percent=n*10/100
elif n>=1000:
   discount_percent=n*5/100

else:
   discount_percent=0
final_amount=n-discount_percent
print("final_amount:=",final_amount)


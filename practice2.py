Units=int(input("Enter the number of units:"))
if Units<=100:
    consumed_rate=2*Units
elif Units<=200:
    consumed_rate=3*Units
elif Units<=300:
    consumed_rate=5*Units
else:
    consumed_rate=7*Units
print("Electricity Bill:",consumed_rate)
     
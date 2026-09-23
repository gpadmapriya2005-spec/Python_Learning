#single import
import calculator 

# #members are not imported
# #functions
# print(add(20,10))
# print(sub(20,10))
# print(mul(20,10))
# print(div(20,10))
# #classes
# c = Calculator()
# #objects 
# print(c1)
# print(c2)

#module is imported
#functions
print(calculator.add(20,10))  #30
print(calculator.sub(20,10))  #20
print(calculator.mul(20,10))  #200
print(calculator.div(20,10))  #2.0
#classes
c = calculator.Calculator()
#objects 
print(calculator.c1)   #101
print(calculator.c2)   #201

 
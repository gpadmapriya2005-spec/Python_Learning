#multiple import 
import biology, physics, calculator 

# #members are not imported
# print(dna())
# b = Biology() 
# print(b1)
# print(add(20,10))
# c = Calculator()
# print(c1)
# print(newtonsfirst())
# p = Physics() 
# print(p1)

#modules are imported 
print(biology.dna())    #DNA: Carries genetic information
b = biology.Biology() 
print(biology.b1)       #'DNA'
print(calculator.add(20,10))   #30
c = calculator.Calculator()
print(calculator.c1)           #101
print(physics.newtonsfirst())  #First Law: Intertia: Objects remain at rest or in uniform motion unless acted on by an external force.'
p = physics.Physics() 
print(physics.p1)    #'Einstein'

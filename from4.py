#__all__ 
from physics import * 
from calculator import * 
from biology import * 

#all members of biology module
print(dna())   #'DNA: Carries genetic information.'
print(genes()) #'Genes: Units of heredity that control traits.'
b = Biology() 
print(b1)   #'DNA'
print(b2)   #'Protein'
print()

#all members of physics module
print(newtonsfirst()) #'First Law: Intertia: Objects remain at rest or in uniform motion unless acted on by an external force.'
print(newtonssecond())  #'Second Law: (F = ma): Acceleration is proportional to force and inversely proportional to mass.'
print(newtonsthird())   # '(Third Law: Action-Reaction): Every action has an equal and opposite reaction.'
p = Physics() 
print(p1)   #'Einstein'
print(p2)   #'Nikola Tesla'
print()

#all members of calculator module
print(add(20,10))  #30
print(sub(20,10))  #10
print(mul(20,10))  #200
print(div(20,10))  #2.0
c = Calculator()
print(c1)   #101
print(c2)   #201

# change __all__ of calculator(__all__ = ['add', 'c1']) and check
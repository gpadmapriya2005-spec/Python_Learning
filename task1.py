#print the keywords in python
import keyword
print(keyword.kwlist)
print(len(keyword.kwlist))

#create a variable for age and name
name="Padmapriya"
age=21
print("Name:",name)
print("Age:",age)

#create a variable with special symbol
my_name="Padmapriya"
print("Myname:",my_name)

#create variable starting with number
name1="PadmaPriya"
print("Myname",name1)

#assign multiple variables to multiple values
x=100
y=200
z=300
print(x,y,z)

#assign multiples variables to a single value
x=y=z=300
print(x,y,z)

#assign a variable to a value,re-assign to a different value
a=10
b=20
a=30
print(a,b)

#create and delete a variable
a=29
b=16
c=27
d=30
del d
print(a,b,c)

#swap variables in different ways
a=40
b=80
temp=a
a=b
b=temp
print("After swap using temp:")
print("a=",a)
print("b=",b)

#method2
a=50
b=100
a,b=b,a
print("a=",a)
print("b=",b)

#method3
a=16
b=29
a=a+b
b=a-b
a=a-b
print("a=",a)
print("b=",b)

#write a single line comment
print("Hi")


# def add(a, b):
#     print('add function')
#     c = a + b 
#     return c       #add function
#     print('HI')    
# def sub(a, b):
#     print('sub function')
#     c = a - b
#     return      #sub function
# def div(a, b):
#     print('div function')
#     c = a / b         #div function
# x = add(10, 15)   
# y = sub(20, 10)   
# z = div(25, 10)   
# print(x)      #25
# print(y)      #None
# print(z)      #None
# print()

#Type of arguments
def detail(name, age, rollno):
    print(f'My name is {name}') #My name is rakesh
    print(f'My age is {age}')   #My age is 20
    print(f'My rollno is {rollno}')  #My rollno is A101
#positional 
detail('rakesh', 20, 'A101') #My name is rakesh
detail(20, 'A101', 'rakesh') #My age is 20
#keyword                     #My roll no is A101
detail(age=20, rollno='A101', name='rakesh')
detail(rollno='A101', age=20, name='rakesh')
#default
def add(a, b=10, c=20):
    return a + b + c 
print(add(1))    #31
print(add(1,2))  #23
print(add(1,2,3)) #6
print(add(c=3, a=1, b=2)) #6

# #order of = in function def. DA after NDA
# def sub(a=10, b, c):
#     pass 

# #order of = in function call. KA after PA
# add(a=10, b, c)

def f1(*a):
    print(a)  #(1,2,3,4)
    print(type(a))  #class 'tuple'
f1(1,2,3,4)

def f2(**a):
    print(a)        #{a:'1',b:'2',c:'3',d:'4'}
    print(type(a))  #class 'dict'
f2(1,2,3,4)         
f2(a=1, b=2, c=3, d=4)
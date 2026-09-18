# local, global variable
a = 1
def f1():
    b = 2
    print(a)   #1
    print(b)   #2
    # print(c)   #error
def f2():
    c = 2 
    print(a)  #1
    # print(b)  #error
    print(c)  #2
f1()
f2()
print(a)      #1
# print(b)      #error
# print(c)      #error

#call by value, call by reference
# call by value 
def f1(a):
    a = 100
a = 4
f1(a)         
print(a)      #4

#call by reference
def f2(a):
    a = [10, 20, 30]
a = [1, 2, 3]
f2(a)
print(a)    #[1,2,3]

def f3(a):
    a = [100, 200, 300]
    a[2] = 200
a = [1, 2, 3]
f3(a)
print(a)    #[1,2,3]

# recursive functions
# factorial 
# fibonacci
def fact(n):
    if n==0:
        return 1
    if n==1:
        return 1
    return n-1




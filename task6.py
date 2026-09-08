for x in 'rakesh':
    print(x, end=' ')  
print()                  #r a k e s h
for x in range(2, 7):
    print(x, end=' ')  
print()                 #2 3 4 5 6
for x in [1,2,3]:
    print(x, end=' ')
print()                  #1 2 3
for x in (4,5,6):
    print(x, end=' ') 
print()                  # 4 5 6
for x in {7, 8, 9}:
    print(x, end=' ') 
print()                 #7 8 9
d = {1:'a', 2:'b', 3:'c'}
for x in d:
    print(x, end=' ')  
print()          #1 2 3
for x in d.keys():
    print(x, end=' ')  
print()        #1 2 3
for x in d:
    print(d[x], end=' ') 
print()       #'a' 'b' 'c'
for x in d.values():   
    print(x, end=' ')
print()       #a b c
for x in d.items():     
    print(x, end=' ')
print()       #([1:'a',2:'b',3:'c'])
#index based for loop. 
l = [5,4,3,2,1]
#iterate from left to right 
for i in range(len(l)):
    print(l[i], end=' ')
print()   #5 4 3 2 1
#iterate from right to left 
for i in range(len(l)-1, -1, -1):
    print(l[i], end=' ')
print()            #1 2 3 4 5
#iterate from 3rd element 
for i in range(2, len(l)):
    print(l[i], end=' ')
print()        #3 2 1
#iterate in steps of 2
for i in range(0, len(l), 2):
    print(l[i], end=' ')
print()    #5 3 1

#tricky
l = [1, 2, 3, 4, 5, 6]
for x in l:
    print(x)
    l.remove(x)     #1 3 5

#Homework
t = (5,4,3,2,1)  
s = {5,4,3,2,1}
d = {5:'e', 4:'d', 3:'c', 2:'b', 1:'a'}
w = 'rakesh' 
r = range(5,0,-1)
print()     #

#continue 
for x in range(1,11):
    if x % 3 == 0:
        continue 
    print(x,end=' ')    
print()     #1 2 4 5 7 8 10
#break
for x in range(1,11):
    if x % 3 == 0:      
        break 
    print(x,end=' ')  
print()   # 1 2
#pass 
for x in range(1,11):
    pass
a = 21      #21
#else 
for x in range(1,11):
    if x % 3 == 0:
        continue 
    print(x, end=' ')
else:
    print('Loop completed successfully')
print()                        #1 2 4 5 7 8 10 Loop completed successfully
for x in range(1, 11):
    if x % 3 == 0:
        break 
    print(x, end=' ')
else:
    print('Loop completed successfully') 
print('\n')
#assert
n = 10 
assert n > 5, 'N is not greater than 5' #A
print('A')
assert n < 5, 'N is not lesser than 5' 
print('B')
 
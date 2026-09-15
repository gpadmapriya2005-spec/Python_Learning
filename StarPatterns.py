n=5
for x in range(1,n+1):
    print(x*"*")

n=5
for x in range(n,0,-1):
    print(x*"*")

n=5
for r in range(1,n+1):
    print((n-r)*" " +r*"* ")

n=5
for r in range(n,0,-1):
    print((n-r)*" " +r* "* ")

n=5
for r in range(1,n+1):
    print((n-r)*" " +r*"* ")
for r in range(n-1,0,-1):
     print((n-r)*" " +r*"* ")

n=6
for r in range(n):
    for c in range(n):
        if r==0 or r==n-1 or c==0 or c==n-1:
          print("*",end=" ")
        else:
             print(" ",end=" ")
    print()
print()

n=6
for r in range(n):
    for c in range(n):
        if (r==c or c==n-r-1):
          print("*",end=" ")
        else:
             print(" ",end="")
    print()
print()


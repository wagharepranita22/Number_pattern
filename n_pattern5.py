n = int(input(" n value : "))
for i in  range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i+1):
        print("1", end=" ")
    for j in range(i):
        print("1", end=" ")
    print()

for i in range(n+1):
    for j in range(i):
        print(" ",end=" ")
    for j in range(i,n+1):
        print("1",end=" ")
    for j in range(i+1,n+1):
        print("1",end=" ")
    print()

n = int(input(" n : "))
for i in range(n):
    for j in range(i):
        print(" ",end=" ")
    for j in range(i,n):
        print("1",end=" ")
    for j in range(i+1,n):
        print("1",end=" ")
    print()

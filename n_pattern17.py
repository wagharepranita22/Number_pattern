n = int(input("n value :"))
p = 1
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i+1):
        if i % 2 == 0:
            print("a", end=" ")
        else:
            print("b",end=" ")
    for j in range(i):
        if i % 2 == 0:
            print("a", end=" ")
        else:
            print("b",end=" ")

    print()

n = int(input("n value :"))
for i in range(n):
    for j in range(i):
        print(" ",end=" ")
    for j in range(i+1,n+1):
        if i % 2 == 0:
            print("1", end=" ")
        else:
            print("3",end=" ")

    print()

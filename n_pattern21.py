n = int(input("Give your n value : "))
for i in range(n):
    for j in range(i):
        print(" ",end=" ")
    for j in range(i+1,n):
        if i % 2 == 0:
            print("1",end=" ")
        else:
            print("0",end=" ")
    for j in range(i,n):
        if i % 2 == 0:
            print("1", end=" ")
        else:
            print("0", end=" ")
    print()
n = int(input("Give your n value : "))
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i+1):
        if i % 2 == 0:
            print("#",end=" ")
        else:
            print("$",end=" ")
    for j in range(i):
        if i % 2 == 0:
            print("#", end=" ")                            
        else:
            print("$", end=" ")
    print()
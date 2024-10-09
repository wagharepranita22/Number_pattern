n = int(input("Give your n th  number : "))
for i in range (n):
    for j in range(i):
        print(" ",end=" ")
    for j in range(i,n):
        print("1", end=" ")
    print()

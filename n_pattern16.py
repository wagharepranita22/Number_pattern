n = int(input("n value :"))
p = 1
for i in range(n):
    for j in range(i+1):
        if i % 2 == 0:
            print("#", end=" ")
        else:
            print("$",end=" ")

    print()

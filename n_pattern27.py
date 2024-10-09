n = int(input("Give your n value : "))
k=1
for i in range(n):
    p=1
    for j in range(i+1):
        print(p, end=" ")
        p += 1
    for j in range(i+1,n):
        print(" ", end=" ")
    for j in range(i+1,n):
        print(" ", end=" ")
    p = 1
    for j in range(i+1):
        print(p, end=" ")
        p += 1

    print()

for  i in range (n):
    p = 1
    for j in range(i + 1, n):
        print(p, end=" ")
        p += 1
    for j in range(i+1):
        print(" ", end=" ")
    for j in range(i+1):
        print(" ", end=" ")
    p = 1
    for j in range(i+1,n):
        print(p, end=" ")
        p += 1
    print()
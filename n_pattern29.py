n = int(input("Give your input for n:"))
k=n
for i in range(n):
    p=k
    for j in range(i):
        print(" ",end=" ")
    for j in range(i,n):
        print(p,end=" ")
        p -=1
    k -=1
    print()
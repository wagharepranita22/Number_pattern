n = int(input("n value :"))
p = n
for i in range(n):
    for j in range(i):
        print(" ",end=" ")
    for j in range(i+1,n+1):
        print(p,end=" ")
    p -= 1
    print()

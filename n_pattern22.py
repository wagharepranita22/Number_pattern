n = int(input("Give your n value : "))
p =1
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i+1):
        print(p,end=" ")
    for j in range(i):
        print(p, end=" ")
    p +=1
    print()

for i in range(n+1):
    for j in range(i):
        print(" ",end=" ")
    for j in range(i+1,n+1):
        print(p,end=" ")
    for j in range(i,n+1):
        print(p, end=" ")
    p += 1
    print()
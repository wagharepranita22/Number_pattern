n = int(input("n value : "))
p = 1
for i in range(n):
    for j in range(i,n):
        print(p,end=" ")
    p+=1
    print()
import sys
n = int(input())
l = [int(x) for x in input().split()]
print(1,1)
print((n-1)*l[0])
x = l[:]
if (n!=1):
    print(2,n)
    
    x[0]+=(n-1)*l[0]
    for i in range(1,n):
        x[i]+=(n-1)*l[i]
        print((n-1)*l[i],end=' ')
    print()
else:
    print(1,1)
    print(0)
    
print(1,n)
for i in range(n):
    x[i]=(-1)*x[i]
print(*x)
    
    
                
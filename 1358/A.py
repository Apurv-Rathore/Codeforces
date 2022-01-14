t = int(input())
for _ in range(t):
    n , m = [int(x) for x in input().split()]
    if n%2==0 and m%2==0:
        print((m*n)//2)
    elif m%2==1 and n%2==1:
        print((n*(m-1)//2) + ((n-1)//2)+1)
    else:
        print(m*n//2)
from collections import defaultdict
t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    l = 0
    r = n-1
    ans = [0]*n
    i = 0
    while(l<=r and i<n):
        
        ans[i]=a[l]
        if (i==n-1):
            break
        ans[i+1]=a[r]
        l+=1
        r-=1
        i+=2
    
    print(*ans)
t = int(input())
for _ in range(t):
    n,k = list(map(int,input().split()))
    l = list(map(int,input().split()))
    m = max(l)
    for i in range(n):
        l[i] = m - l[i]
    
    if k%2==1:
        print(*l)
    else:
        m = max(l)
        for i in range(n):
            l[i] = m - l[i]
        print(*l)
    
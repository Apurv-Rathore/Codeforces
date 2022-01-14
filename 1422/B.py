from collections import defaultdict
def fun(l):
    m= 1000000000000000
    cur = 0
    for j in l:
        cur = 0
        for i in l:
            cur+=abs(i-j)
        m = min(cur,m)
    return m
t = int(input())
for _ in range(t):
    n,m = [int(x) for x in input().split()]
    l = []
    eles = []
    for i in range(n):
        x = [int(x) for x in input().split()]
        eles+=x
        l.append(x)
    ans = 0
    for i in range((n+1)//2):
        for j in range((m+1)//2):
            x = []
            x.append(l[i][j])
            if n-i-1!=i:
                x.append(l[n-i-1][j])
            if m-j-1!=j:
                x.append(l[i][m-j-1])
            if m-j-1!=j and n-i-1!=i:
                x.append(l[n-i-1][m-j-1])
            x.sort()
            ans+=fun(x)
    print(ans)
        
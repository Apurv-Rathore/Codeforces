t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    diffa = []
    diffb = []
    ma = min(a)
    mb = min(b)
    for i in range(n):
        diffa.append(a[i]-ma)
        diffb.append(b[i]-mb)
    
    ans = 0
    for i in range(n):
        ans+=max(diffa[i],diffb[i])
    print(ans)
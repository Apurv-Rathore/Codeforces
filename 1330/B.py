def check(a):
    a.sort()
    b=[i+1 for i in range(len(a))]
    if b==a:
        return 1
    else:
        return 0
 
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=max(a)
    c=[]
    if check(a[:b]) and check(a[b:]):
        c.append((b,n-b))
    if check(a[:n-b]) and check(a[n-b:]):
        c.append((n-b,b))
    c=list(set(c))
    print(len(c))
    for i in range(len(c)):
        print(*c[i])
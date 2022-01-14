t = int(input())
for i in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    ans = []
    for e in range(n*2):
        if l[e] not in ans:
            ans.append(l[e])
    ans = list(ans)
    print(*ans)
        
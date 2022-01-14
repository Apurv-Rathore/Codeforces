from math import ceil, log
from sys import stdin
import heapq 
t = int(input())
for _ in range(t):
    n = int(input())
    w = list(map(int,stdin.readline().split()))
    # w = [int(x) for x in input().split()]
    h = []
    adj = [set() for i in range(n)]
    f = [0]*n
    for i in range(n-1):
        a,b = list(map(int,stdin.readline().split()))
        a-=1
        b-=1
        adj[a].add(b)
        adj[b].add(a)
        f[a]+=1
        f[b]+=1
    # heapq.heapify(h) 
    # for i in range(n):
    #     if (len(adj[i])==1):
    #         heapq.heappush(h,[(-1)*w[list(adj[i])[0]],i])
    ans = [sum(w)]
    v = []
    for i in range(n):
        if (f[i]>1):
            f[i]-=1
            x = [w[i]]*f[i]
            v+=x
    v.sort(reverse=True)
    for i in range(len(v)):
        ans.append(ans[-1]+v[i])
    print(*ans)
    
import sys
from collections import defaultdict
from types import GeneratorType
def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to

    return wrappedfunc
@bootstrap
def dfs(u,prev):
    sz[u] = 1
    iscen = True
    for v in g[u]:
        if (v!=prev):
            yield dfs(v,u)
            sz[u] +=sz[v]
            if sz[v]>n//2:
                iscen = False
    if n-sz[u]>n//2:
        iscen = False
    if iscen:
        ans.append(u)
    yield
t = int(input())
for _ in range(t):
    n = int(input())
    g = [[] for i in range(n+1)]
    ans = []
    for i in range(n-1):
        x,y = map(int,input().split())
        g[x].append(y)
        g[y].append(x)
    
    sz = defaultdict(lambda:0)
    dfs(1,-1)
#    print(ans)
    if len(ans)==1:
        print(ans[0],g[ans[0]][0])
        print(ans[0],g[ans[0]][0])
        continue
    elif len(ans)>=2:
        x = ans[0]
        y = g[ans[0]]
        ff = y[0]
        if ff==ans[1]:
            ff = y[1]

        print(x,ff)
        print(ans[1],ff)
import sys,os,io
import math 
from collections import defaultdict
def ii():
    return int(input())
def li():
    return list(map(int,input().split()))
if(os.path.exists('input.txt')):
    sys.stdin = open("input.txt","r") ; sys.stdout = open("output.txt","w") 
else:
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

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
def dfs1(u,p):
    for kid in g[u]:
        if kid!=p:
            yield dfs1(kid,u)
            sumA[u]+=sumA[kid]
    sumA[u]+=a[u]
    yield

@bootstrap
def dfs2(u,p):
    for k in g[u]:
        if k!=p:
            dis[k]=1+dis[u]
            yield dfs2(k,u)
    yield



@bootstrap
def dfs3(node,parent,answer):
    global res
    res = max(res , answer)
    # print(node,answer)
    for kid in g[node]:
        if kid!=parent:
            yield dfs3(kid,node,answer+Sum-2*sumA[kid])
    yield

n = ii()
a = li()
g = [[] for i in range(n)]
for i in range(n-1):
    aa,b = li()
    aa-=1
    b-=1
    g[aa].append(b)
    g[b].append(aa)
sumA = [0]*n 
dfs1(0,-1)

dis = [0]*n 
dfs2(0,-1)
costWithRoot1 = 0
for i in range(n):
    costWithRoot1+=a[i]*dis[i]
answer = costWithRoot1
res = 0
# print(sumA)
Sum = sum(a)

dfs3(0,-1,answer)

print(res)
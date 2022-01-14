import sys,os,io
import math 
from collections import defaultdict
from collections import deque

def ii():
    return int(input())
def li():
    return list(map(int,input().split()))
if(os.path.exists('input.txt')):
    sys.stdin = open("input.txt","r") ; sys.stdout = open("output.txt","w") 
else:
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline



#for deep recursion__________________________________________-
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

ok = 0 

@bootstrap
def dfs(node,p,dis,l,g):
    global ok
    # print(node,l,dis[node])
    if l>=dis[node]:
        yield 
    if len(g[node])==1 and node!=0:
        # print("f")
        ok = 1 
        yield
    for i in g[node]:
        if i!=p:
            yield dfs(i,node,dis,l+1,g)
    yield



def solve():
    s = input()
    n,k = li()
    g = [[] for i in range(n)]
    friends = li()
    for i in range(k):
        friends[i]-=1
    for i in range(n-1):
        a,b = li()
        a-=1 
        b-=1 
        g[a].append(b)
        g[b].append(a)
    
    dis = [float('inf')]*n 
    vis = [False]*n 
    for i in friends:
        dis[i] = 0
        vis[i] = True
    friends = deque(friends)
    while friends:
        nn = len(friends)
        
        for i in range(nn):
            node = friends[0]
            friends.popleft()
            for child in g[node]:
                if vis[child]==False:
                    vis[child] = True 
                    friends.append(child)
                    dis[child] = dis[node]+1 
    global ok 
    ok = 0
    # print(dis)
    dfs(0,-1,dis,0,g)
    if ok:
        print("YES")
    else:
        print("NO")
    # st = [0]
    # d = 0
    # while st:
    #     node = st.pop(-1)
    #     if dis[node]<








t = 1
t = ii()
for _ in range(t):
    solve()

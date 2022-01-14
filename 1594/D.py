import sys,os,io
import math 
from collections import defaultdict
from collections import deque
def ii():
    return int(input())
def li():
    return list(map(int,input().split()))
input = sys.stdin.readline
# if(os.path.exists('input.txt')):
    # sys.stdin = open("input.txt","r") ; sys.stdout = open("output.txt","w") 
# else:
#     input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

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
def dfs(player, team):
    if vis[player]:
        yield
    vis[player]=True 
    val[team]+=1
    
    for i in imposter[player]:
        if which[i]==team:
            pos[0]=False
            yield 
        if vis[i]==False:
            which[i] = abs(1-team)
            yield dfs(i,team^1)
    for i in crewmate[player]:
        if which[i]==abs(1-team):
            pos[0]=False
            yield 
        if vis[i]==False:
            which[i] = team 
            yield dfs(i,team)
    yield 



            


t = 1
t = ii()
for _ in range(t):
    n,m = li()
    imposter = [[] for i in range(n)]
    crewmate = [[] for i in range(n)]
    played = defaultdict(lambda:0)
    for i in range(m):
        u,v,c = input().split()
        u = int(u)-1
        v = int(v)-1
        played[u]=1
        played[v]=1
        if c[0]=="i":
            imposter[u].append(v)
            imposter[v].append(u)
        else:
            crewmate[u].append(v)
            crewmate[v].append(u)
    vis = [0]*n 
    which = [-1]*n 
    ans = n 
    pos = [True]
    for i in played:
        ans-=played[i]
    for i in range(n):
        if vis[i]==0 and played[i]:
            val = [0,0]
            which[i] = 0
            dfs(i,0)
            ans += max(val)
    if pos[0]==False:
        ans = -1
    print(ans)

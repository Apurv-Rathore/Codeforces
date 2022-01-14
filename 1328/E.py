# ///////////////////////////////////////////////////////////////////////////
# //////////////////// PYTHON IS THE BEST ////////////////////////
# ///////////////////////////////////////////////////////////////////////////
from collections import defaultdict
import sys,os,io
from sys import stdin
from io import BytesIO, IOBase
BUFSIZE = 8192


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
class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")

if(os.path.exists('input.txt')):
    sys.stdin = open("input.txt","r") ; sys.stdout = open("output.txt","w") 
else:
    sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
    input = lambda: sys.stdin.readline().rstrip("\r\n")

n,m = [int(x) for x in input().split()]
adj = [set() for i in range(n)]
for i in range(n-1):
    u,v = [int(x) for x in input().split()]
    u-=1
    v-=1
    adj[u].add(v)
    adj[v].add(u)
tin  = defaultdict(lambda:0)
tout = defaultdict(lambda:0)
st = [0]
time = 0

@bootstrap
def dfs(node,p):
    global time
    tin[node] = time 
    time+=1
    for kid in adj[node]:
        if kid!=p:
            level[kid]=level[node]+1 
            yield dfs(kid,node)
            parent[kid] = node 
    tout[node] = time 
    time+=1
    yield
level = [0]*n 
parent = [-1]*n
dfs(0,-1)
# print(tin)
# print(tout)
def isparent(node,p):
    if tin[p]<=tin[node] and tout[p]>=tout[node]:
        return True
    return False
for _ in range(m):
    k = [int(x) for x in input().split()][1:]
    mxd = 0
    for i in range(len(k)):
        k[i]=parent[k[i]-1]
        if k[i]==-1:
            k[i]=0
    mxd = 0
    node = -1
    for i in k:
        if level[i]>mxd:
            mxd = level[i]
            node = i 
    f = 0
    for i in k:
        if i!=node:
            if isparent(node,i):
                continue 
            f =1
            break 
    if f:
        print("NO")
    else:
        print("YES")
    


# ///////////////////////////////////////////////////////////////////////////
# //////////////////// PYTHON IS THE BEST ////////////////////////
# ///////////////////////////////////////////////////////////////////////////

import sys,os,io
import math 
from collections import defaultdict

from io import BytesIO, IOBase
from types import GeneratorType
BUFSIZE = 8192
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
def ii():
    return int(input())
def li():
    return list(map(int,input().split()))


# ///////////////////////////////////////////////////////////////////////////
# //////////////////// DO NOT TOUCH BEFORE THIS LINE ////////////////////////
# ///////////////////////////////////////////////////////////////////////////
if(os.path.exists('input.txt')):
    sys.stdin = open("input.txt","r") ; sys.stdout = open("output.txt","w") 
else:
    sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
    input = lambda: sys.stdin.readline().rstrip("\r\n")

n = ii()
adj = [[] for i in range(n)]
for i in range(n-1):
    u,v = li()
    u-=1
    v-=1
    adj[u].append(v)
    adj[v].append(u)
ans = 0
size = [0]*n 

@bootstrap
def dfs(node,parent):
    sz = 0 
    for kid in adj[node]:
        if kid!=parent:
            sz+=yield dfs(kid,node)
    size[node] = sz+1
    yield size[node]
dfs(0,-1)
# print(size)
parentscore = 0
@bootstrap
def dfs(node,parent):
    global parentscore
    parentscore += size[node]
    cnt = 0
    for kid in adj[node]:
        if kid!=parent:
            yield dfs(kid,node)
    yield
dfs(0,-1)
# print(parentscore)
@bootstrap
def dfs(node,parent,parentscore):
    global ans 
    ans = max(ans,parentscore)
    # print(parent,node,parentscore)
    for kid in adj[node]:
        if kid!=parent:
            yield dfs(kid,node,parentscore+n-2*size[kid])
    yield
dfs(0,-1,parentscore)
print(ans)







# ///////////////////////////////////////////////////////////////////////////
# //////////////////// PYTHON IS THE BEST ////////////////////////
# ///////////////////////////////////////////////////////////////////////////

import sys,os,io
import math 
from collections import defaultdict

from io import BytesIO, IOBase
from types import GeneratorType
BUFSIZE = 8192

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
l = li()
ans = -1
p = 0
for i in range(n):
    # print(l,ans,p)
    if (set(l))==set([-1]):
        break 
    if i%2==0:
        ans+=1
        for j in range(n):
            if l[j]==-1:
                continue
            if l[j]<=p:
                p+=1
                l[j]=-1
    else:
        ans+=1
        for j in range(n-1,-1,-1):
            if l[j]==-1:
                continue
            if l[j]<=p:
                p+=1
                l[j]=-1
print(ans)
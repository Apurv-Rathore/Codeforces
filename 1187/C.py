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

n,m = li()
s = []
ns = []
for i in range(m):
    t,l,r = li()
    l-=1
    r-=1
    if t==0:
        ns.append([l,r])
    else:
        s.append([l,r])
arr = [0]*n 
for i in range(n-1):
    ss = 0
    nss = 0
    for l,r in s:
        if l<=i<=i+1<=r:
            ss+=1
    for l,r in ns:
        if l<=i<=i+1<=r:
            nss+=1
    # if ss>0 and nss>0:
    #     print("NO")
    #     exit()
    if nss>0 and ss==0:
        arr[i+1]=-1
c = 0
for i in range(n):
    if arr[i]==-1:
        c-=2 
        arr[i]=c 
    else:
        arr[i]=c 
    c+=1

for l,r in s:
    for i in range(l,r):
        if arr[i]>arr[i+1]:
            print("NO")
            exit()

for l,r in ns:
    f = 0
    for i in range(l,r):
        if arr[i]>arr[i+1]:
            f = 1
    if f==0:
        # print(l,r)
        print("NO")
        exit()


m = min(arr)
if m<=0:
    y = -m+1
    for i in range(n):
        arr[i]+=y 
print("YES")
print(*arr)







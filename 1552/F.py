import sys,os,io
from sys import stdin
from bisect import bisect_left
from io import BytesIO, IOBase
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

#__________________________TEMPLATE__________________OVER_______________________________________________________


# if(os.path.exists('input.txt')):
#     sys.stdin = open("input.txt","r") ; sys.stdout = open("output.txt","w") 
# else:
sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")

n = ii()
l = []
x = []
y = []
s = []
for i in range(n):
    l.append(li())
    x.append(l[-1][0])
    y.append(l[-1][1])
    s.append(l[-1][2])
dp = [0]*(n)
# dp[0]=x[0]
mod =998244353
prefix = [0]
for i in range(n):
    whichportal = bisect_left(x,y[i])
    dp[i]+=prefix[-1] - prefix[whichportal] + x[i]-y[i]
    dp[i]%=mod 
    prefix.append(dp[i]+prefix[-1])
    prefix[-1]%=mod
# print(dp)
ans = 0
# print(s)
for i in range(n):
    if s[i]==1:
        ans+=dp[i]
ans%=mod
    # ans = ans + dp[i] if s[i]==1 else 0
print((ans+x[-1]+1)%mod)
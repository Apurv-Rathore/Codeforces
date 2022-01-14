import os
import sys
from io import BytesIO, IOBase


def main():
    pass


# region fastio

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


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")

# endregion

if __name__ == "__main__":
    main()
def bs(beg,end,l,r,val):
    while(beg<=end):
        mid=(beg+end)//2
        v=(pre[mid-1]-pre[l-1])-(pre[r]-pre[mid])

        if (v==0):
            return mid
        elif((v<0 and val<0) or (v>0 and val>0)):
            end=mid-1
        else:
            beg=mid+1
    return beg

T=int(input())
for _ in range(T):
    n,q=map(int,input().split())
    s=list(input())
    pre=[0 for i in range(n+1)]

    for i in range(n):
        if (s[i]=="+"):
            if (i%2==0):
                pre[i+1]=pre[i]+1
            else:
                pre[i+1]=pre[i]-1
        else:
            if (i%2==0):
                pre[i+1]=pre[i]-1
            else:
                pre[i+1]=pre[i]+1

    for i in range(q):
        l,r=map(int,input().split())
        v=pre[r]-pre[l-1]
        if (v==0):
            print(0)
            
        elif(v%2==0):
            print(2)
            if (pre[r]-pre[l]%2!=0):
                x=bs(l+1,r,l+1,r,pre[r]-pre[l])
                print(l,x)
            else:
                x=bs(l+1,r,l+1,r,pre[r-1]-pre[l-1])
                print(x,r)
        else:
            print(1)
            x=bs(l,r,l,r,v)
            print(x)

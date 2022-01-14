import os
import sys
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


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")

from math import inf, log2


class SegmentTree:
    def __init__(self, array, func=max):
        self.n = len(array)
        self.size = 2**(int(log2(self.n-1))+1) if self.n != 1 else 1
        self.func = func
        self.default = 0 if self.func != min else inf
        self.data = [self.default] * (2 * self.size)
        self.process(array)

    def process(self, array):
        self.data[self.size : self.size+self.n] = array
        for i in range(self.size-1, -1, -1):
            self.data[i] = self.func(self.data[2*i], self.data[2*i+1])

    def query(self, alpha, omega):
        """Returns the result of function over the range (inclusive)!"""
        if alpha == omega:
            return self.data[alpha + self.size]
        res = self.default
        alpha += self.size
        omega += self.size + 1
        while alpha < omega:
            if alpha & 1:
                res = self.func(res, self.data[alpha])
                alpha += 1
            if omega & 1:
                omega -= 1
                res = self.func(res, self.data[omega])
            alpha >>= 1
            omega >>= 1
        return res

    def update(self, index, value):
        """Updates the element at index to given value!"""
        index += self.size
        self.data[index] = value
        index >>= 1
        while index:
            self.data[index] = self.func(self.data[2*index], self.data[2*index+1])
            index >>= 1


from math import gcd

n = int(input())
a = list(map(int, input().split()))
st = SegmentTree(a, func=gcd)

def check(n,alpha, omega, x):
    while alpha < omega:
        mid = (alpha+omega)//2
        left = st.query(alpha, mid)
        right = st.query(mid+1, omega)
        if left % x and right % x:
            return False
        if not left % x and not right % x:
            return True
        if (not left % x and n == 500000) or left % x != 0:
            omega = mid
        else:
            alpha = mid+1
    return True



for _ in range(int(input())):
    s = map(int, input().split())
    s = list(s)
    if len(s) == 4:
        p, l, r, x = s
        print("YES" if check(n,l-1, r-1, x) else "NO")
    else:
        p, i, y = s
        st.update(i-1,y)



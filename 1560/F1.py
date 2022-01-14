import os
import sys
from io import BytesIO, IOBase

from collections import defaultdict

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

def go(n, i, a, b, eq):
    if i == len(n):
        return True, []

    if eq:
        if n[i] == a:
            flag, x = go(n, i + 1, a, b, True)
            if flag:
                return True, [a] + x
        if n[i] < a:
            flag, x = go(n, i + 1, a, b, False)
            if flag:
                return True, [a] + x
        if n[i] == b:
            flag, x = go(n, i + 1, a, b, True)
            if flag:
                return True, [b] + x
        if n[i] < b:
            flag, x = go(n, i + 1, a, b, False)
            if flag:
                return True, [b] + x

        return False, []
    else:
        flag, x = go(n, i + 1, a, b, False)
        return True, [a] + x


def maxDigit(n):
    return str(max(int(d) for d in n))

def number(L):
    r = 0
    for d in L:
        r = r * 10 + int(d)
    return r

def find(n, k):
    if len(set(n)) == 1:
        return n
    
    D = []
    for d in map(int, n):
        if d not in D:
            D.append(d)

    if k == 1:
        U = [[D[0], D[0]], [D[0] + 1, D[0] + 1]]
    else:
        U = [[D[0], D[1]], [D[0], D[1] + 1], [D[0] + 1, 0], [D[0], 0]]

    r = 10**20
    for a, b in U:
        x = []
        m, M = min(a, b), max(a, b)
        flag, x = go(list(map(int, n)), 0, m % 10, M % 10, True)
        if flag:
            r = min(r, number(x))

    return r

T = int(input())
for _ in range(T):
    n, k = input().split(' ')
    k = int(k)

                
    print(find(n, k))

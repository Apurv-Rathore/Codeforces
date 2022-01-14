import io,os,sys
# input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

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
sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
# input = lambda: sys.stdin.readline().rstrip("\r\n")
def getSum( BITree, index): 
	sum = 0 
	while (index > 0): 
		sum += BITree[index] 
		index -= index & (-index) 
 
	return sum
 
def updateBIT(BITree, n, index, val): 
	while (index <= n): 
		BITree[index] += val
		index += index & (-index)

n,k = [int(x) for x in input().split()]
a = []
for i in range(n):
    a.append(int(input()))
ans = [1]*n 
bit = [[0]*(n+1) for i in range(k+1)]
for i in range(n):
    updateBIT(bit[0],n,a[i],1)
    for j in range(1,k+1):
        ans[i] = getSum(bit[j-1],a[i]-1)
        updateBIT(bit[j],n,a[i],ans[i])
    
print(sum(ans))


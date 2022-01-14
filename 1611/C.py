import sys,os,io
import math 
from collections import defaultdict
from collections import deque
def ii():
    return int(input())
def li():
    return list(map(int,input().split()))
if(os.path.exists('input.txt')):
    sys.stdin = open("input.txt","r") ; sys.stdout = open("output.txt","w") 
else:
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

def solve():
    n = ii()
    a = li()

    if a[0]!=n and a[-1]!=n:
        print(-1)
        return 
    a = deque(a)
    p = deque([])
    while len(a)>1:
        if a[0]<a[-1]:
            p.appendleft(a[0])
            a.popleft()
        else:
            p.append(a[-1])
            a.pop()
    
    print(*(a+p))



t = 1
t = ii()
for _ in range(t):
    solve()

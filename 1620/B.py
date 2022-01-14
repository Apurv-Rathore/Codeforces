import sys,os,io
import math 
from collections import defaultdict
def ii():
    return int(input())
def li():
    return list(map(int,input().split()))
if(os.path.exists('input.txt')):
    sys.stdin = open("input.txt","r") ; sys.stdout = open("output.txt","w") 
else:
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

def solve():
    w,h = li()
    x0 = li()[1:]
    x1 = li()[1:]
    y0 = li()[1:]
    y1 = li()[1:]
    ans = 0
    x = max(x0)-min(x0)
    x = x * h 
    ans = max(ans ,x )

    x = max(x1)-min(x1)
    x = x * h 
    ans = max(ans ,x )

    x = max(y0)-min(y0)
    x = x * w
    ans = max(ans ,x )

    x = max(y1)-min(y1)
    x = x * w
    ans = max(ans ,x )

    print(ans)

t = 1
t = ii()
for _ in range(t):
    solve()

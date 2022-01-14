import sys,os,io
import math 
from collections import defaultdict
from heapq import heappush, heappop, heapify
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
    l = li()
    l.sort()
    ans = -100000000000000000000000000
    m = 0
    for i in range(n):
        x = l[i]
        y = x
        # print(l[i],m,x,x-m)
        x-=m 
        ans = max(ans , x)
        m += x 
    print(ans)




t = 1
t = ii()
for _ in range(t):
    solve()

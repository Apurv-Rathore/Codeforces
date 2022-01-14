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
    n = ii()
    d = defaultdict(lambda:[])
    l = li()
    for i in range(n):
        d[l[i]].append(i)
    ans = -1
    for i in d:
        for j in range(1,len(d[i])):
            ans = max(ans , d[i][j-1] + n-d[i][j])
    print(ans)

t = 1
t = ii()
for _ in range(t):
    solve()

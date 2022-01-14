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
    d = defaultdict(lambda:0)
    for i in range(1,n+1):
        if i*i>n:
            break 
        d[i*i]=1 
    
    for i in range(1,n+1):
        if i*i*i>n:
            break 
        d[i*i*i]=1 
    ans = 0
    for i in d:
        if d[i]>0:
            ans += 1 
    print(ans)
    

t = 1
t = ii()
for _ in range(t):
    solve()

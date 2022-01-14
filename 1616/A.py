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
    a = li()
    d = defaultdict(lambda:0)   
    for i in a:
        d[abs(i)]+=1
    ans = 0
    for i in d:
        if i==0:
            ans+=1
        else:
            ans += min(d[i],2)
    print(ans)

t = 1
t = ii()
for _ in range(t):
    solve()

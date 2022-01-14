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
    h = li()
    l = 0
    r = max(h)
    ans = 0
    h1 = h[:]
    while l<=r:
        mid = (l+r)//2
        f = 1
        h = h1[:]
        for i in range(n-1,1,-1):
            d = min(h1[i]//3,max((h[i]-mid)//3,0))
            h[i]-=3*d
            h[i-1]+=d 
            h[i-2]+=2*d
        if min(h)>=mid:
            ans = max(ans,mid ) 

            l = mid+1 
        else:
            r = mid-1
    print(ans)
             



        



t = 1
t = ii()
for _ in range(t):
    solve()

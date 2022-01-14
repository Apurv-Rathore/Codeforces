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
    n,k = li()

    a = li()
    x = []
    k+=1
    a.sort()
    for i in range(1,n):
        x.append(a[i]-a[i-1])
    ans = 0
    notes = 0
    for i in range(len(x)):
        if k>0:
            ans += (10**a[i]) * min(10**(x[i])-1,k)
            k-=min(10**(x[i])-1,k)
    print(ans+k*(10**a[-1]))
        
    
    

t = 1
t = ii()
for _ in range(t):
    solve()

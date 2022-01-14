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
# else:
#     input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

def solve():
    n = ii()
    a = li()
    s = list(input())
    b = []
    r = []
    for i in range(n):
        if s[i]=='R':
            r.append(a[i]-1)
        else:
            b.append(a[i]-1)
    r.sort()
    b.sort()
    openn = 0
    f = [0]* (n+1)
    if b and b[0]<0:
        print("NO")
        return
    for i in b:
        if i>=n:
            continue
        
        f[min(n,i)] += 1
    x = 0
    # print(f)
    for i in range(n):
        if f[i]==0:
            x+=1
        else:
            if f[i]==1:
                continue 
            if f[i]-1>x:
                print("NO")
                return 
            x -= (f[i]-1)
    if r and r[-1]>=n:
        print("NO")
        return 
    f = [0]* n
    for i in r:
        if i>=0:
            f[max(0,i)] += 1
    x = 0
    for i in range(n-1,-1,-1):
        if f[i]==0:
            x+=1
        else:
            if f[i]==1:
                continue 
            if f[i]-1>x:
                print("NO")
                return 
            x -= (f[i]-1)

    print("YES")


t = 1
t = ii()
for _ in range(t):
    solve()

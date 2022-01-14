import sys,os,io
from sys import stdin
from math import log, gcd, ceil
from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
from bisect import bisect_left , bisect_right
import math 
def ii():
    return int(input())
def li():
    return list(map(int,input().split()))
if(os.path.exists('input.txt')):
    sys.stdin = open("input.txt","r") ; sys.stdout = open("output.txt","w") 
else:
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

no = "NO"
yes = "YES"
def solve():
    n = ii()
    v = li()
    t = li()
    p = []
    for i in range(n):
        if i==0:
            p.append(t[i])
        else:
            p.append(t[i]+p[-1])
    halfvolumemeltedDay = [0]*n
    ans = [0]*n
    suf = [0]*n
    for i in range(n):
        prev = 0
        if i>0:
            prev = p[i-1]
        ans = bisect_left(p,v[i]+prev,i,n-1)
        if p[ans]<=v[i]+prev:
            ans+=1
        # print(i,ans)

        if ans<n:
            # print(v[i]-( (0 if ans==0 else p[ans-1])-prev))
            halfvolumemeltedDay[ans] +=v[i]-( (0 if ans==0 else p[ans-1])-prev)
        
        # suf[min(n-1,ans)]+=1
        
        if i>0:
            suf[i-1]-=1
        if ans>0:
            suf[ans-1]+=1

        # print(suf)
        # print(halfvolumemeltedDay)
    for i in range(n-2,-1,-1):
        suf[i]+=suf[i+1]
    # print(suf)
    ans=[0]*n
    for i in range(n):
        ans[i]+=halfvolumemeltedDay[i]+suf[i]*t[i]
        
    # print(halfvolumemeltedDay)
    print(*ans)
    


t = 1
# t = int(input())
for _ in range(t):
    solve()
    

import sys,os,io
import math 
import random
from collections import defaultdict
def ii():
    return int(input())
def li():
    return list(map(int,input().split()))
if(os.path.exists('input.txt')):
    sys.stdin = open("input.txt","r") ; sys.stdout = open("output.txt","w") 
else:
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

def fun(a,b):
    if a and b and abs(a)//a==abs(b)//b:
        return 1
    return 0

def solve():
    #brute force
    n = ii()
    a = li()
    cnt = 0
    d = defaultdict(lambda:[])
    for i in range(n):
        x = a[i]
        while x>0:
            if x<=n:
                d[x].append(i)
            x//=2 
    res = 0
    def rec(x,d):
        nonlocal res
        if x==0:
            res = 1
            return 
        if res:
            return 
        for j in d[x]:
            d1 = d.copy()
            for i in d1:
                if j in d1[i]:
                    d1[i].remove(j)
            rec(x-1,d1)
    rec(n,d)
    if res:
        print("YES")
    else:
        print("NO")




        



t = 1
t = ii()
for _ in range(t):
    solve()

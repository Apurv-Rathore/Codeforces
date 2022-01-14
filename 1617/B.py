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


p = []
d =defaultdict(lambda:0)
ptr = 2 
while ptr<10000+1:
    if d[ptr]==0:
        p.append(ptr)
    else:
        a = 5 
    for q in range(len(p)):
        if ptr*p[q]>10000:
            break
        else:
            xx = p[q]
            d[ptr*xx]=xx
            ff = 0
            if ptr%xx==0:
                ff = 1
            if ff:
                break
    ptr+=1
x =len(p)
def fun(n):
    for qq in range(x):
        q = p[qq]
        w = n-q-1 
        if w%q==0:
            s = 1 
        else:
            a = n-q-1
            b = q 
            print(a,b,1)
            return 
    

def solve():
    n = ii()
    fun(n)
    
    

t = 1
t = ii()
for _ in range(t):
    solve()

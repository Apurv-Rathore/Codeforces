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
    l = [a]
    while(1):
        new = [0]*n 
        d = defaultdict(lambda:0)
        for i in l[-1]:
            d[i]+=1 
        for i in range(n):
            new[i] = d[l[-1][i]]
        if new==l[-1]:
            break 
        l.append(new[:])
    q = ii()
    for _ in range(q):
        x,k = li()
        x-=1 
        k = min(k , len(l)-1)
        print(l[k][x])



    

t = 1
t = ii()
for _ in range(t):
    solve()

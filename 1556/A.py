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
    c,d = li()
    if c<d:
        c,d=d,c
    if (c-d)%2==1:
        print(-1)
        return 
    if c==d:
        if c==0:
            print(0)
        else:
            print(1)
    else:
        print(2)

t = 1
t = ii()
for _ in range(t):
    solve()

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
    c = 0 
    for i in range(n):
        if a[i]>i+1+c:
            c += (a[i]) - (i+c+1)
    print(c)


t = 1
t = ii()
for _ in range(t):
    solve()


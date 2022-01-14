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
    l,r = li()
    x = r//2 +1
    if l<=x:
        print(r%x)
    else:
        print(r%l)


t = 1
t = ii()
for _ in range(t):
    solve()



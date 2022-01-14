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
    ind = 0
    while ind<n:
        j = ind 
        xx = 0
        while j>=0:
            x = j+2
            if a[ind]%x==0:
                j-=1 
            else:
                xx = 1 
                j-=1
                break
        if xx==1:
            ind+=1
        else:
            print("NO")
            return
    print("YES")

t = 1
t = ii()
for _ in range(t):
    solve()


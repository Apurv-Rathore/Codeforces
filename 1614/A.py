import sys,os,io
import math 
from collections import defaultdict
from collections import deque

def ii():
    return int(input())
def li():
    return list(map(int,input().split()))
if(os.path.exists('input.txt')):
    sys.stdin = open("input.txt","r") ; sys.stdout = open("output.txt","w") 
else:
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline



def solve():
    n,l,r,k = li()
    a = li()
    new = []
    for i in a:
        if l<=i<=r:
            new.append(i)
    new.sort()
    cnt = 0

    for i in range(len(new)):
        if k<new[i]:
            break 
        k-=new[i]
        cnt+=1 
    print(cnt)

        









t = 1
t = ii()
for _ in range(t):
    solve()

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
    n,m = li()
    res = 0
    for i in range(m):
        l,r,x = li()
        res |= x 
    res %= 1000000007
    y = pow(2,n-1,1000000007)
    res = res * y 
    res %= 1000000007
    print(res )


        









t = 1
t = ii()
for _ in range(t):
    solve()

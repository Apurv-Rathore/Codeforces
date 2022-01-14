import sys,os,io
import math 
from collections import defaultdict
def ii():
    return int(input())
def li():
    return list(map(int,input().split()))
if(os.path.exists('input.txt')):
    sys.stdin = open("input.txt","r") ; sys.stdout = open("output.txt","w") 
# else:
#     input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

def solve():
    n = list(input())
    ok = 0
    for i in n:
        if (int(i))%2==0:
            ok = 1 
    if not ok:
        print(-1)
        return 
    if int(n[-1])%2==0:
        print(0)
        return 
    
    if int(n[0])%2==0:
        print(1) 
        return 
    print(2)


t = 1
t = ii()
for _ in range(t):
    solve()

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
    n,l = li()
    b = li()
    ans = 0
    for i in range(l-1,-1,-1):
        ones = 0
        z=0
        for j in b:
            if j&(1<<i)==0:
                z+=1
            else:
                ones+=1
        if ones>z:
            ans += 1<<i 
    print(ans)

t = 1
t = ii()
for _ in range(t):
    solve()

# ///////////////////////////////////////////////////////////////////////////
# //////////////////// PYTHON IS THE BEST ////////////////////////
# ///////////////////////////////////////////////////////////////////////////
import sys,os,io
from sys import stdin
import math 
from collections import defaultdict

def ii():
    return int(input())
def li():
    return list(map(int,input().split()))


if(os.path.exists('input.txt')):
    sys.stdin = open("input.txt","r") ; sys.stdout = open("output.txt","w") 


t = ii()
for _ in range(t):
    n = ii()
    l = li()
    if l[-1]==0:
        ans = [i+1 for i in range(n+1)]
        print(*ans)
        continue

    if l[0]==1:
        ans = [i+1 for i in range(n)]
        ans = [n+1] + ans
        print(*ans)
        continue


    ok = 0
    for i in range(n-1):
        if l[i]==0 and l[i+1]==1:
            ans = []
            ok = 1
            for j in range(i+1):
                ans.append(j+1)
            ans.append(n+1)
            for j in range(i+1,n):
                ans.append(j+1)
            print(*ans)
            break 
    if ok==0:
        print(-1)


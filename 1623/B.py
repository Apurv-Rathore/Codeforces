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
    a = []
    d = defaultdict(lambda:0)
    for i in range(n):
        a.append(li()) 
        d[tuple(a[-1])]=1
    res = []
    # print(a)
    for i in range(n):
        if a[i][0]==a[i][1]:
            # print("f",i,a[i]+[a[i][0]])
            res.append(a[i]+[a[i][0]])
            continue
        for j in range(1,n+1):
            # if 1 in [d[()]]
            if ((a[i][0],j-1) in d) and ((j+1,a[i][1]) in d):
                res.append(list(a[i])+[j])
                break
            if ((a[i][0],j-1) in d) and j==a[i][1]:
                res.append(list(a[i])+[j])
                break
            if ((j+1,a[i][1]) in d) and j==a[i][0]:
                res.append(list(a[i])+[j])
                break
    for i in res:
        print(*i)
        



t = 1
t = ii()
for _ in range(t):
    solve()

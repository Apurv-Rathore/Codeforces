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



t = ii()
for _ in range(t):
    n = ii()
    s = list(input())
    res = s[:]
    res1 = s[:]
    ans = 0
    prev = 'B'
    for i in range(n):
        if s[i]=='?':
            if prev=='B':
                res[i]='R'
            else:
                res[i]='B'
        else:
            res[i]=s[i]
        prev = res[i]
    # ans = res.count('BB')+res.count('RR')
    ans = 0
    for i in range(1,n):
        if res[i]==res[i-1]:
            ans+=1

    ans1 = ans
    res1 = res[:] 
    res = s[:]
    prev = 'R'
    for i in range(n):
        if s[i]=='?':
            if prev=='B':
                res[i]='R'
            else:
                res[i]='B'
        else:
            res[i]=s[i]
        prev = res[i]
    # print(res)
    ans = 0
    for i in range(1,n):
        if res[i]==res[i-1]:
            ans+=1
    if ans1<ans:
        print(''.join(res1))
    else:
        print(''.join(res))
    

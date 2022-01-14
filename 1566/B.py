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
    s = list(input())
    if len(set(s))==1:
        if s[0]=='0':
            print(1)
        else:
            print(0)
    else:
        c = 0
        for i in range(1,len(s)):
            c += s[i]!=s[i-1]
        if c==1:
            print(1)
        elif c==2:
            if s[0]=='1' and s[-1]=='1':
                print(1)
            else:
                print(2)
        else:
            print(2)
            # print(min(2,s.count('0')))


t = 1
t = ii()
for _ in range(t):
    solve()


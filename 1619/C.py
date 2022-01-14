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
    a,s = li()
    a = str(a)
    s = str(s)
    a = list(a)
    s = list(s)
    # x = max(len(a),len(s))
    # a = ['0']*(x-len(a))+a
    # s = ['0']*(x-len(s))+s
    ptr = len(s)-1
    b = []
    for i in range(len(a)-1,-1,-1):
        if ptr<0:
            print(-1)
            return
        if int(a[i])<=int(s[ptr]):
            b.append(str(int(s[ptr])-int(a[i])))
            ptr-=1 
        else:
            if ptr==0:
                print(-1)
                return 
            x = int(s[ptr-1])*10 + int(s[ptr])
            if 0<=x-int(a[i])<=9:
                b.append(str(x-int(a[i])))
                ptr-=2 
            else:
                print(-1)
                return 
    print(int(''.join(s[:ptr+1] + b[::-1])))
    

    

t = 1
t = ii()
for _ in range(t):
    solve()

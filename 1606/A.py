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
    # n = ii()
    s = input()
    x = []
    o = s[:]
    n = len(s)
    for i in s:
        if not x or x[-1]!=i:
            x.append(i)
    if len(x)%2==1:
        print(s)
        return 
    s = list(s)
    for i in range(n):
        if s[i]=='a':
            s[i] = 0
        else:
            s[i] = 1 
    cnt = 0
    for i in range(1,n):
        if s[i-1]==0 and s[i]!=s[i-1] :
            cnt+=1 
        else:
            if s[i-1]==1 and s[i-1]!=s[i]:
                cnt-=1
    o = list(o) 
    if cnt!=1:
        o[-1]='b'
        print(''.join(o))
    else:
        o[-1] = 'a'
        print(''.join(o))

    

t = 1
t = ii()
for _ in range(t):
    solve()

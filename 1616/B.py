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
    n = ii()
    f = 0
    s = list(input())
    xx = ""
    
    for i in range(n-1):
        if s[i+1]>s[i]:
            xx = ''.join(s[:i+1]+s[:i+1][::-1])
            f = 1
            break
    if f:
        print(min(xx,s[0]+s[0])) 
        return 

    
    print(min(s[0]+s[0],''.join(s+s[::-1])))

t = 1
t = ii()
for _ in range(t):
    solve()

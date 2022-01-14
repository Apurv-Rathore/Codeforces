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
    s = input()
    for i in range(n-1):
        if s[i]=='a' and s[i+1]=='b':
            print(i+1,i+2)
            return 
        if s[i]=='b' and s[i+1]=='a':
            print(i+1,i+2)
            return 
    print(-1,-1)

t = 1
t = ii()
for _ in range(t):
    solve()

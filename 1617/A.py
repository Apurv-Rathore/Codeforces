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
    s = input()
    t = list(input())
    if t!=['a','b','c'] or 'a' not in s or 'b' not in s or 'c' not in s:
        s = list(s)
        s.sort()
        print(''.join(s))
    else:
        s = list(s)
        s.sort()
        rem = [-1]*len(s)
        new = []
        for i in range(len(s)):
            if s[i]=='a':
                new.append('a')
                rem[i]=1
        for i in range(len(s)):
            if s[i]=='c':
                new.append('c')
                rem[i]=1
        for i in range(len(s)):
            if s[i]=='b':
                new.append('b')
                rem[i]=1
        for i in range(len(s)):
            if rem[i]==-1:
                new.append(s[i])
        print(''.join(new))



t = 1
t = ii()
for _ in range(t):
    solve()

import sys,os,io
from sys import stdin
from functools import cmp_to_key
from bisect import bisect_left , bisect_right
def ii():
    return int(input())
def li():
    return list(map(int,input().split()))
if(os.path.exists('input.txt')):
    sys.stdin = open("input.txt","r") ; sys.stdout = open("output.txt","w") 
# else:
#     input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

for _ in range(1):
    n = ii()
    l = []
    ans=''
    last=[]
    for i in range(n):
        s = list(input())
        if s.count('s')==0:
            last+=s
            continue
        l.append([s.count('h')/s.count('s'),s])
    l.sort()
    # print(l)
    
    ans=[]
    for i in l:
        ans+=i[1]
    ans+=list(last)
    ans=''.join(ans)
    s = ans[:]
    pres = [0]*(len(s))
    sufh = [0]*(len(s))
    for i in range(len(s)):
        if i>0:
            pres[i]+=pres[i-1]
        if s[i]=='s':
            pres[i]+=1
    for i in range(len(s)-1,-1,-1):
        if i<len(s)-1:
            sufh[i]+=sufh[i+1]
        if s[i]=='h':
            sufh[i]+=1
    cnt = 0
    for i in range(len(s)):
        if s[i]=='s':
            cnt+=sufh[i]
    print(cnt)
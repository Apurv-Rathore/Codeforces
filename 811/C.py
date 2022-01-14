import sys,os,io
from sys import stdin
from collections import defaultdict
def ii(): return int(input())
def li(): return list(map(int,input().split()))
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
n = ii()
l = [-1] + li()
start = defaultdict(lambda:n)
end = defaultdict(lambda:-1)
for i in range(n+1):
    start[l[i]]=min(start[l[i]], i)
    end[l[i]]=max(end[l[i]], i)
dp = [float('-inf')]*(n+1)
dp[0]=0
for i in range(1,n+1):
    if end[l[i]]!=i:
        dp[i]=dp[i-1]
        continue
    s = set()
    ls = start[l[i]]
    x = 0
    for j in range(i,-1,-1):
        if end[l[j]]>i:
            break 
        ls = min(ls,start[l[j]])
        if l[j] not in s:
            x^=l[j]
        s.add(l[j])
        if j<=ls:
            dp[i]=max(dp[j-1] + x , dp[i])
    dp[i]=max(dp[i],dp[i-1])
print(dp[-1])





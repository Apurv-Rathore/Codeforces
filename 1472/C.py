from math import ceil,log
from collections import defaultdict
from sys import stdin
# l = list(map(int,stdin.readline().split()))
t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    suf = l[:]
    
    for i in range(n-1,-1,-1):
        if (i+l[i]<n):
            suf[i]+=suf[i+l[i]]
    print(max(suf))
    
    
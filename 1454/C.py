import math
import sys
from sys import stdin
from collections import defaultdict
t=int(input())
for _ in range(t):
    n = int(input())
    l = [int(x) for x in input().split()]
    answer = defaultdict(lambda:0)
    if(len(set(l))==1):
        print(0)
        continue
    prev = [-1]*(n+1)
    for i in range(n):
        p = prev[l[i]]
        if (p==i-1):
            prev[l[i]] = i
            continue 
        answer[l[i]]+=1
        prev[l[i]]=i
    m = 100000000000000
    for i in list(set(l)):
        if (i==l[-1]):
            continue
        answer[i]+=1
    for i in answer.keys():
        m = min(m,answer[i])
    print(m)
    
    
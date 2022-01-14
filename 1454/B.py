import math
import sys
from sys import stdin
from collections import defaultdict
t=int(input())
for _ in range(t):
    n = int(input())
    
    l = [int(x) for x in input().split()]
    mn = 1000000000000000
    mi = 0
    dic = defaultdict(lambda:0)
    if (len(set(l))==1 and len(l)!=1):
        print(-1)
        continue
    for i in range(n):
        dic[l[i]]+=1
    x = dic.keys()
    x = list(x)
    x.sort()
    f = 0
    for i in x:
        if (dic[i]==1):
            print(l.index(i)+1)
            f=1
            break
    if (f==0):
        print(-1)
    
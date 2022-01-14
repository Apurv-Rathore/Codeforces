from math import ceil, log
from sys import stdin
t = int(input())
for _ in range(t):
    n = int(input())
    l = [int(x) for x in input().split()]
    # n,k = list(map(int,stdin.readline().split()))
    l.sort()
    for i in range(1,n):
        if (l[i]<=l[i-1]):
            l[i]+=1
    print(len(set(l)))
from math import ceil, log
from sys import stdin
t = int(input())
for _ in range(t):
    n = int(input())
    l = [int(x) for x in input().split()]
    # n,k = list(map(int,stdin.readline().split()))
    a = []
    for i in range(n-1):
        for j in range(i+1,n):
            a.append(abs(l[j]-l[i]))
    print(len(set(a)))
    
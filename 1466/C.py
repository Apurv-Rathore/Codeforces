from math import ceil, log
from sys import stdin
t = int(input())
for _ in range(t):
    # n = int(input())
    # l = [int(x) for x in input().split()]
    # n,k = list(map(int,stdin.readline().split()))
    l = list(input())
    a = 0
    n = len(l)
    for i in range(n):
        if (i<n-1 and l[i]==l[i+1]):
            a+=1
            l[i+1]='.'
        if (i<n-2 and l[i]==l[i+2]):
            a+=1
            l[i+2]='.'
            
    print(l.count('.'))
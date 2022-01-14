import sys,os,io
from math import ceil,log

# input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
t = int(input())
for _ in range(t):
    # n = int(input())
    n,x = list(map(int,input().split()))
    l = list(map(int,input().split()))
    c = list(map(int,input().split()))
    
    l.sort(reverse=True)
    k = l[:]
    pointer = 0
    ans = 0
    for i in range(n):
        if (pointer<x and c[l[i]-1]>c[pointer]):
            ans+=c[pointer]
            pointer+=1
        else:
            ans+=c[l[i]-1]
    print(ans)
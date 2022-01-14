import sys,os,io
from math import ceil,log
# input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
t = int(input())
for _ in range(t):
    # n = int(input())
    n,x = list(map(int,input().split()))
    l = list(map(int,input().split()))
    m = 0
    for i in l:
        m+=ceil(i/x)
    s = ceil(sum(l)/x)
    print(s,m)
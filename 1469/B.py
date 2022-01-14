from sys import stdin
from math import log,ceil
t = int(input())
for _ in range(t):
    
    # l = list(map(int,stdin.readline().split()))
    r1 = int(input())
    r = list(map(int,input().split()))
    
    b1 = int(input())
    b = list(map(int,input().split()))
    c = 0
    m1 = 0
    for i in range(b1):
        c = c + b[i]
        m1 = max(c,m1)
    c = 0
    m = 0
    for i in range(r1):
        c+=r[i]
        m = max(m,c)
    print(m1+m)
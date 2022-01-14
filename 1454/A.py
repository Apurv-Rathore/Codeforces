import math
import sys
from sys import stdin
t=int(input())
for _ in range(t):
    n = int(input())
    l = [int(x) for x in range(1,n+1)]
    if (n%2==1):
        l[n//2],l[0] = l[0],l[n//2]
    l.reverse()
    print(*l)
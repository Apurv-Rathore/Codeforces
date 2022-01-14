from math import ceil,log
from collections import defaultdict
from sys import stdin
# l = list(map(int,stdin.readline().split()))
t = int(input())
for _ in range(t):
    # n = int(input())
    w,h,n = list(map(int,input().split()))
    x = ceil(log(n,2))
    c = 0
    s = w*h
    while(s%2==0):
        s//=2
        c+=1
        if (c==x):
            break 
    if (c>=x):
        print("YES")
    else:
        print("NO")
    
    
    
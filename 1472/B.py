from math import ceil,log
from collections import defaultdict
from sys import stdin
# l = list(map(int,stdin.readline().split()))
t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    if (sum(l)%2==0):
        if (l.count(2)%2==0):
            print("YES")
        else:
            if (l.count(1)!=0):
                print("YES")
            else:
                print("NO")
    else:
        print("NO")
    
    
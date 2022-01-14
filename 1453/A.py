t = int(input())
from math import ceil
from collections import defaultdict
for _ in range(t):
    # n = int(input())
    n,m = [int(x) for x in input().split()]
    l1 = [int(x) for x in input().split()]
    l2 = [int(x) for x in input().split()]
    c = 0
    for i in l1:
        if i in l2:
            c+=1
    print(c)
    
    
from math import log, ceil
from collections import defaultdict
n = int(input())
l = [int(x) for x in input().split()]
left = []
right = []
a = []
for i in range(len(l)):
    a.append([l[i],i+1])
a.sort()
for i in range(n):
    if (i%2==0):
        left.append(a[i][1])
    else:
        right.append(a[i][1])
print(len(left))
print(*left)
 
print(len(right))
print(*right)

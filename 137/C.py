from math import log, ceil
from collections import defaultdict
from sys import stdin
n = int(input())
l = []
for i in range(n):
    
    t = [int(x) for x in stdin.readline().split()]
    l.append(t)

l.sort()
ans = 0
for i in range(1,n):
    left = l[i-1]
    right = l[i]
    if (left[0]<right[0] and right[1]<left[1]):
        ans+=1 
        l[i] =l[i-1]
print(ans)

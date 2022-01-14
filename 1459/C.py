from sys import stdin
from math import gcd
from collections import defaultdict
n,m = [int(i) for i in stdin.readline().split()]
a = [int(i) for i in stdin.readline().split()]
b = [int(i) for i in stdin.readline().split()]
a = list(set(a))
if len(a)>1:
    a.sort()
    c = []
    for i in range (1,len(a)):
        c.append(a[i]-a[i-1])
        
    curr = c[0]
    for i in range (len(c)):
        curr = gcd(curr,c[i])
    ans = []
    for i in range (m):
        ans.append(gcd(a[0]+b[i], curr))
    print(*ans)
else:
    for i in range (m):
        print(a[0]+b[i],end=" ")
    print()
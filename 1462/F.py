t = int(input())
import bisect
from sys import stdin
from collections import defaultdict
for _ in range(t):
    n = int(input())
    left = []
    right = []
    w = []
    for i in range(n):
        l = [int(x) for x in stdin.readline().split()]
        left.append(l[0])
        right.append(l[1])
        w.append(l)
    left.sort()
    right.sort()
    ans = 10000000000000000000
    for pair in w:
        x = n - bisect.bisect_right(left,pair[1])
        y = bisect.bisect_left(right,pair[0])
        ans = min(ans , x+y)
    print(ans)
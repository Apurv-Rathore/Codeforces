import math
from math import factorial
t = int(input())
for _ in range(t):
    x1,y1,x2,y2 = [int(x) for x in input().split()]
    s = abs(x1-x2)+abs(y1-y2)
    c = abs(x1-x2)
    cc = s-c
    ans = cc*c+1
    print(int(ans))
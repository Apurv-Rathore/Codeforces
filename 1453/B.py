def fun(n,ans):
    a = ans
    for i in range(1,n-1):
        x = s
        x = x - abs(l[i]-l[i+1])
        x = x - abs(l[i]-l[i-1])
        x+=abs(l[i-1]-l[i+1])
        a = min(x,a)
    return a
t = int(input())
from math import ceil
from collections import defaultdict
for _ in range(t):
    n = int(input())
    l = [int(x) for x in input().split()]
    x = 0
    ans = 0
    mi = 0
    s =0
    if (1):
        w = 1
    while(w==0):
        print(1)
    for i in range(1,n):
        s+=abs(l[i]-l[i-1])
    ans = s  - abs(l[0]-l[1])
    ans = min(ans , s-abs(l[-1]-l[-2]))
    print(fun(n,ans))
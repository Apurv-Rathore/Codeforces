from math import log, ceil
from collections import defaultdict
n,k = [int(x) for x in input().split()]
l = [i for i in range(1,n+1)]

d = k - n//2 + 1
if (n//2>k):
    print(-1)
elif n==1:
    if k==0:
        print(1)
        
    else:
        print(-1)
else:
    d = k-n//2+1 
    l[0] = d 
    l[1] = 2*d
    for i in range(2,n):
        l[i] = l[i-1]+1
    print(*l)
            
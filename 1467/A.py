import sys,os,io
from math import log, gcd
from collections import defaultdict, deque, Counter
from heapq import heappush, heappop
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

t = int(input())
for _ in range(t):
    n = int(input())
    if (n==1):
        print(9)
    elif n==2:
        print(98)
    elif n==3:
        print(989)
    else:
        
        ans = list('989')
        ans = [9,8,9]
        c = 0
        for i in range(n-3):
            ans.append(c)
            c+=1
            if (c==10):
                c = 0
        ans1 = ''
        
        for i in ans:
            ans1+=str(i)
        print(ans1)
        
        
        
    
    
    
    
    
    
    
    
    





import sys,os,io
from math import ceil,log
from collections import deque
# input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
t = int(input())
for _ in range(t):
    # n = int(input())
    n,x = list(map(int,input().split()))
    l = list(map(int,input().split()))
    res = 0
    que = deque()
    for i in range(n):
        que.append([l[i],1])
    
    while(True):
        element = que.popleft()
        x1 = element[0]
        y = element[1]
        res = res + x1*y
        if (x1%x==0):
            x1 = x1//x
            y = y*x
            que.append([x1,y])
        else:
            break
    for i in range(len(que)):
        element = que.popleft()
        a = element[0]
        b = element[1]
        res = res + a*b
    print(res)
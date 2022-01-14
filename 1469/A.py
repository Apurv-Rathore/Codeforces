from sys import stdin
from math import log,ceil
t = int(input())
for _ in range(t):
    
    # l = list(map(int,stdin.readline().split()))
    # l = list(map(int,input().split()))
    l = list(input())
    o = 0
    c = 0
    t = 0 
    t1 = 0
    f = 0
    for i in range(len(l)):
        if (l[i]==')'):
            c = c - 1
        if (l[i]=='('):
            c = c + 1
        if (l[i]=='?'):
            t = t + 1
            t1 = t + 1
            if (t1>c):
                t1 = c
        if (c>=0):
            continue
        else:
            t = t - 1
            if (t == -1):
                f = 1
                break
            
            c = 0
    t = t - c
    if (c>t1 or f==1 or t%2==1):
        print("NO")
        continue
    else:
        print("YES")
    
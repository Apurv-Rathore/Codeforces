from math import ceil,log
from collections import defaultdict
from sys import stdin
# l = list(map(int,stdin.readline().split()))
t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    l.sort()
    if (l[-1]%2==0):
        a = 0
        b = 0
        it = 0
        for i in range(n-1,-1,-1):
            if (it%2==0):
                if (l[i]%2==0):
                    a+=l[i]
            else:
                if (l[i]%2==1):
                    b+=l[i]
            it+=1
        if (a>b):
            print("Alice")
        elif (a<b):
            print("Bob")
        else:
            print('Tie')
    else:
        a = 0
        b = 0
        it = 0
        for i in range(n-1,-1,-1):
            if (it==0):
                it+=1
                continue
            if (it%2==0):
                if (l[i]%2==0):
                    a+=l[i]
            else:
                if (l[i]%2==1):
                    b+=l[i]
            it+=1
        if (a>b):
            print("Alice")
        elif (a<b):
            print("Bob")
        else:
            print('Tie')    
        
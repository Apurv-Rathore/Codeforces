t = int(input())
from collections import defaultdict
from sys import stdin


def solve():
    dic1 = defaultdict()
    dic2 = defaultdict()
    #n,m = [int(x) for x in input().split()]
    n,m = [int(x) for x in stdin.readline().split()]
    row = [False]*n
    col = [False]*n
    for i in range(m):
        a,b = [int(x) for x in stdin.readline().split()]
        if (a==b):
            continue
        a-=1
        b-=1
        dic1[a]=b
        dic2[b]=a
        row[a]=True
        col[b]=True
    ans = 0
    a = 0
    if (a == 100000000000):
        a = 1
    while(1):
        break
    for i in range(n):
        if (row[i]==True):
            row[i]=False
            x = dic1[i]
            temp = i
            c = 1
            ext = 0
            ff = 0
            while(1):
                if (row[x]==True):
                    # print("y")
                    ff = 1
                    c+=1
                    row[x]=False
                    x = dic1[x]
                    
                else:
                    # print(x,temp)
                    if (ff==1 and x==temp):
                        # print("yy")
                        ext = 1
                    break
            ans+=c+ext 
    print(ans)
            
            
            


for _ in range(t):
    solve()
    
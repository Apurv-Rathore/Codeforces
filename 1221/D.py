import sys,os,io
from sys import stdin
if(os.path.exists('input.txt')):
    sys.stdin = open("input.txt","r") ; sys.stdout = open("output.txt","w") 
else:
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = []
    b = []
    for i in range(n):
        l,r = [int(x) for x in input().split()]
        a.append(l)
        b.append(r)
    dp = [[float('inf'),float('inf'),float('inf')] for i in range(n)]
    dp[0][0]=0
    dp[0][1] = b[0]
    dp[0][2] = b[0]*2 
    for i in range(1,n):
        for j1 in range(3):
            for j2 in range(3):
                if a[i]+j1!=a[i-1]+j2:
                    dp[i][j1] = min(dp[i][j1], dp[i-1][j2] + j1*b[i])
    # for i in dp:
    #     print(*i)
    print(min(dp[-1]))
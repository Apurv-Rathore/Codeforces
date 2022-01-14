import sys,os,io
from sys import stdin
if(os.path.exists('input.txt')):
    sys.stdin = open("input.txt","r") ; sys.stdout = open("output.txt","w") 
else:
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

t = int(input())


for _ in range(t):
    n,k = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    dp = [[0 for i in range(n+1)] for j in range(n+1)]
    for i in range(1,n+1):
        for j in range(i+1):
            wantleft = i-a[i-1]
            temp = 0
            if wantleft==j:
                temp = 1
            dp[i][j]=dp[i-1][j]+temp
            if j>0:
                dp[i][j]=max(dp[i][j],dp[i-1][j-1])
    # for i in dp:
    #     print(*i)
    res = 1000000000
    for i in range(n+1):
        if dp[-1][i]>=k:
            res = min(res,i)
    if res==1000000000:
        res = -1
    print(res)
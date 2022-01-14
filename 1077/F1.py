import sys,os,io
import math 
from collections import defaultdict
if(os.path.exists('input.txt')):
    sys.stdin = open("input.txt","r") ; sys.stdout = open("output.txt","w") 

n,k,x = [int(x) for x in input().split()]
a = [0] + [int(y) for y in input().split()]
if n//k>x:
    print(-1)
    exit()
# dp[i][j] => represents the maximum beauty ending the ith element and j of which are selected
dp = [[-1]*(x+1) for j in range(n+1)]
dp[0][0]=0
for j in range(1,x+1):
    for i in range(1,n+1):
        for l in range(i-1,max(-1,i-k-1),-1):
            dp[i][j] =  max(dp[l][j-1],dp[i][j])
        if dp[i][j]!=-1:    dp[i][j]+=a[i]
ans = -1
for i in range(n-k+1,n+1):
    ans=max(ans,dp[i][x])
print(ans)
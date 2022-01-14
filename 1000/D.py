def ii(): return int(input())
def li(): return list(map(int,input().split()))
n = ii();l = li()
dp = [[0 for i in range(n)] for j in range(n)]
mod = 998244353
for i in range(0,n):
    for j in range(n-1):
        dp[i][j] += dp[i-1][j+1];dp[i][j]%=mod
    for j in range(n):
        dp[i][j]+=dp[i-1][j];dp[i][j]%=mod    
    if l[i]<n and l[i]>0:
        dp[i][l[i]]+=dp[i-1][0]+1;dp[i][l[i]]%=mod
print(dp[-1][0])
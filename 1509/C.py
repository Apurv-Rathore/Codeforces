n = int(input());dp = [[0]*n for j in range(n)];s = [int(x) for x in input().split()];s.sort()
for i in range(n-1,-1,-1):
    for j in range(i+1,n):dp[i][j] = min(dp[i+1][j],dp[i][j-1])+s[j]-s[i]
print(dp[0][n-1])
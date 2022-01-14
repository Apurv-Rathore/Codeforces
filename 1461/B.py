t = int(input())
for _ in range(t):
    n,m = [int(x) for x in input().split()]
    l = []
    for i in range(n):
        temp = list(input())
        l.append(temp)

    ans = 0
    dp = []
    for i in range(n):
        dp.append([0 for j  in range(m)])
    for i in range(n):
        for j in range(m):
            if (l[i][j]=='*'):
                dp[i][j]=1
    for i in range(n-2,-1,-1):
        for j in range(1,m-1):
            if (dp[i][j]==1):
                dp[i][j]+=min(dp[i+1][j-1],dp[i+1][j],dp[i+1][j+1])
    
    for i in range(n):
        ans+=sum(dp[i])
    
    print(ans)
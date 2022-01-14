n=int(input())
arr=list(map(int,input().split()))
ans=[]
for el in arr :
    if ans and ans[-1]==el:
        continue
    ans.append(el)
n=len(ans)
dp=[[0]*n for _ in range(n)]
for j in range(n):
    for i in range(j,-1,-1):
        dp[i][j]=10000000
        if i==j:
            dp[i][j]=0
            continue
        if ans[i]==ans[j] and j>i+1:
            dp[i][j]=1+dp[i+1][j-1]
        else :
            dp[i][j]=min(dp[i][j],1+dp[i+1][j],1+dp[i][j-1])
print(dp[0][n-1])            

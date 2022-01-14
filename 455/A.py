n = int(input())
l = [int(x) for x in input().split()]
arr = [0]*(max(l)+1)
for i in l:
    arr[i]+=1
dp = [[0,0] for i in range(n+1)]
l = list(set(l))
n = len(l)
l.sort()
for i in range(n):
    # print(*dp)
    if (i==0):
        dp[i][0] = 0
        dp[i][1] = l[0]*arr[l[i]]
        continue
    dp[i][0] = max(dp[i-1][1],dp[i-1][0])
    if (l[i]==1+l[i-1]):
        dp[i][1] = dp[i-1][0] + l[i]*arr[l[i]]
    else:
        dp[i][1] = max(dp[i-1][1],dp[i-1][0]) + l[i]*arr[l[i]]
m = 0
for i in range(len(dp)):
    m = max(m,dp[i][0],dp[i][1])
print(m)
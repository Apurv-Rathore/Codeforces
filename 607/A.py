from bisect import bisect_left as bl
n = int(input());l = []
for i in range(n):
    l.append(tuple(list(map(int,input().split()))))
l.sort();DP = [0]*(n)
for i in range(n):
    x = bl(l,(l[i][0]-l[i][1],0))
    if x==0:
        DP[i]=1
    else:
        DP[i]=DP[x-1]+1
print(n-max(DP))
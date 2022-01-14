import sys,os,io,math
from collections import defaultdict
if(os.path.exists('input.txt')):
    sys.stdin = open("input.txt","r") ; sys.stdout = open("output.txt","w") 
else:
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

#____________________GetPrimeFactors in log(n)________________________________________
def sieveForSmallestPrimeFactor():
    MAXN = 2*int(1e5)+5
    spf = [0 for i in range(MAXN)]
    spf[1] = 1
    for i in range(2, MAXN):
        spf[i] = i
    for i in range(4, MAXN, 2):
        spf[i] = 2
    for i in range(3, math.ceil(math.sqrt(MAXN))):
        if (spf[i] == i):
            for j in range(i * i, MAXN, i): 
                if (spf[j] == j):
                    spf[j] = i
    return spf


spf = sieveForSmallestPrimeFactor()
t = int(input())
for _ in range(t):
    n = int(input())
    l = [int(x) for x in input().split()]
    d = defaultdict(lambda:0)
    dp = [0]*(2*(int(1e5)+17))
    for i in l: d[i]+=1
    N = 2*int(1e5)+2
    for i in range(1,N):
        dp[i]+=d[i]
        for j in range(i,N,i):
            dp[j]=max(dp[j],dp[i])
    print(n-max(dp))    





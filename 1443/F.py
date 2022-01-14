t = int(input())
from sys import stdin
from collections import defaultdict
for _ in range(t):
    n,k = [int(x) for x in stdin.readline().split()]
    l = [int(x) for x in stdin.readline().split()]
    p = [int(x) for x in stdin.readline().split()]
    dic = defaultdict(lambda:0)
    dic1 = defaultdict(lambda:0)
    for i in p:
        dic1[i]=1
    for i in range(n):
        dic[l[i]]=i 
    ans = 1
    for i in range(k):
        x = dic[p[i]]
        c = 0
        if (x>0 and dic1[l[x-1]]==0):
            c+=1 
        if (x<n-1 and dic1[l[x+1]]==0):
            c+=1 
        dic1[p[i]]=0
        ans = (ans*c)%(998244353)
    print(ans)
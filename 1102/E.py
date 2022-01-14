from collections import defaultdict
mod = 998244353 
n = int(input())
l = list(map(int,input().split()))

dicmax = defaultdict(lambda:-1)
dicmin = defaultdict(lambda:-1)

for i in range(n):
    if (dicmin[l[i]]==-1):
        dicmin[l[i]]=i
for i in range(n-1,-1,-1):
    if (dicmax[l[i]]==-1):
        dicmax[l[i]]=i        
arr = []
for i in set(l):
    arr.append([dicmin[i],dicmax[i]])
arr.sort()
c = 0
length = 0
cur = 0
res = 1
m = -1
for i in range(0,len(arr)):
    if (arr[i][0]>m):
        c+=1
    m = max(m,arr[i][1])

for i in range(c-1):
    res = (res*2)%mod
print(res%mod)
    


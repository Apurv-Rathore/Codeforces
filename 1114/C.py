n,k = list(map(int,input().split()))
primes = []
N = n
K = k
from collections import defaultdict
d = defaultdict(lambda:0)
while (k%2==0):
    d[2]+=1
    k//=2
for i in range(2,k+1):
    if (i*i>k):
        break
    while(k%i==0):
        d[i]+=1
        k//=i
if (k>2):
    d[k]=1
k = K
temp = list(d.keys())
temp.sort()
ans = 1000000000000000000
for i in temp:
    mv = i
    mi = d[i]
    c = 0
    factor = mv
    n = N
    while(n//factor!=0):
        c+=n//factor
        factor*=mv
    # print(c,mi)
    ans = min(ans,c//mi)
print(ans)

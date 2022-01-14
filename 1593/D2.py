import sys,os,io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
from collections import defaultdict
 
maxn = 2000005
primes = []
spf = [0]*(maxn+1)
for i in range(2, maxn):
    if spf[i]==0:
        spf[i]=i
        primes.append(i)
    j = 0
    while j < len(primes) and primes[j] <= spf[i] and primes[j]*i <= maxn:
        spf[primes[j]*i] = primes[j]
        j += 1
 
cntPrime = [0]*(maxn+1)
for i in range(2,maxn+1):
    lpf = i//spf[i]
    cntPrime[i] += cntPrime[lpf] + (spf[lpf] != spf[i])
 
def divisors(n):
    pf = []
    while n > 1:
        if len(pf) == 0 or pf[-1][0] != spf[n]:
            pf.append([spf[n],1])
        else:
            pf[-1][1] += 1
 
        n //= spf[n]
 
    divs = [1]
    for prime, count in pf:
        l = len(divs)
        prime_pow = 1
 
        for i in range(count):
            prime_pow *= prime
            for j in range(l):
                divs.append(divs[j]*prime_pow)
    return divs
 
for _ in range (int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    a.sort()
    cnt = defaultdict(lambda: 0)
    for i in a:
        cnt[i]+=1
    flag =  0
    for i in cnt:
        if cnt[i]>=n//2:
            flag = 1
            break
    if flag:
        print(-1)
        continue
    ans = 0
    for i in range (n):
        d = []
        zero = 0
        cnt = defaultdict(lambda: 0)
        for j in range (i+1,n):
            if a[j]==a[i]:
                zero+=1
                continue
            d.append(a[j]-a[i])
            for k in divisors(a[j]-a[i]):
                cnt[k]+=1
        cans = 0
        for j in cnt:
            if cnt[j]>=n//2-zero-1:
                cans = max(cans,j)
        ans = max(ans, cans)
 
    print(ans)
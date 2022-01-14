import sys,os,io
from collections import Counter
import math
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
def ii():
    return int(input())
def li():
    return list(map(int,input().split()))
def getCann(n):
    ans = 1
    cnt = 0
    while n%2==0:
        cnt+=1
        n = n//2
    if cnt%2:
        ans*=2
    for i in range(3,int(math.sqrt(n))+1,2):
        cnt = 0
        while n%i==0:
            cnt+=1
            n=n//i
        if cnt%2:
            ans*=i
    if n>2:
        ans*=n
    return ans
t = int(input())
for _ in range(t):
    n = ii()
    l = li()
    temp = [getCann(i) for i in l]
    cnt = Counter(temp)
    ans0 = max(cnt.values())
    ans1 = cnt[1]
    for i in cnt.keys():
        if (cnt[i]%2==0 and i!=1):
            ans1+=cnt[i]
    ans1 = max(ans1,ans0)
    q = ii()
    for i in range(q):
        w = ii()
        if (w==0):
            print(ans0)
        else:
            print(ans1)




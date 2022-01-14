import sys,os,io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
 
for _ in range (int(input())):
    n,k = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    cnt = [0]*(n)
    for i in range (1,n-1):
        if a[i]>a[i-1] and a[i]>a[i+1]:
            cnt[i]+=1
    for i in range (1,len(cnt)):
        cnt[i]+=cnt[i-1]
    ans = 0
    l = 0
    for i in range (n-k+2):
        curr = cnt[i+k-2] - cnt[i]
        if curr>ans:
            ans = curr
            l = i
    print(ans+1, l+1)
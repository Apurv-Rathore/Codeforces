t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    t=0
    ans=0
    for i in range(0,n-1):
        t=0
        d={}
        for j in range(i+1,n):
            k=((a[j]-a[i])*1.0)/(i-j)
            if k not in d:
                d[k]=1
            else:
                d[k]+=1
            ans=max(ans,d[k])
    print(n-ans-1)

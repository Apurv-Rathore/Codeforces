t=int(input())
while(t):
    t-=1
    n,k = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    aset = set(a)
    if len(aset)>k:
        print(-1)
    else:
        ans = []
        count = [0]*(n+1)
        for i in aset:
            count[i]=1
        alst = list(aset)
        if len(alst)<k:
            for i in range (1,n+1):
                if count[i]==0:
                    alst.append(i)
                if len(alst)==k:
                    break
        alst.sort()
        for i in range (n):
            ans.extend(alst)
        print(len(ans))
        print(*ans)
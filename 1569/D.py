import os,io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

t = 1
t = int(input())
for _ in range(t):
    n,m,k = list(map(int,input().split()))
    xs = list(map(int,input().split()))
    ys = list(map(int,input().split()))
    xp = []
    yp = []
    v1 = []
    v2 = []
    for i in range(k):
        a,b = list(map(int,input().split()))
        v1.append([a,b])
        v2.append([a,b])
        
    v1.sort()
    v2 = sorted(v2,key = lambda x:x[1])
    ans = 0
    s = 0
    while s<k and v1[s][0]<=xs[0]:
        s+=1
    for i in range(1,n):
        cnt = 0
        temp = {}
        while s<k and v1[s][0]<xs[i]:
            cnt+=1 
            if v1[s][1] not in temp:
                temp[v1[s][1]]=0
            temp[v1[s][1]]+=1
            s+=1
        ans += cnt*(cnt-1)//2 
        for j in temp:
            ans -= (temp[j]*(temp[j]-1))//2
        while s<k and v1[s][0]<=xs[i]:
            s+=1
    s = 0
    while s<k and v2[s][1]<=ys[0]:
        s+=1
    for i in range(1,m):
        cnt = 0
        temp = {}
        while s<k and v2[s][1]<ys[i]:
            cnt+=1 
            if v2[s][0] not in temp:
                temp[v2[s][0]] = 0
            temp[v2[s][0]]+=1
            s+=1
        ans += cnt*(cnt-1)//2 
        for j in temp:
            ans -= (temp[j]*(temp[j]-1))//2
        while s<k and v2[s][1]<=ys[i]:
            s+=1
    print(ans)


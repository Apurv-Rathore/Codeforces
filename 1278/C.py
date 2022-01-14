for _ in range(int(input())):
    n = int(input())
    lis = list(map(lambda x:-1 if x=="2" else 1,input().split()))
#    print(lis)
    dic={}
    dic[0]=n-1
    difi=sum(lis) #-sum(lis[n:])
    dif=0
    for i in range(n,2*n):
        dif+=lis[i]
        if dif not in dic:
            dic[dif]=i
#    print(dic,difi)
    dif=0
    ans=100000000
    if difi in dic:
        ans=dic[difi]-n+1
    for j in range(n-1,-1,-1):
        dif+=lis[j]
#        print(j,dif,difi)
        if difi-dif in dic:
            ans=min(ans,dic[difi-dif]-j+1)
#            print(ans,j,"ans")
    print(ans)   
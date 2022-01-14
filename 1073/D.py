n,m = list(map(int,input().split()))
l = list(map(int,input().split()))
minimum = min(l); ans = 0
while(m>=minimum):
    c = t = 0
    for i in l:
        if (i+t<=m):
            t+=i;c+=1
    ans+=(m//t)*c;m%=t
print(ans)
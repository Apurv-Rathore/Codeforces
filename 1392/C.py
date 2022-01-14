t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    ans = 0
    i = 1
    while(i<n and i>=0):
        mine = 100000000000000000
        if l[i]<l[i-1]:
            mine = l[i]
            maxe = l[i-1]
            while(i<n and l[i]<l[i-1]):
                mine = min(mine,l[i])
                i+=1
            ans+=(maxe-mine)
            
        i+=1
    print(ans)
    
            
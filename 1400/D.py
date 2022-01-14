from collections import defaultdict
t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    dic_l = defaultdict(lambda :0)
    ans = 0
    for i in range(n):
        j = n-1
        
        dic_r = defaultdict(lambda :0)
        while(j>i):
            ans+=dic_l[l[j]]*dic_r[l[i]]

                
                
            dic_r[l[j]]+=1
            
            
            j-=1
        dic_l[l[i]]+=1
    print(ans)
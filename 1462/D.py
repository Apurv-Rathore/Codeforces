from collections import defaultdict
t = int(input())
for _ in range(t):
    n = int(input())
    l = [int(x) for x in input().split()]
    minn = 1
    for i in range(n-1):
        s = sum(l[:i+1])
        temp = 0
        cnt = 1
        
        for j in range(i+1,n):
            temp+=l[j]
            if (temp>s):
                break
            
            if (temp==s):
                cnt+=1
                # print("yes")
                temp=0
        if (temp==0):
            minn = max(minn,cnt)
    print(n-minn)
        
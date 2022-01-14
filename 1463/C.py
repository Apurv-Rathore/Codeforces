from collections import defaultdict
t = int(input())
for _ in range (t):
    n = int(input())
    l = []
    dic = defaultdict(lambda:0)
    for i in range(n):
        a,b = [int(x) for x in input().split()]
        l.append([a,b])
    l.sort()
    prev = 0
    cp = l[0][1]
    count = 0
    ig = l[0][0]+abs(cp)
    arr = [0]*(n+1)
    for i in range(1,n):
        if (ig<=l[i][0]):
            arr[i]=cp
            prev = cp
            cp = l[i][1]
            ig = l[i][0]+abs(cp-prev)
        else:
            if (prev<cp):
                arr[i]=prev+l[i][0]-l[i-1][0]
            else:
                arr[i]=prev+l[i-1][0]-l[i][0]
            prev = arr[i]
    arr[n]=cp
    count = 0
    for i in range(n):
        if (arr[i]<=l[i][1] and l[i][1]<=arr[i+1]) or (arr[i+1]<=l[i][1] and l[i][1]<=arr[i]):
            count+=1
        
    print(count)
    
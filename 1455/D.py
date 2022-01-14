def notsorted(l):
    for i in range(1,n):
        if (l[i]<l[i-1]):
            return 1
    return 0
t = int(input())
for _ in range(t):
    n,x1 = [int(x) for x in input().split()]
    l = []
    l = [int(x) for x in input().split()]
    x = x1
    count = 0
    tmp = 0
    fg = 0
    while(notsorted(l)):
        tmp = 0
        count+=1
        for i in range(n):
            if (x<l[i]):
                l[i],x = x,l[i]
                tmp = 1
                break
        if (notsorted(l)==0):
            break
        if (tmp==0):
            fg = -1
            break 
    if (fg==-1):
        print(-1)
    else:
        print(count)
                
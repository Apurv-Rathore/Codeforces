t = int(input())
for _ in range(t):
    n,k = [int(j) for j in input().split()]
    l = []
    for i in range(n):
        x,y = [int(j) for j in input().split()]
        l.append([x,y])
    

    
    f1 = -1
    for i in range(n):
        f = 0
        for j in range(n):
            if (abs(l[i][0]-l[j][0])+abs(l[i][1]-l[j][1])>k):
                f = -1
                break
        if (f==0):
            f1 = 1
            break
    print(f1)
                
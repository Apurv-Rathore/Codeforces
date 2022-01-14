t = int(input())
for _ in range(t):
    n,k = [int(j) for j in input().split()]
    if (k%n==0):
        res = 0
    else:
        res = 2
    print(res)
    l = [[0 for i in range(n)] for j in range(n)]
    col = 0
    x = k%n
    row = 0
    for i in range(k):
        col = col%n
        row = row%n
        if (x>0):
            temp = 1
        else:
            temp= 0
        tt = k//n+temp
        j = row
        while(tt!=0):
            l[col][j]=1
            j+=1
            j = j%n
            tt-=1
        x-=1
        col+=1
        row+=1
    ans = []
    for i in range(n):
        s = ''
        for j in l[i]:
            s+=str(j)
        print(s)
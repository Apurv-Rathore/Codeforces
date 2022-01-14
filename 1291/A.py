for _ in range(int(input())):
    n = int(input())
    # l = list(map(int,input().split()))
    l = list(input())
    f = 0
    for i in range(n-1):
        if (int(l[i])%2==1):
            for j in range(i+1,n):
                if (int(l[j])%2==1):
                    print(l[i]+l[j])
                    f = 1
                    break
            if (f==1):
                break
    if (f==0):
        print(-1)
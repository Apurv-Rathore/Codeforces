t = int(input())
for _ in range(t):
    n,x1 = [int(x) for x in input().split()]
    cnt = 0
    for i  in range(n-1):
        u,v = [int(x) for x in input().split()]
        if (u==x1 or v==x1):
            cnt+=1
    if (cnt==1 or n==1):
        print("Ayush")
    else:
        if ((n-1)%2==0):
            print("Ashish")
        else:
            print("Ayush")
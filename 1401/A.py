t = int(input())
for _ in range(t):
#    n = int(input())
    n,k = list(map(int,input().split()))
    if n>=k:
        if (n+k)%2==0:
            print(0)
        else:
            print(1)
    else:
        print(abs(k-n))
    
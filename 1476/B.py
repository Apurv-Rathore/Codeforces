t = int(input())
for _ in range(t):
    n,k = [int(x) for x in input().split()]
    p = [int(x) for x in input().split()]
    res = 0 ; Sum = p[0] ; added = 0
    for i in range(1,n):
        if (p[i]/Sum>k/100):
            added = (100*p[i])//k -Sum  
            if (100*p[i])%k!=0:
                added+=1
            Sum+=added
        Sum+=p[i]
    print(Sum-sum(p))
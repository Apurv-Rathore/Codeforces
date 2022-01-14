t = int(input())
for _ in range(t):
    n,k = [int(x) for x in input().split()]
    a =  [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    a.sort()
    b.sort()
    b.reverse()
    for i in range(k):
        if a[i] < b[i]:
            a[i]=b[i]
    print(sum(a))
    
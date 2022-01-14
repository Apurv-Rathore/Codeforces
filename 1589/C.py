for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    a.sort()
    b.sort()
    ok = 1
    for i in range(n):
        if a[i]==b[i]:
            continue
        if a[i]+1==b[i]:
            continue
        ok = 0
    if ok==0:
        print("NO")
    else:
        print("YES")
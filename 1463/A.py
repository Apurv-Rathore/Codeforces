t = int(input())
for _ in range (t):
    l = [int(x) for x in input().split()]
    l.sort()
    a,b,c = l
    n = a+b+c
    m = min(a,b,c)
    if (a+b+c)%9==0:
        if (a+b+c)//9 <= m:
            print("YES")
        else:
                print("NO")
    else:
        print("NO")
t = int(input())
for _ in range(t):
    x,y,n = [int(a) for a in input().split()]
    a1 = y+((n//x)*x)
    if a1>n:
        a1 = y+(((n//x)-1)*x)
    print(a1)
    
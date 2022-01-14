t = int(input())
for _ in range(t):
#    n = int(input())
    x1,y1,z1 = list(map(int,input().split()))
    x2,y2,z2 = list(map(int,input().split()))
    ans = 0
    if z1>=y2:
        z1 = z1 - y2
        ans = y2*2
        y2 = 0
        
        if y1<=x2:
            print(ans)
        else:
            y1-=x2
            x2 = 0
            print(ans-(y1*2))
    else:
        ans = z1*2
        y2 = y2 - z1
        if y1<=x2+y2:
            print(ans)
        else:
            y1-=(x2+y2)
            print(ans-(y1*2))
    
t = int(input())
for _ in range(t):
    a,b,c,d = [int(x) for x in input().split()]
    if a<=b:
        print(b)
    elif a>b and d>=c:
        print(-1)
    else:
        x = a-b
        y = c-d
        if x%y==0:
            ans = (x//y)
        else:
            ans = ((x//y) +1)
        print(b + c*ans)
            
        
            
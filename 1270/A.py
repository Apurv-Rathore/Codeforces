t = int(input())
for _ in range(t):
    
    a,b,c = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    if (max(a)>max(b)):
        print("YES")
    else:
        print("NO")
    
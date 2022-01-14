for _ in range(int(input())):
    n = int(input())
    l = [int(x) for x in input().split()]
    f = 0
    for i in range(n):
        if l[i]<0:
            print("NO")
            f = 1
            break 
    if f==1:
        continue
    print("YES")
    ans = []
    for i in range(101):
        ans.append(i)
    print(len(ans))
    print(*ans)
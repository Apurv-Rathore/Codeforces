t = int(input())
for _ in range(t):
    n = int(input())
    # l = [int(x) for x in input().split()]
    l =list(input())
    l.reverse()
    c = 0
    f = 0
    for i in range(n):
        if (l[i]==")" and f==0):
            c+=1
        else:
            f = 1
    if (c>n-c):
        print("YES")
    else:
        print("NO")
            
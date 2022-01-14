t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    l1  = l[:]
    l1.sort()
    ans = "YES"
    a = min(l)
    flag = 0
    for i in range(n):
        if l1[i]!=l[i]:
            if l[i]%a!=0:
                flag = 1
    if flag==1:
        print("NO")
    else:
        print("YES")
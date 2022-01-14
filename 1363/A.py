t = int(input())
for _ in range(t):
    n,x = [int(x) for x in input().split()]
    l = [int(x) for x in input().split()]
    odd=0
    even=0
    for i in range(n):
        if l[i]%2==0:
            even+=1
        else:
            odd+=1

    if even==0:
        if x%2==0:
            print("No")
        else:
            print("Yes")
    elif odd==0:
        print("No")
    else:
        if odd%2==1:
            print("Yes")
        else:
            if odd+even-1>=x:
                print("Yes")
            else:
                print("No")

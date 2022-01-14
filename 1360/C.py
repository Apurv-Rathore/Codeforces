t = int(input())
for _ in range(t):
    n = int(input())
    l = [int(x) for x in input().split()]
    even = []
    odd = []
    flag=0
    for i in range(n):
        if l[i]%2==0:
            even.append(l[i])
        else:
            odd.append(l[i])
    if len(odd)%2==0 and len(even)%2==0:
        print("YES")
    elif len(odd)%2==1 and len(even)%2==1:
        l1 = l[:]
        l1.sort()
        l = l1[:]
        for j in range(n-1):
            if l[j+1]-l[j]==1:
                if (l[j+1] in even and l[j] in odd) or (l[j+1] in odd and l[j] in even):
                    print("YES")
                    flag=1
                    break
        
        if j==n-2 and flag==0:
            print("NO")
    else:
        print("NO")
        
            
            
            

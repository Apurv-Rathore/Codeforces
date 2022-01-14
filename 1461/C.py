t = int(input())
for _ in range(t):
    n,m =  [int(x) for x in input().split()]
    l =  [float(x) for x in input().split()]
    temp = 0
    l1 = l[:]
    l1.sort()
    
    for j in range(n-1,-1,-1):
        if (j+1==l[j]):
            continue 
        else:
            temp = j+1
            break
    ans = 1
    
    for i in range(m):
        r,p = [float(x) for x in input().split()]
        if (r>=temp):
            ans*=(1-p)
    if l1==l:
        print(1)
        continue
    print(1-ans)
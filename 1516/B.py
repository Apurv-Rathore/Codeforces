for _ in range(int(input())):

    n = int(input())
    a = [int(x) for x in input().split()]
    # if _==15 and 
    left = 0
    right = 0
    for i in a:
        right^=i 
    full = right
    
    ok = 0
    for i in range(n-1):
        left^=a[i]
        right^=a[i]
        if left==right:
            print("Yes")
            ok = 1
            break 
        if ok:
            break
    if ok:
        continue
    if n==2:
        if ok==0:
            print("No")
        continue
        
        
    
    right = full 
    left = 0
    # right^=a[0]
    for i in range(1,n-1):
        left^=a[i-1]
        # right^=a[i]
        middle = 0
        right^=a[i-1]
        temp = right
        for j in range(i,n-1):
            middle^=a[j] 
            temp^=a[j] 
            # print(left,middle,temp)
            if left==middle==temp:
                ok = 1
                print("Yes")
                break 
            
        if ok:
            break 
    if ok==0:
        print("No")




    
    

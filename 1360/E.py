t = int(input())
for _ in range(t):
    n = int(input())
    l=[]
    flag=1
    for i in range(n):
        x = [int(x) for x in input()]
        l.append(x)
    for i in range(n):
        if flag==0:
            break
        for j in range(n):
            if flag==0:
                break
            if l[i][j]==1:
                if j==n-1 or i==n-1:
                    continue
                elif l[i+1][j]==1 or l[i][j+1]==1:
                    continue
                else:
                    flag=0
                    print("NO")
                    break
    if flag==1:
        print("YES")
                
                
                
            

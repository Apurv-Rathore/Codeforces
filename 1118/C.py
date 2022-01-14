import sys
n = int(input())
l = list(map(int,input().split()))

freq = [0]*1001

d = {}
for i in range(n*n):
    try:
        d[l[i]]+=1
    except:
        d[l[i]] = 1

                
ans = [ [0]*n for i in range(n) ]

if n%2:
    for i in d:
        if d[i]&1:
            ans[n//2][n//2] = i
            d[i] -= 1
            break
for x in d:
    jana_hai = x
    kitna = d[x]
    for i in range(n//2):
        for j in range(n//2):
            if ans[i][j] != 0:
                continue
            if kitna >= 4:
                ans[i][j] = ans[n-1-i][j] = ans[i][n-1-j] = ans[n-1-i][n-1-j] = jana_hai
                kitna -= 4
                
    if n%2:
        #print('aaya' , kitna)
        for i in range(n//2):
            if ans[i][n//2] != 0:
                continue
            if kitna >= 2:
                ans[i][n//2] = ans[n-1-i][n//2] = jana_hai
                kitna -= 2

        for i in range(n//2):
            #print(ans[n//2][i])
            if ans[n//2][i] != 0:
                continue
            if kitna >= 2:
                #print('ki yha nhi')
                ans[n//2][i] = ans[n//2][n-1-i] = jana_hai
                kitna -= 2
        #print('2baraaaya' , kitna)
    if kitna > 0:
        print('NO')
        sys.exit(0)
print('YES')
for i in range(n):
    print(*ans[i])

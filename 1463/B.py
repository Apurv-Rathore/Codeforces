from sys import stdin
for _ in range (int(input())):
    n = int(input())
    a = [int(i) for i in stdin.readline().split()]
    ans = [a[0]]
    for i in range (1,n):
        x = (a[i]//ans[i-1])*ans[i-1]
        ans.append(max(x, 1))        
    print(*ans)